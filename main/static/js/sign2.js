$(document).ready(function() {
  // Initially hide all tabs except the first one
  $('.tab-content > div').not(':first').hide();

  // Handle tab switching on click
  $('.tab-group a').on('click', function(e) {
    e.preventDefault();

    // Get the target ID based on the href attribute
    var target = $(this).attr('href');

    console.log('Clicked tab:', target); // Add this line to check which tab is clicked

    // Hide all tab content
    $('.tab-content > div').hide();

    // Show the selected tab content
    $(target).show();

    // Remove active class from all tabs
    $('.tab-group li').removeClass('active');

    // Add active class to the clicked tab
    $(this).parent().addClass('active');
  });
});
