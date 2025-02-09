document.addEventListener('DOMContentLoaded', function() {
    // Fetch donation history from the database
    fetchDonationHistory();
});

function fetchDonationHistory() {
    // This would typically be an API call to your backend
    const mockHistory = [
        {
            date: '2025-01-15',
            bloodType: 'A+',
            hospital: 'City General Hospital',
            status: 'Completed'
        },
        {
            date: '2024-12-20',
            bloodType: 'A+',
            hospital: 'Medical Center',
            status: 'Completed'
        }
        // Add more mock data as needed
    ];

    displayHistory(mockHistory);
}

function displayHistory(history) {
    const tableBody = document.getElementById('historyTableBody');
    tableBody.innerHTML = '';

    history.forEach(donation => {
        const row = document.createElement('tr');
        row.className = 'border-t border-gray-700';
        row.innerHTML = `
            <td class="px-4 py-3">${formatDate(donation.date)}</td>
            <td class="px-4 py-3">${donation.bloodType}</td>
            <td class="px-4 py-3">${donation.hospital}</td>
            <td class="px-4 py-3">
                <span class="px-2 py-1 rounded ${getStatusClass(donation.status)}">
                    ${donation.status}
                </span>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

function getStatusClass(status) {
    switch (status.toLowerCase()) {
        case 'completed':
            return 'bg-green-500 text-white';
        case 'scheduled':
            return 'bg-blue-500 text-white';
        case 'cancelled':
            return 'bg-red-500 text-white';
        default:
            return 'bg-gray-500 text-white';
    }
}