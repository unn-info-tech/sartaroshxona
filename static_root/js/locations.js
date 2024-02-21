$(document).ready(function () {
    $("#id_country").change(function () {
        const url = $("#personForm").data("regions-url");
        const countryId = $(this).val();

        $.ajax({
            url: url,
            data: {
                'country_id': countryId
            },
            success: function (data) {
                $("#id_region").html(data);
            }
        });
    });

    $("#id_region").change(function () {
        const url = $("#personForm").data("districts-url");
        const regionId = $(this).val();

        $.ajax({
            url: url,
            data: {
                'region_id': regionId
            },
            success: function (data) {
                $("#id_district").html(data);
            }
        });
    });

    $("#id_district").change(function () {
        const url = $("#personForm").data("cities-url");
        const districtId = $(this).val();

        $.ajax({
            url: url,
            data: {
                'district_id': districtId
            },
            success: function (data) {
                $("#id_city").html(data);
            }
        });
    });
});
