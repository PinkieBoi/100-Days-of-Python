import os
import requests
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, SubmitField, IntegerField, FloatField

load_dotenv()
api_token = os.environ['TMDB_API_READ_TOKEN']
api_key = os.environ['TMDB_API_KEY']

tmdb_url = "https://api.themoviedb.org/3/search/movie"
tmdb_headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_token}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_films.db"
Bootstrap5(app)


class FilmSearch(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search')


class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating (out of 10)')
    review = StringField("Your Review")
    submit = SubmitField("Done")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class FilmDB(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    submit = SubmitField('Add Film')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        all_films = [film for film in db.session.execute(db.select(FilmDB).order_by(FilmDB.rating.desc())).scalars()]
        return render_template(
            "index.html",
            films=all_films
        )


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = FilmSearch()
    if request.method == 'POST':
        response = requests.get(
            url=tmdb_url,
            headers=tmdb_headers,
            params={
                "query": form.title.data,
            }
        ).json()['results']
        return render_template(
            "select.html",
            films=response
        )
    return render_template(
        "add.html",
        form=form
    )


@app.route("/update", methods=['GET', 'POST'])
def update_db():
    film_id = request.args.get('id')
    form = RateMovieForm()
    with app.app_context():
        edit_entry = db.session.execute(db.select(FilmDB).where(FilmDB.id == film_id)).scalar()
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            edit_entry.rating = form.rating.data
            edit_entry.review = form.review.data
            db.session.add(edit_entry)
            db.session.commit()
        return redirect('/')
    return render_template(
        "edit.html",
        movie=edit_entry,
        form=form
    )


@app.route("/save", methods=['GET', 'POST'])
def save_selection():
    form = RateMovieForm()
    response = requests.get(
        url=tmdb_url,
        headers=tmdb_headers,
        params={
            "query": request.args.get('title'),
            "id": request.args.get('id')
        }
    ).json()['results'][0]
    if request.method == 'POST':
        new_film = FilmDB(
            title=response['original_title'],
            release_date=response['release_date'].split("-")[0],
            description=response['overview'],
            rating=form.rating.data,
            review=form.review.data,
            img_url="https://image.tmdb.org/t/p/original" + response['poster_path']
        )
        db.session.add(new_film)
        db.session.commit()
        return redirect('/')
    return render_template(
        "edit.html",
        form=form,
        movie=response,
    )


@app.route("/delete")
def delete_entry():
    with app.app_context():
        rmfilm = db.session.execute(db.select(FilmDB).where(FilmDB.id == request.args.get('id'))).scalar()
        db.session.delete(rmfilm)
        db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
