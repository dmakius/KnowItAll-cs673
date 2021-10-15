// variables
var arr = Array.from({length: 50}, (_, i) => i+1);
var result = [];

$(document).ready(function () {
    //Make Add score to Leader board form appear

    $('#submitScore').click(function(){
        console.log('clicked!');
        $('#cover-caption').slideToggle("slow");
    });

    // clicking on any of the options
    $('.option').click(function () {
        //TODO: Check if selection is correct
        //TODO: subtract lives if neccesary
        //TODO: Assign points

        //------------------------------------
        //SELECT A NEW RANDOM QUESTION
        //TODO: Replace max number with number of questions come backend

        // no duplicated questions, every question will be show once
        if (arr.length > 0) {
            var ran = Math.floor(Math.random() * arr.length);
            // delete id number of question from arr
            index = arr.splice(ran,1)[0];
            // push the id number of question to the result array list
            result.push(index);
        } else {
            alert("Congratulation! You finished all the questions! ");
        }
        var test_int = index;

        // var max_number = 50;
        // var test_int = Math.floor(Math.random() * max_number);
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

window.addEventListener("DOMContentLoaded", event => {
    document.getElementById("startgame").addEventListener("click", event => {
        document.getElementById("startgame").style.display = "none";
        document.querySelector(".jumbotron.well").style.display = "block";
        display_all_options();
    });
});

function display_all_options() {
    var selector, i;
    selector = document.querySelectorAll(".row.answers");
    for (i = 0; i < selector.length; i++) {
        selector[i].style.display = "flex";
    }
}

