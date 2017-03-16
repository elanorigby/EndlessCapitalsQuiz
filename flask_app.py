# needs

# title text
# input field
# choice buttons
# display question area
# display feedback area
# stop please button

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/capitals")
def hello():
    return "Hello World!"


@app.route("/countries")
def hello():
    return "Hello World!"


@app.route("/random")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()