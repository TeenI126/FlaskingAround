# let's go through the quickstart doc for Flask

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def my_cat():
    return "<p>My cat is called Simon!</p>"

@app.route("/escape/<name>")
def using_escape(name):
    return f"my cat is named {escape(name)}"