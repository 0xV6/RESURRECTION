document.addEventListener('DOMContentLoaded', () => {
    // User Registration Modal
    const userRegistrationModal = document.getElementById('userRegistrationModal');
    const registerUserBtn = document.getElementById('registerUserBtn');
    const closeUserModalBtn = document.getElementById('closeUserModal');
    const userRegistrationForm = document.getElementById('userRegistrationForm');

    // Hospital Registration Modal
    const hospitalRegistrationModal = document.getElementById('hospitalRegistrationModal');
    const registerHospitalBtn = document.getElementById('registerHospitalBtn');
    const closeHospitalModalBtn = document.getElementById('closeHospitalModal');
    const hospitalRegistrationForm = document.getElementById('hospitalRegistrationForm');

    // Modal Event Listeners
    registerUserBtn.addEventListener('click', () => {
        userRegistrationModal.style.display = 'flex';
    });

    closeUserModalBtn.addEventListener('click', () => {
        userRegistrationModal.style.display = 'none';
    });

    registerHospitalBtn.addEventListener('click', () => {
        hospitalRegistrationModal.style.display = 'flex';
    });

    closeHospitalModalBtn.addEventListener('click', () => {
        hospitalRegistrationModal.style.display = 'none';
    });

    // Form Submission Handlers
    userRegistrationForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = Object.fromEntries(new FormData(userRegistrationForm));

        try {
            const response = await fetch('http://localhost:5000/register_user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            if (result.status === 'success') {
                alert('User registered successfully!');
                userRegistrationModal.style.display = 'none';
                userRegistrationForm.reset();
            } else {
                alert(result.message || 'User registration failed');
            }
        } catch (error) {
            console.error('User Registration Error:', error);
            alert('User registration failed: ' + error.message);
        }
    });

    hospitalRegistrationForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = Object.fromEntries(new FormData(hospitalRegistrationForm));

        try {
            const response = await fetch('http://localhost:5000/register_hospital', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            if (result.status === 'success') {
                alert('Hospital registered successfully!');
                hospitalRegistrationModal.style.display = 'none';
                hospitalRegistrationForm.reset();
            } else {
                alert(result.message || 'Hospital registration failed');
            }
        } catch (error) {
            console.error('Hospital Registration Error:', error); 
            alert('Hospital registration failed: ' + error.message);
        }
    });

    // Donation Form Handler
    const donationForm = document.getElementById('donationForm');
    if (donationForm) {
        donationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = Object.fromEntries(new FormData(donationForm));

            try {
                const response = await fetch('http://localhost:5000/donate_blood', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();
                if (result.status === 'success') {
                    alert('Donation offer submitted successfully!');
                    donationForm.reset();
                } else {
                    alert(result.message || 'Donation offer submission failed');
                }
            } catch (error) {
                console.error('Donation Offer Error:', error);
                alert('Donation offer submission failed: ' + error.message);
            }
        });
    }

    // Utility Functions
    function getUrgencyClass(urgency) {
        switch(urgency.toLowerCase()) {
            case 'critical':
                return 'urgency-critical';
            case 'urgent':
                return 'urgency-urgent';
            default:
                return 'urgency-normal';
        }
    }

    function formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    // Clipboard Function with Toast Notification
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            // Create toast notification
            const toast = document.createElement('div');
            toast.textContent = 'Phone number copied!';
            toast.className = 'fixed bottom-4 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
            document.body.appendChild(toast);

            // Remove toast after 2 seconds
            setTimeout(() => {
                toast.remove();
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy:', err);
            alert('Failed to copy phone number');
        });
    }

    // Fetch and Display Blood Posts
    async function fetchBloodPosts() {
        const postsContainer = document.getElementById('postsContainer');

        try {
            const response = await fetch('http://localhost:5000/get_blood_posts');
            const result = await response.json();

            if (result.status === 'success') {
                postsContainer.innerHTML = '';

                result.posts.forEach(post => {
                    const postElement = document.createElement('div');
                    postElement.classList.add(
                        'bg-gray-700',
                        'rounded-lg',
                        'p-4',
                        'shadow-md',
                        'hover:shadow-lg',
                        'transition-all',
                        'mb-4'
                    );

                    postElement.innerHTML = `
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="text-xl font-bold text-white mb-2">${post.name}</h3>
                                <div class="flex items-center space-x-2 mb-2">
                                    <span class="blood-type-tag ${getUrgencyClass(post.urgency)}">
                                        ${post.blood_type}
                                    </span>
                                    <span class="text-sm text-gray-400 ${getUrgencyClass(post.urgency)}">
                                        ${post.urgency.toUpperCase()} NEED
                                    </span>
                                </div>
                                <p class="text-gray-300 mb-2">
                                    <i class="fas fa-phone mr-2"></i>
                                    <span class="phone-number">${post.phone}</span>
                                </p>
                                <p class="text-gray-300 mb-2">
                                    <i class="fas fa-map-marker-alt mr-2"></i>${post.address}
                                </p>
                            </div>
                            <div class="text-right">
                                <span class="text-sm text-gray-400">
                                    ${formatDate(post.created_at)}
                                </span>
                            </div>
                        </div>
                        <div class="mt-4 flex justify-end">
                            <button
                                class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition-colors flex items-center"
                                onclick="copyToClipboard('${post.phone}')"
                            >
                                <i class="fas fa-phone mr-2"></i>
                                Contact
                            </button>
                        </div>
                    `;

                    postsContainer.appendChild(postElement);
                });
            } else {
                postsContainer.innerHTML = `
                    <div class="text-center text-gray-400">
                        No blood posts available
                    </div>
                `;
            }
        } catch (error) {
            console.error('Error fetching blood posts:', error);
            postsContainer.innerHTML = `
                <div class="text-center text-red-500">
                    Failed to load blood posts
                </div>
            `;
        }
    }

    // Initialize Blood Posts and set up auto-refresh
    fetchBloodPosts();

    // Auto refresh every 30 seconds (30000 milliseconds)
    setInterval(fetchBloodPosts, 30000);

    // Make copyToClipboard function available globally
    window.copyToClipboard = copyToClipboard;
});




