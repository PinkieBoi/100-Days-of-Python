from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold_text():
        return f"<strong>{function()}</strong>"
    return bold_text


def make_emphasis(function):
    def italic_text():
        return f"<em>{function()}</em>"
    return italic_text


def make_underline(function):
    def underline_text():
        return f"<u>{function()}</u>"
    return underline_text


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
