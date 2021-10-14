$(document).ready(function () {

    //keep options
    var option1;
    var option2;
    var option3;
    var option4;
    //keep answer location
    var answer_location;
    //keep user selection
    var user_selection;
    // count how many attempt used
    var attempt_counter = 0;

    //Make Add score to Leader board form appear

    $('#submitScore').click(function () {
        console.log('clicked!');
        $('#cover-caption').slideToggle("slow");
    });

    // clicking on any of the options and buttons
    $('.option').click(function () {
        //var clicked = $(this).attr("clicked");
        //get user selection
        user_selection = $(this);
        console.log('clicked!');
        //TODO: subtract lives if neccesary
        //TODO: Assign points
    });
    //Display new question
    $('#next').on('click', DisplayNewQuestion);
    //Check if selection is correct
    $('#submit').on('click', Submit);
    //------------------------------------
    //SELECT A NEW RANDOM QUESTION
    //TODO: Replace max number with number of questions come backend
    function DisplayNewQuestion() {

        // replace the changed color back.
        $(Answer()).css('color', 'black')
        $(user_selection).css('color', 'black')
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
                option1 = data[2]['Answer'];
                $('#option_2').text("B: " + data[3]['Option_1']);
                option2 = data[3]['Option_1'];
                $('#option_3').text("C: " + data[4]['Option_2']);
                option3 = data[4]['Option_2'];
                $('#option_4').text("D: " + data[5]['Option_3']);
                option4 = data[5]['Option_3'];
                answer_location = data[6]['Answer_Location'];
            }
        });
    }

    //function UserSelect(){
    //    user_selection = this.id
    //    return user_selection
    //}

    // function for submit button and check attempts
    function Submit() {

        if (user_selection == Answer()) {
            // change answer color to green
            $(Answer()).css('color', 'green');
            // score function people can add their score++ in this if function
        } else {
            // change user_selection color to red, and answer to green
            $(user_selection).css('color', 'red');
            $(Answer()).css('color', 'green');

            // attempt counter count one chance
            attempt_counter++;
            // score function people can add their score-- in here.
        }

        // when 3 attempts, game over, goes to the leader board.
        if (attempt_counter >= 3) {
            alert("GameOver!" + "Score shows up here");
            $('#next').detach();
            $('#submit').detach();
        }
    }

    // function for checking which option is the answer
    function Answer() {
        if (answer_location == 1) {
            q_answer = option_1;
        } else if (answer_location == 2) {
            q_answer = option_2;
        } else if (answer_location == 3) {
            q_answer = option_3;
        } else {
            q_answer = option_4;
        }
        console.log(q_answer);
        return q_answer;
    }
});
