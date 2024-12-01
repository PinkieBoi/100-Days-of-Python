from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField, SelectField, SubmitField
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, request, redirect, url_for


class LibraryForm(FlaskForm):
    book_title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = SelectField(
        label='Rating',
        choices=[(1, "⭐️"), (2, "⭐️⭐️"), (3, "⭐️⭐️⭐️"), (4, "⭐️⭐️⭐️⭐️"), (5, "⭐️⭐️⭐️⭐️⭐️")],
        validators=[DataRequired()]
    )
    submit = SubmitField(label='Add Book')


class EditForm(FlaskForm):
    rating = SelectField(
        label='New Rating',
        choices=[(1, "⭐️"), (2, "⭐️⭐️"), (3, "⭐️⭐️⭐️"), (4, "⭐️⭐️⭐️⭐️"), (5, "⭐️⭐️⭐️⭐️⭐️")],
        validators=[DataRequired()]
    )
    submit = SubmitField(label='Submit')


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = "iu34u342hr139p8teioj"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favourite_books.db"
Bootstrap5(app)


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book)).scalars()
        return render_template(
            "index.html",
            library=all_books
        )


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = LibraryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            with app.app_context():
                new_book = Book(
                    title=form.book_title.data.title(),
                    author=form.author.data.title(),
                    rating=form.rating.data
                )
                db.session.add(new_book)
                db.session.commit()
            return redirect('/')
    return render_template(
        "add.html",
        form=form
    )


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    with app.app_context():
        edit_book = db.session.execute(db.select(Book).where(Book.id == request.args.get('id'))).scalar()
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            edit_book.rating = form.rating.data
            # edited_book = Book(
            #     id=request.args.get('id'),
            #     title=edit_book.title,
            #     author=edit_book.author,
            #     rating=form.rating.data
            # )
            db.session.add(edit_book)
            db.session.commit()
        return redirect('/')
    return render_template(
        "edit.html",
        library=edit_book,
        form=form
    )


@app.route("/delete")
def delete():
    with app.app_context():
        rmbook = db.session.execute(db.select(Book).where(Book.id == request.args.get('id'))).scalar()
        db.session.delete(rmbook)
        db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
