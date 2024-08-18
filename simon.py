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
        return f'hello {request.form.get("name")} with cat {request.form.get("cat")}'
    else:
        return HTTPMaker().add_par("ello").add_form(url_for("login"), {"name":"string", "cat": "simon"}).get_http()


class HTTPMaker:
    text = ""

    def add_par(self, text: str):
        self.text += f"<p>{text}</p>\n"
        return self

    def make_url(self, url: str, display: str) -> str:
        return f'<a href=\"{url}\">{display}</a>'

    def get_function_url(self, func_name: str, **kwargs) -> str:
        return url_for(func_name, **kwargs)  # interested tangent on arbitrary keyword args

    def get_http(self) -> str:
        return self.text

    def add_form(self, url:str,inputs:dict):
        questions = ""
        for quest, type in inputs.items():
            questions += f'<label for"{quest}">{quest}</label>\n' \
                         f'<input type="{type}" id="{quest}" name="{quest}">\n'
        questions += f'<button type="submit">Submit</button>\n'

        to_return = f'<form action="{url}" method="POST">\n' \
                    f'{questions}\n' \
                    f'</form>\n'
        print(to_return)
        self.text += to_return
        return self
