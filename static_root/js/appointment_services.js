$(document).ready(function () {
    $(".selectable").on("click", function () {
        $(this).toggleClass("selected");
        calculateTotal();
    });

    function calculateTotal() {
        let totalDuration = 0;
        let totalPrice = 0;

        $(".selected-list").empty();
        $(".service-item.selected").each(function () {
            const duration = parseInt($(this).data("duration"));
            const price = parseInt($(this).data("price"));
            totalDuration += duration;
            totalPrice += price;
            $(".selected-list").append(`<li>${$(this).text()}</li>`);
        });

        $("#total-duration").text(totalDuration);
        $("#total-price").text(totalPrice);
    }
});
