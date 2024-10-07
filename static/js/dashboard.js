// admin_dashboard.js

document.addEventListener('DOMContentLoaded', () => {
    // Example data fetching simulation
    fetchActiveRentals();
    fetchTotalUsers();
    fetchTotalBikes();
    fetchRecentActivity();
});

function fetchActiveRentals() {
    // Simulate fetching data
    setTimeout(() => {
        document.getElementById('active-rentals-count').textContent = '120';
    }, 1000);
}

function fetchTotalUsers() {
    // Simulate fetching data
    setTimeout(() => {
        document.getElementById('total-users-count').textContent = '350';
    }, 1000);
}

function fetchTotalBikes() {
    // Simulate fetching data
    setTimeout(() => {
        document.getElementById('total-bikes-count').textContent = '200';
    }, 1000);
}

function fetchRecentActivity() {
    // Simulate fetching data
    setTimeout(() => {
        document.getElementById('recent-activity-list').innerHTML = `
            <p>User JohnDoe updated profile.</p>
            <p>Bike ID 45 checked out for rental.</p>
            <p>New bike added: Trek 2024.</p>
        `;
    }, 1000);
}
