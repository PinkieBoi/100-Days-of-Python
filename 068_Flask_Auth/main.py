from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template(
        "index.html",
        logged_in=not login_manager.anonymous_user
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        with app.app_context():
            new_user = User(
                name=request.form.get('name').title(),
                email=request.form.get('email'),
                password=generate_password_hash(request.form.get('password'), salt_length=16)
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Registration Successful.')
            return redirect(url_for('secrets'))
    return render_template(
        "register.html",
        logged_in=not login_manager.anonymous_user
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with app.app_context():
            user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
            if user and check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Email or password incorrect.')
                return redirect(url_for('login'))
    return render_template(
        "login.html",
        logged_in=not login_manager.anonymous_user
    )


@app.route('/secrets')
@login_required
def secrets():
    user = db.session.execute(db.select(User).where(User.id == current_user.id)).scalar()
    return render_template(
        "secrets.html",
        user=user,
        logged_in=True
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        'static',
        'files/cheat_sheet.pdf'
    )


if __name__ == "__main__":
    app.run(debug=True)
