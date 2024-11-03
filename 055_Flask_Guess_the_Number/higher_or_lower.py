import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def initial_display():
    return (f"<h1>Guess a number between 0 and 9</h1>\n"
            f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />")


@app.route("/<int:num>")
def guess_number(num):
    if num > 9 or num < 0:
        return "<h1>You had ONE job!</h1>"
    elif num < target_num:
        return f"<h1>Too Low!</h1>\n{higher_img}"
    elif num > target_num:
        return f"<h1>Too High!</h1>\n{lower_img}"
    else:
        return f"<h1>Correct, The number was {num}!</h1>\n{correct_img}"


target_num = random.randint(0, 9)
correct_img = ('<iframe src="https://giphy.com/embed/M7vffPHtFXqSI" width="480" height="319" style="" frameBorder="0" '
               'class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/M7vffPHtFXqSI">via '
               'GIPHY</a></p>')
higher_img = ('<iframe src="https://giphy.com/embed/3o6ZtaO9BZHcOjmErm" width="480" height="461" style="" '
              'frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a '
              'href="https://giphy.com/gifs/dog-puppy-fly-3o6ZtaO9BZHcOjmErm">via GIPHY</a></p>')
lower_img = ('<iframe src="https://giphy.com/embed/URoLoCo1s9jm8" width="480" height="317" style="" frameBorder="0" '
             'class="giphy-embed" allowFullScreen></iframe><p><a '
             'href="https://giphy.com/gifs/dog-puppy-URoLoCo1s9jm8">via GIPHY</a></p>')

if __name__ == "__main__":
    app.run()
