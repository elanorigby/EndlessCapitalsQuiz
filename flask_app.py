import randomcolor
from flask import Flask, render_template

from logic import CapitalsQuiz, CountriesQuiz, RandomQuiz


def get_color(lum):
    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity=lum)[0])
    return color

app = Flask(__name__)


@app.route("/")
def index():
    title = "Capitals"
    return render_template('index.html', title=title)


@app.route("/capitals", methods=["GET", "POST"])
def capitals():
    quiz = CapitalsQuiz()
    bkcolor = get_color('light')
    title = "Capitals"
    correct_answer = quiz.correct_answer
    hint = quiz.hint
    question = "What is the capital of {}?".format(hint)

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint, bkcolor=bkcolor)


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
