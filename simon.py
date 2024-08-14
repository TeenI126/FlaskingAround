# let's go through the quickstart doc for Flask

from markupsafe import escape
from flask import *

app = Flask(__name__)


@app.route("/")
def my_cat():
    http = HTTPMaker()
    http.add_par("I have a cat named simon")
    http.add_par(f"login here -> {http.make_url(http.get_function_url('login'),'login')}")
    return http.get_http()


@app.route("/likes/<name>")
def using_vars(name):
    return f"He likes {escape(name)}"


# Http methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "hello"
    else:
        return "hi"


class HTTPMaker:
    text = ""

    def add_par(self, text: str):
        self.text += f"<p>{text}</p>\n"

    def make_url(self, url: str, display: str) -> str:
        return f'<a href=\"{url}\">{display}</a>'

    def get_function_url(self, func_name: str, **kwargs) -> str:
        return url_for(func_name, **kwargs)  # interested tangent on arbitrary keyword args

    def get_http(self) -> str:
        return self.text
