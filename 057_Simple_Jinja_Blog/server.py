import random
import requests
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    current_year = date.today().year
    random_num = random.randint(0, 9)
    return render_template(
        "index.html",
        random_num=random_num,
        current_year=current_year
    )


@app.route("/guess/<name>")
def guess(name):
    age_data = requests.get(url=f"https://api.agify.io?name={name}").json()
    gender_data = requests.get(url=f"https://api.genderize.io?name={name}").json()
    return render_template(
        "name_age.html",
        name=name.title(),
        age=age_data["age"],
        gender=gender_data["gender"]
    )


@app.route("/blog")
def blog():
    return render_template(
        "blog.html",
        all_posts=blog_data
    )


@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    return render_template(
        "post.html",
        post=all_posts[post_id]
    )


blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
all_posts = {post["id"]: post for post in blog_data}

if __name__ == "__main__":
    app.run(debug=True)
