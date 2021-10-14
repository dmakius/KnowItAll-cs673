$(document).ready(function () {

    var counter = 0;
    var correctCount = 0;
    var answer = $('#option_1').text();
    var answerLocation = null;

    var timer = 30; // Timer (Seconds)
    var timeleft = timer;

    var max_number = 50;
    //TODO: Bugfix: sometime test_int will return a specific number, which occur a error that not forward to the next question.



    // Initialize the firstQuestion
    //  Comment: Each Time the First question would put the answer in the first option, it does not follow the rule, because the function only available after you click. (You need to initialize the first question as well)
    pickQuestion();

    // Timer
    var Timer = setInterval(function () {
        if (timeleft < 0) {

            document.getElementById("Timer").innerHTML = "Finished";
            alert("Timeout!");
            pickQuestion()
            timeleft = timer;

        } else {
            document.getElementById("Timer").innerHTML = timeleft + " seconds remaining";
        }
        timeleft -= 1;

    }, 1000);


    // clicking on any of the options
    $('.option').click(function () {
        //TODO: Check if selection is correct
        //TODO: subtract lives if neccesary
        //TODO: Assign points

        //------------------------------------
        //SELECT A NEW RANDOM QUESTION
        //TODO: Replace max number with number of questions come backend

        var max_number = 50;

        //TODO: sometime test_int will return a specific number, which occur a error that not forward to the next question.
        /* Reference:
                jquery.min.js:2 GET http://127.0.0.1:5000/question/0 500 (INTERNAL SERVER ERROR)
                send @ jquery.min.js:2
                ajax @ jquery.min.js:2
                (anonymous) @ game.js:49
                dispatch @ jquery.min.js:2
                v.handle @ jquery.min.js:2
        */
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

                answerLocation = data[6]['Answer_Location']
                console.log("answer Location is : " + answerLocation);
                answer = $('#option_' + answerLocation).text();
                console.log("answer is : " + answer);

            }
        });

        // Check the selected answer if is the correct answer
        if (this.id == "option_" + answerLocation) {
            alert("TRUE")
            timeleft = timer;
            correctCount = correctCount + 1
        } else {
            timeleft = timer;
            alert("FALSE")
        }


        /* console.log(correctCount + "/" + counter); */
        counter = counter + 1;
        $('#Counter').html(correctCount + "/" + counter);
    });

});

function pickQuestion() {
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

            answerLocation = data[6]['Answer_Location']
            console.log("answer Location is : " + answerLocation);
            answer = $('#option_' + answerLocation).text();
            console.log("answer is : " + answer);
        }
    });
}