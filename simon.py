# let's go through the quickstart doc for Flask

from flask import Flask

app = Flask(__name__)


@app.route("/")
def my_cat():
    return "<p>My cat is called Simon!</p>"
