// share.js

document.getElementById('shareButton').addEventListener('click', function() {
    var barberId = this.getAttribute('data-barber-id');

    if (barberId) {
        var shareUrl = `http://127.0.0.1:8000/cl/appointment/${encodeURIComponent(barberId)}`;

        if (navigator.share) {
            navigator.share({
                title: document.title,
                url: shareUrl
            });
        } else {
            alert("Sharing is not supported in this browser.");
        }
    } else {
        alert("Barber ID is not available.");
    }
});