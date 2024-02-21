$(document).ready(function() {
    // User Profile Edit Toggle
    $("#editUserButton").click(function() {
        $("#readOnlyUserMode").hide();
        $("#editUserForm").show();
        
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

     
    // Show Add Service Form
    $("#showAddServiceForm").click(function() {
        $("#showAddServiceForm").hide();
        $("#addServiceForm").show();
    });

    // Hide Add Service Form and Reset on Cancel
    $("#cancelAddService").click(function() {
        $("#addServiceForm").hide();
        $("#showAddServiceForm").show();
        // Additional logic to reset form fields if needed
    });

    
    // Additional logic for submitting forms via AJAX or other methods
    // ...
});
