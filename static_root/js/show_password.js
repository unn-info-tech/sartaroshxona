// password-toggle.js

document.addEventListener('DOMContentLoaded', function () {
    const passwordFields = document.querySelectorAll('.toggle-password');

    passwordFields.forEach(function (eyeIcon) {
        eyeIcon.addEventListener('click', function () {
            const passwordField = document.getElementById(this.getAttribute('toggle'));
            const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordField.setAttribute('type', type);
            this.classList.toggle('active');
        });
    });
});
