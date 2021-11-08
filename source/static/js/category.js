$(document).ready(function () {
    var selected = [];
    var select = $('.category');
    select.on('click', Select);
    function Select() {
        selected = $(this);
    }

    $.ajax({
        dataType: 'json',
        // type: 'GET',
        type: 'POST',
        url: '/category/select',
        data: {
            "select_category": selected
        }
    });

});
