// Function to display the message for a few seconds and then hide it
function showMessage() {
    let message = document.querySelector('.popup-message');
    message.classList.add('show');
    setTimeout(function () {
        message.classList.remove('show');
    }, 3000); // Change the duration (in milliseconds) as needed
}

// Call the showMessage function when the page loads
document.addEventListener('DOMContentLoaded', function() {
    showMessage();
});
