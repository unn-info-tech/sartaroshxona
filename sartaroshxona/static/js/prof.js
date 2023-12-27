// Get HTML elements
const editButton = document.getElementById('editButton');
const editForm = document.getElementById('editForm');
const saveButton = document.getElementById('saveButton');
const cancelButton = document.getElementById('cancelButton');

// Function to toggle between display modes
function toggleEditMode() {
    if (editForm.style.display === 'none') {
        editButton.style.display = 'none';
        editForm.style.display = 'block';
    } else {
        editButton.style.display = 'block';
        editForm.style.display = 'none';
    }
}

// Event listener for Edit button
editButton.addEventListener('click', () => {
    toggleEditMode();
});

// Event listener for Cancel button
cancelButton.addEventListener('click', () => {
    toggleEditMode();
});

// Event listener for Save button
saveButton.addEventListener('click', () => {
    // Retrieve values from form fields
    const newUsername = document.getElementById('usernameField').value;
    const newEmail = document.getElementById('emailField').value;
    // Send data to the server for saving/updating user information (use AJAX/fetch)
    // Toggle back to read-only mode after saving
    toggleEditMode();
});
