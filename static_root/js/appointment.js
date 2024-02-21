// slider.js

// Assuming you have an element with the class 'uk-slider-container'
const sliderElement = document.querySelector('.uk-slider-container');

if (sliderElement) {
    UIkit.slider(sliderElement, {
        // Configuration options for the slider
        // Add your options here
    });
}


document.getElementById('heartButton').addEventListener('click', function() {
    // Toggle the 'clicked' class on the container
    document.getElementById('container').classList.toggle('clicked');
});
