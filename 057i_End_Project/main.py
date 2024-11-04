import requests
from post import Post
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "index.html",
        blog=blog
    )


@app.route("/<int:post_id>")
def blog_post(post_id):
    return render_template(
        "post.html",
        post=blog_posts.posts[post_id]
    )


blog = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
blog_posts = Post(blog)

if __name__ == "__main__":
    app.run(debug=True)
