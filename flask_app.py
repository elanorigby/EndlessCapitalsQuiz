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
    return title, question, ans, hint, bkcolor


app = Flask(__name__)


@app.route("/")
def index():
    title = "Quiz"
    return render_template('index.html', title=title)


@app.route("/capitals", methods=["GET", "POST"])
def capitals():
    title, question, ans, hint, bkcolor = make_quiz('capitals')
    return render_template('quiz.html', title=title, question=question, ans=ans, hint=hint, bkcolor=bkcolor)


@app.route("/countries", methods=["GET", "POST"])
def countries():
    title, question, ans, hint, bkcolor = make_quiz('countries')
    return render_template('quiz.html', title=title, question=question, ans=ans, hint=hint, bkcolor=bkcolor)


@app.route("/random", methods=["GET", "POST"])
def random():
    title, question, ans, hint, bkcolor = make_quiz('random')
    return render_template('quiz.html', title=title, question=question, ans=ans, hint=hint, bkcolor=bkcolor)

if __name__ == "__main__":
    app.run()
