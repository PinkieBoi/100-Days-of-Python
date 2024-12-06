from datetime import date
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


ckeditor = CKEditor()
ckeditor.init_app(app)
days = []


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Article', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def get_all_posts():
    posts = [post for post in db.session.execute(db.select(BlogPost)).scalars()]
    return render_template(
        "index.html",
        all_posts=posts
    )


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template(
        "post.html",
        post=requested_post
    )


# TODO: add_new_post() to create a new blog post
@app.route('/add_post', methods=['GET', 'POST'])
def add_new_post():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                date=date.today().strftime('%B %_d, %Y'),
                author=form.author.data,
                img_url=form.img_url.data
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template(
        "make-post.html",
        form=form,
        page_type="New Post"
    )


# TODO: edit_post() to change an existing blog post
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            post_to_edit.title = form.title.data
            post_to_edit.subtitle = form.subtitle.data
            post_to_edit.author = form.author.data
            post_to_edit.img_url = form.img_url.data
            post_to_edit.body = form.body.data
            post_to_edit.date = date.today().strftime('%B %_d, %Y')
            db.session.add(post_to_edit)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
    form.title.data = post_to_edit.title
    form.subtitle.data = post_to_edit.subtitle
    form.author.data = post_to_edit.author
    form.img_url.data = post_to_edit.img_url
    form.body.data = post_to_edit.body
    return render_template(
        "make-post.html",
        form=form,
        page_type="Edit Post"
    )


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    with app.app_context():
        post = db.get_or_404(BlogPost, post_id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
