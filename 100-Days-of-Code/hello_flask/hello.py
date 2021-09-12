from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def w():
        return f"<b>{func()}</b>"
    return w


def make_emphasis(func):
    def w():
        return f"<em>{func()}</em>"
    return w


def make_underlined(func):
    def w():
        return f"<u>{func()}</u>"
    return w


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}! You are {number} person!"


if __name__ == "__main__":
    app.run(debug=True)
