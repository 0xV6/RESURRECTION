document.addEventListener('DOMContentLoaded', function() {
    // Initial load of donation offers
    loadDonationOffers();
    displaySystemInfo();

    // Add event listeners for filters
    document.getElementById('bloodTypeFilter').addEventListener('change', loadDonationOffers);
    document.getElementById('dateSort').addEventListener('change', loadDonationOffers);
});

function displaySystemInfo() {
    fetch('http://localhost:5000/system_info')
        .then(response => response.json())
        .then(data => {
            // You can add elements to display this information if needed
            console.log('System Info:', data);
        })
        .catch(error => console.error('Error fetching system info:', error));
}

function loadDonationOffers() {
    const bloodType = document.getElementById('bloodTypeFilter').value;
    const sort = document.getElementById('dateSort').value;

    fetch(`http://localhost:5000/get_donation_offers?blood_type=${bloodType}&sort=${sort}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayDonationOffers(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error loading donation offers');
        });
}

function displayDonationOffers(offers) {
    const tableBody = document.getElementById('donationOffersTableBody');
    tableBody.innerHTML = '';

    offers.forEach(offer => {
        const row = document.createElement('tr');
        row.className = 'border-t border-gray-700 hover:bg-gray-700';

        row.innerHTML = `
            <td class="px-4 py-3 text-center">
                <span class="px-2 py-1 rounded bg-blue-500">
                    ${offer.blood_type}
                </span>
            </td>
            <td class="px-4 py-3">${formatDate(offer.last_donation_date)}</td>
            <td class="px-4 py-3">${offer.medical_conditions || 'None'}</td>
            <td class="px-4 py-3">${offer.availability}</td>
            <td class="px-4 py-3">${offer.contact}</td>
            <td class="px-4 py-3">${formatDateTime(offer.created_at)}</td>
        `;

        tableBody.appendChild(row);
    });
}

function formatDate(dateString) {
    if (!dateString) return 'N/A';
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

function formatDateTime(dateTimeString) {
    if (!dateTimeString) return 'N/A';
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    return new Date(dateTimeString).toLocaleDateString(undefined, options);
}