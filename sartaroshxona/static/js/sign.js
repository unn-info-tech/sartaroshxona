document.addEventListener("DOMContentLoaded", function() {
    // Get references to the trigger links
    const triggerLinks = document.querySelectorAll(".trigger");
  
    // Loop through each trigger link
    triggerLinks.forEach(function(link) {
      // Add click event listener to each link
      link.addEventListener("click", function(e) {
        e.preventDefault();
  
        // Find the parent form group element
        const formGroup = this.closest(".formGroup");
  
        // Toggle the 'active' class on the form container
        const formContainers = formGroup.querySelectorAll(".formContainer");
        formContainers.forEach(function(container) {
          container.classList.toggle("active");
        });
      });
    });
  });
  