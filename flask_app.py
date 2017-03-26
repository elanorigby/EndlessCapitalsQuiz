from flask import Flask, render_template
from random import choice
from logic import CapitalsQuiz, CountriesQuiz, RandomQuiz


app = Flask(__name__)


@app.route("/")
def index():
    title = "Capitals"
    return render_template('index.html', title=title)


@app.route("/capitals", methods=["GET", "POST"])
def capitals():
    quiz = CapitalsQuiz()

    title = "Capitals"
    correct_answer = quiz.correct_answer
    hint = quiz.hint
    question = "What is the capital of {}?".format(hint)

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint)


@app.route("/countries", methods=["GET", "POST"])
def countries():
    quiz = CountriesQuiz()

    title = "Countries"
    correct_answer = quiz.correct_answer
    hint = quiz.hint
    question = "{} is the capital of what country?".format(hint)

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint)

# @app.route("/random", methods=["GET", "POST"])
# def random():
#     random_quiz = random.choice(countries, capitals)
#     random_quiz()


if __name__ == "__main__":
    app.run()
