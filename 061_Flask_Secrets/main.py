from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "This-is-a-secreT"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if request.method == "POST" and login_form.validate():
        user = login_form.email.data
        passcode = login_form.password.data
        if user == "admin@email.com" and passcode == "12345678":
            return render_template(
                "success.html",
                user=user.split("@")[0]
            )
        else:
            return render_template("denied.html")
    return render_template(
        "login.html",
        form=login_form
    )


if __name__ == '__main__':
    app.run(debug=True)
