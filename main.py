import flask


def func_add(a: int, b: int) -> int:
    return a + b


app = flask.Flask(__name__)


@app.route("/")
def index():
    return "<h1 style='color:blue'>Coucou !</h1>"


@app.route("/pouet")
def pouet():
    return "Pouet !"
