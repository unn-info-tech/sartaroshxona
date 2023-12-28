$(document).ready(function() {
    // User Profile Edit Toggle
    $("#editUserButton").click(function() {
        $("#readOnlyMode").hide();
        $("#editUserForm").show();
    });

    $("#cancelUserButton").click(function() {
        $("#editUserForm").hide();
        $("#readOnlyMode").show();
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

    // Additional logic for submitting forms via AJAX or other methods
    // ...
});
