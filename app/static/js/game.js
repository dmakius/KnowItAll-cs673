// variables
// to automatically generate a new array [1,2,3, ... ,50]
var arr = Array.from({length: 50}, (_, i) => i+1);
// showed_id arry is to store the question id which was already showed
var showed_id = [];

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
            // create a random id number by the lenght of arr
            var q_id = Math.floor(Math.random() * arr.length);
            // delete the same id number of question from arr, and pass the number to index variable
            index = arr.splice(q_id,1)[0];
            // push the id number of question that has been deleted, to the showed_id array list
            showed_id.push(index);
        } else {
            // when arr.length = 0, means all questions has been showed once
            alert("Congratulation! You finished all the questions! ");
        }
        // pass the values of index to the test_int as the next question id
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

// to add some events when the play button is being clicked
window.addEventListener("DOMContentLoaded", event => {
    document.getElementById("startgame").addEventListener("click", event => {
        // disapper the play button
        document.getElementById("startgame").style.display = "none";
        // display the question
        document.querySelector(".jumbotron.well").style.display = "block";
        // display all options
        display_all_options();
    });
});

// go over all contents that meets the condictions with queryselector
function display_all_options() {
    var selector, i;
    selector = document.querySelectorAll(".row.answers");
    for (i = 0; i < selector.length; i++) {
        // display all the contents that meets the condictions
        selector[i].style.display = "flex";
    }
}

