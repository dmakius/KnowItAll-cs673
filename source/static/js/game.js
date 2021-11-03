//Define all game Variables
//For some reason if I don't initialize these variables it seems like the AJAX request doesn't happen fast enough and the variables don't display right initially
// count how many attempt used
var attempt_counter = 3
// total number of questions
var max_questions = 70
// time for each question
var timer = 30
// for skip question function
var MaxSkip = 3
// for player score
var player_score = 0


$(document).ready(function () {
    //get initial game data via ajax request similar to get question data - This also resets the game data to the default state
    $.ajax({
        dataType: 'json',
        type: 'GET',
        url: '/game/settings',
        success: function (data) {
            // Log data on front end
            console.log(typeof data);
            console.log(data);
            
        //initialize the variables from the ajax data
        attempt_counter = data[0]['Lives']
        MaxSkip = data[3]['Number Question Skips']
        timer = data[1]['Question Time']
        player_score = data[2]['Score']
        max_questions = data[4]['numberQuestions']
        }
    });

    //read and keep answer location
    var answer_location;
    //read and keep user selection
    var user_selection = [];
    
    
    // for skip question function
    var skipnum = 0
    var skipleft = MaxSkip
    
    // for timer function and score function
    var timeleft = timer;
    var timerpower = true; //determines whether timer is active or not

    // to automatically generate a new array [1,2,3, ... ,MaxQuestions]
    var arr = Array.from({
        length: 70 //This should be MaxQuestions
    }, (_, i) => i + 1);

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

    // Initiate the first question upon game start
    DisplayNewQuestion();
    

    // Initiate the display of the userlives
    $(".stats").show();
    UpdateLives();

    // Skip question function
    $('#SkipQuestion').click(function(){
        if (skipnum >= MaxSkip){
            console.log('No more skips!');
            return false;
        }
        skipnum += 1
        skipleft = MaxSkip - skipnum;
        document.querySelector('#SkipQuestion').textContent = 'Skip Question (' + skipleft + ')';
        console.log('Skipped!');
        DisplayNewQuestion();
        if (skipnum >= MaxSkip){
           document.getElementById('SkipQuestion').disabled = true;
        };
    });

    // Timer
    var Timer = setInterval(function () {
        if (timerpower == true) {

            if (timeleft < 0) {

                document.getElementById("Timer").innerHTML = "Finished";
                alert("Timeout!");
                user_selection[0] = 5;
                Submit()
                timeleft = timer;

            } else {
                document.getElementById("Timer").innerHTML = timeleft + " seconds remaining";
            }
            timeleft -= 1;
        }
    }, 1000);



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

    // All of the functionality attached to the player clicking the 'Submit' button
    function Submit() {
        // check user selection is empty or not
        if (user_selection[0] == undefined) {

            alert("Please select an option!");


        } else {
            // turn off the selected option color change function,
            // when user submit their answer, selected option no longer available to change color
            opt.off('click', ChangeSelectedOptionColor);

            //pause the timer
            timerpower = false;

            //turn off the skip question button after question submission
            if (skipnum < MaxSkip){
                document.getElementById('SkipQuestion').disabled = true;
                document.querySelector('#SkipQuestion').textContent = 'Skip Question (' + skipleft + ')';
            };

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


                // Update the player score as a function of the time left.
                player_score = player_score + Math.round((100) * ((timeleft+1)/timer) );
                $('#Counter').html(player_score);

            } else {
                // change user_selection color to red, and answer to green
                $(user_selection).css('color', 'red');
                $(CheckAnswer()).css('background-color', 'green').css('color', 'white');

                //Remove one of the remaining lives and update the lives display
                attempt_counter--;
                UpdateLives();
            }

            // When no more attempts are left run through the end of game logic
            if (attempt_counter <= 0) {
                //Alert the player the game is over
                alert("Game over!");
                $('#Score').val(player_score);
                $('#next').detach();
                $('#submit').detach();
                $('input[name="score"]').val(player_score);
                $('#cover-caption').slideToggle("slow");
                $('#main-container').hide();
                $('#optionboard').hide();
                $('#quit').hide();
                $('#SkipQuestion').hide();
            }
        }
    }

    // All of the functionality attached to the player clicking the 'Next Question' button
    function DisplayNewQuestion() {
        // turn on the color change function for selected option
        opt.on('click', ChangeSelectedOptionColor);

        // show submit button, new question, user can do submit
        sub.show();

        // turn off and hide next button, user cannot go next before submit
        next.hide();

        // turn on and reset the timer
        timerpower = true;
        timeleft = timer;

        // enable the skip question button if skips remain
        if (skipnum < MaxSkip){
            document.getElementById('SkipQuestion').disabled = false;

        };

        // set all option colors back to default
        opt.css('color', 'black');
        opt.css('background-color', 'white').css('color', 'black');

        // refresh user selection to an empty list
        user_selection = [];

        // no duplicated questions, every question will be show once
        if (arr.length > 0) {
            // create a random id number by the lenght of arr
            var q_id = Math.floor(Math.random() * arr.length);
            // delete the same id number of question from arr, and pass the number to index variable
            index = arr.splice(q_id, 1)[0];
        } else {
            // when arr.length = 0, means all questions has been showed once
            alert("Congratulation! You finished all the questions! Let's start from the beginning!");

            //Reinitiate the question array and continue as usual
            arr = Array.from({
                length: 70
            }, (_, i) => i + 1);
            // create a random id number by the lenght of arr
            var q_id = Math.floor(Math.random() * arr.length);
            // delete the same id number of question from arr, and pass the number to index variable
            index = arr.splice(q_id, 1)[0];
        }
        // pass the values of index to the test_int as the next question id
        var test_int = index;

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
    function UpdateLives() {
        $(".stats").html('<h4>' + 'LIVES: <span style="color:red"> ' + attempt_counter + '/3' + '</span></h4>');
    }
});