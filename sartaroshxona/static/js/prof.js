$(document).ready(function() {
    // User Profile Edit Toggle
    $("#editUserButton").click(function() {
        $("#readOnlyUserMode").hide();
        $("#editUserForm").show();
        // Reset password input fields to read-only
        $("#old_password").prop('readonly', 'readonly');
        $("#new_password").prop('readonly', 'readonly');
        $("#confirm_password").prop('readonly', 'readonly');
    });

    $("#cancelUserButton").click(function() {
        $("#editUserForm").hide();
        $("#readOnlyUserMode").show();
    });

    // Barber Profile Edit Toggle
    $("#editBarberButton").click(function() {
        $("#readOnlyBarberMode").hide();
        $("#editBarberForm").show();
    });

    $("#cancelBarberButton").click(function() {
        $("#editBarberForm").hide();
        $("#readOnlyBarberMode").show();
    });

    // Toggle between read-only and edit modes for services
    $("#editServiceButton").click(function() {
        $("#readOnlyServiceMode").hide();
        $("#editServiceForm").show();
    });

    $("#cancelServiceButton").click(function() {
        $("#editServiceForm").hide();
        $("#readOnlyServiceMode").show();
    });

    // Password Change Edit Toggle
    $("#editPasswordButton").click(function() {
        $("#readOnlyPasswordMode").hide();
        $("#editPasswordForm").show();
    });

    $("#cancelPasswordButton").click(function() {
        $("#editPasswordForm").hide();
        $("#readOnlyPasswordMode").show();
    });

    // Additional logic for submitting forms via AJAX or other methods
    // ...
});
