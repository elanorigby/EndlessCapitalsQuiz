$(function() {
    var ENTER_KEY = 13;
    var answeredCorrectly = false;

    $('#user_answer').keypress(function(e) {
        if (e.which === ENTER_KEY) {
            e.preventDefault();

           // if they got it right pressing enter reload page, getting a new question
            if (answeredCorrectly) {
                location.reload();
                return;
            }

           // set up user answer and correct answer
            var user_answer = $('#user_answer').val();
            var correct_answer = $('#correct_answer').val();

           // if no input, do not check answer or reload page
            if (! user_answer) {
                return;
            }

           // check answer, give feedback
            if (user_answer.toLowerCase() === correct_answer.toLowerCase()) {
                $('#feedback').text("Yessss!!!!!");
                answeredCorrectly = true;

            } else {
                $('#feedback').text("Nope.");
                $('#user_answer').val('');
            }
        }
    });
});
