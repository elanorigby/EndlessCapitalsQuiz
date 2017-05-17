import randomcolor
from flask import Flask, render_template
from logic import Quiz


def get_color(lum):
    rand_color = randomcolor.RandomColor()
    return str(rand_color.generate(luminosity=lum)[0])


def make_quiz(kind):
    quiz = Quiz(kind)
    title = quiz.kind.capitalize()
    question = quiz.question
    ans = quiz.ans
    hint = quiz.hint
    bkcolor = get_color('light')
    return {'title': title, 'question': question, 'ans': ans, 'hint': hint, 'bkcolor': bkcolor}


app = Flask(__name__)


@app.route("/")
def index():
    title = "Quiz"
    return render_template('index.html', title=title)


@app.route("/capitals", methods=["GET", "POST"])
def capitals():
    kwargs = make_quiz('capitals')
    return render_template('quiz.html', **kwargs)


@app.route("/countries", methods=["GET", "POST"])
def countries():
    kwargs = make_quiz('countries')
    return render_template('quiz.html', **kwargs)


@app.route("/random", methods=["GET", "POST"])
def random():
    kwargs = make_quiz('random')
    return render_template('quiz.html', **kwargs)


if __name__ == "__main__":
    app.run()
