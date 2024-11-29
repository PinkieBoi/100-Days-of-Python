import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        blog=blog
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def read_post(post_id):
    chosen_post = None
    for post in blog:
        if int(post['id']) == post_id:
            chosen_post = post
    return render_template(
        "post.html",
        post=chosen_post
    )


blog = requests.get(url="https://api.npoint.io/132984e41bc7143377f0").json()


if __name__ == "__main__":
    app.run(debug=True)
