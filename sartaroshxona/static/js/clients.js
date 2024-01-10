function toggleHeader() {
    var header = document.getElementById('header');
    var icon = document.getElementById('icon');

    if (header.style.display === 'none') {
        header.style.display = 'block';
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    } else {
        header.style.display = 'none';
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    }

    
}
