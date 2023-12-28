$(document).ready(function() {
    // Hide the edit form initially
    $("#editForm").hide();

    // Function to toggle between read-only and edit mode
    $("#editButton").click(function() {
        $("#readOnlyMode").toggle();
        $("#editForm").toggle();
    });

    $("#cancelButton").click(function() {
        $("#editForm").hide();
        $("#readOnlyMode").show();
    });
});