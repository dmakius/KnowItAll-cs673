$(document).ready(function () {

    // clicking on any of the options
    $('.option').click(function () {
        //TODO: Check if selection is correct
        //TODO: subtract lives if neccesary
        //TODO: Assign points

        //------------------------------------
        //SELECT A NEW RANDOM QUESTION
        //TODO: Replace max number with number of questions come backend
        var max_number = 50;
        var test_int = Math.floor(Math.random() * max_number);
        $.ajax({
            dataType: 'json',
            type: 'GET',
            url: '/question/' + test_int,
            success: function (data) {
                // Log data on front end
                console.log(typeof data);
                console.log(data);

                //replace front end ui with NEW data from server
                $('#question').text(data[1]['Question']);
                $('#option_1').text("A: " + data[2]['Answer']);
                $('#option_2').text("B: " + data[3]['Option_1']);
                $('#option_3').text("C: " + data[4]['Option_2']);
                $('#option_4').text("D: " + data[5]['Option_3']);
            }
        });

    });
});
