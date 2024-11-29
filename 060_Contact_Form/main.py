import os
import smtplib
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
EMAIL = os.environ['GOOGLE_EMAIL']
PASSCODE = os.environ['GOOGLE_APP_PASS']
TO_ADDR = os.environ['TARGET_EMAIL']

app = Flask(__name__)


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(user=EMAIL, password=PASSCODE)
        server.sendmail(
            from_addr=EMAIL,
            to_addrs=TO_ADDR,
            msg=message
        )


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
    return render_template(
        "contact.html",
    )


@app.route("/contact-success", methods=["POST"])
def contact_success():
    msg = (f"Subject:Contact Form\n\nFrom: {request.form['name']}\nEmail: {request.form['email']}\n"
           f"Tel. No.: {request.form['phone']}\nMessage: {request.form['message']}")
    send_email(msg)
    return render_template("contact-success.html")


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
