// confirmation.js
function openModal() {
    var modal = document.getElementById('deleteConfirmationModal');
    modal.style.display = 'block';
}

function closeModal() {
    var modal = document.getElementById('deleteConfirmationModal');
    modal.style.display = 'none';
}

function deleteAccount() {
    var form = document.querySelector('.delete-account-form');
    form.submit();
}
