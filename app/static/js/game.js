$(document).ready(function () {

    // read and keep options here
    var option1;
    var option2;
    var option3;
    var option4;
    //read and keep answer location
    var answer_location;
    //read and keep user selection
    var user_selection = [];
    // count how many attempt used
    var attempt_counter = 3;

    //---------------------------------
    //CLICK/BUTTON
    //Make Add score to Leader board form appear
    $('#submitScore').click(function () {
        console.log('clicked!');
        $('#cover-caption').slideToggle("slow");
    });
    $('#submitScore').hide()


    var opt = $('.option');
    // clicking on any of the options will return value to user_selection
    opt.on('click', Selection);
    // click option will change the option background color
    opt.on('click', ChangeSelectedOptionColor);

    //Submit button, Check if selection is correct
    var sub = $('#submit');
    sub.on('click', Submit);

    //Next button, for new question
    var next = $('#next');
    next.on('click', DisplayNewQuestion);
    //Hide next button before click submit
    next.hide();
    //------------------------------------------------


    //------------------------------------------------
    //FUNCTION

    // Load random question when load the page
    DisplayNewQuestion();

    //Display remaining lives
    $(".stats").show();
    DisplayStats();

    //TODO: Assign points

    //get user selection when player click the option
    function Selection() {
        user_selection = $(this);
        console.log(user_selection[0] + 'clicked!');
    }

    // change the player selected option's color
    function ChangeSelectedOptionColor() {
        opt.css('background-color', 'white').css('color', 'black');
        $(user_selection).css('background-color', 'grey').css('color', 'white');
    }

    //TODO: subtract lives if neccesary

    //------------------------------------
    //SELECT A NEW RANDOM QUESTION
    //TODO: Replace max number with number of questions come backend
    function DisplayNewQuestion() {
        // turn on the color change function for selected option
        opt.on('click', ChangeSelectedOptionColor);

        // show submit button, new question, user can do submit
        sub.show();

        // turn off and hide next button, user cannot go next before submit
        next.hide();

        // replace the changed color back, and background color back.
        opt.css('color', 'black');
        opt.css('background-color', 'white').css('color', 'black');

        // refresh user selection to an empty list
        user_selection = [];

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
                option1 = $('#option_1').text("A: " + data[2]['Option_1']);
                option2 = $('#option_2').text("B: " + data[3]['Option_2']);
                option3 = $('#option_3').text("C: " + data[4]['Option_3']);
                option4 = $('#option_4').text("D: " + data[5]['Option_4']);
                answer_location = data[6]['Answer_Location'];
            }
        });
    }

    // return answer, count attempts
    function Submit() {

        // check user selection is empty or not
        if (user_selection[0] == undefined){

            alert("Please select an option!");

        } else {
            // turn off the selected option color change function,
            // when user submit their answer, selected option no longer available to change color
            opt.off('click', ChangeSelectedOptionColor);

            // hide Submit button, user already submitted once
            sub.hide();

            // show next button
            next.show();
            // if else function for check if player answer right or wrong
            // user_selection is getting from function Selection(),
            // and user_selection is a list, value locate at [0] is a HTML<div>...</div>
            // something like this: <div class="col-md-5 text-center option btn btn-outline-secondary" id="option_2" style="color: green;">B: Baker Street</div>
            // So that we can use user_selection[0] compare with the result from function CheckAnswer()
            // to check if player selection is right or wrong
            if (user_selection[0] == CheckAnswer()) {
                // change answer color to green
                $(CheckAnswer()).css('background-color', 'green').css('color', 'white');


                // score function can be added score++ in this if function

            } else {
                // change user_selection color to red, and answer to green
                $(user_selection).css('color', 'red');
                $(CheckAnswer()).css('background-color', 'green').css('color', 'white');

                // attempt counter count one chance
                attempt_counter--;


                // score function can be added score-- in here.

            }
            DisplayStats();

            // when 3 attempts, game over, only allow to submit score.
            if (attempt_counter <= 0) {
                alert("GameOver!");
                $('#next').detach();
                $('#submit').detach();
                $('#cover-caption').slideToggle("slow");
                $('#optionboard').hide()
                $('#quit').hide()
            }
        }
    }

    // function for checking which option is the answer
    function CheckAnswer() {

        //answer_location is getting from DisplayNewQuestion(), and the value is a int
        if (answer_location == 1) {
            //option_1 is getting from DisplayNewQuestion() option_1
            q_answer = option_1;

        } else if (answer_location == 2) {
            //option_2 is getting from DisplayNewQuestion() option_2
            q_answer = option_2;

        } else if (answer_location == 3) {
            //option_3 is getting from DisplayNewQuestion() option_3
            q_answer = option_3;

        } else {
            //option_4 is getting from DisplayNewQuestion() option_4
            q_answer = option_4;
        }
        // the return value is a HTML <div>...</div>,
        // something like: <div class="col-md-5 text-center option btn btn-outline-secondary" id="option_1" style="color: green;">B: Baker Street</div>
        return q_answer;
    }
    // Display remaining lives
    function DisplayStats() {
        $(".stats").html('<h4>' + 'remaining lives: ' + attempt_counter + '/3' + '</h4>');
    }

});
