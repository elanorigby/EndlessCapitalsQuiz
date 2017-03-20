from flask import Flask, render_template, request

from logic import CapitalsQuiz, CountriesQuiz, RandomQuiz


app = Flask(__name__)


@app.route("/")
def index():
    title = "Endless Capitals Quiz"
    return render_template('index.html', title=title)


@app.route("/capitals", methods=['GET', 'POST'])
def capitals():
    title = "Endless Capitals Quiz"
    quiz = CapitalsQuiz()
    correct_ans = quiz.correct_answer
    hint = quiz.hint
    question = "What is the capital of {}?".format(hint)

    #
    # user_answer = request.form.user_answer.strip().lower()
    # if quiz.is_right(user_answer):
    #     feedback = "Yes! {} is the capital of {}".format(correct_ans, hint)
    # else:
    #     feedback = "Nope. Try Again."

    # tell = request.form.tell
    # if tell:

    # correct_ans=correct_ans, hint=hint, feedback=feedback,

    return render_template('quiz.html', title=title, question=question, correct_ans=correct_ans, hint=hint)

#
#
# @app.route("/countries")
# def countries():
#     return render_template('countries.html')  # pass variables
#
#
# @app.route("/random")
# def random():
#     return render_template('random.html')  # pass variables
#
#
if __name__ == "__main__":
    app.run()
