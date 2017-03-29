import randomcolor
from flask import Flask, render_template
from random import choice
from logic import CapitalsQuiz, CountriesQuiz

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
    title = quiz.name
    correct_answer = quiz.correct_answer
    hint = quiz.hint
    question = "What is the capital of {}?".format(hint)

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint,
                           bkcolor=bkcolor)


@app.route("/countries", methods=["GET", "POST"])
def countries():
    quiz = CountriesQuiz()
    bkcolor = get_color('light')
    title = quiz.name
    correct_answer = quiz.correct_answer
    hint = quiz.hint
    question = "{} is the capital of what country?".format(hint)

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint,
                           bkcolor=bkcolor)


@app.route("/random", methods=["GET", "POST"])
def random():
    random_quiz = choice([CapitalsQuiz, CountriesQuiz])
    quiz = random_quiz()
    bkcolor = get_color('light')
    title = quiz.name
    correct_answer = quiz.correct_answer
    hint = quiz.hint

    if random_quiz == CapitalsQuiz:
        question = "What is the capital of {}?".format(hint)
    elif random_quiz == CountriesQuiz:
        question = "{} is the capital of what country?".format(hint)
    else:
        raise TypeError

    return render_template('quiz.html', title=title, question=question, correct_answer=correct_answer, hint=hint,
                           bkcolor=bkcolor)


if __name__ == "__main__":
    app.run()
