from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


## Delete this code:
# import requests
# posts = requests.get('https://api.npoint.io/43644ec4f0013682fc0d').json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = BlogPost.query.get(index)
    return render_template('post.html', post=requested_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title = post_form.title.data,
            subtitle = post_form.subtitle.data,
            body = post_form.body.data,
            img_url = post_form.img_url.data,
            author = post_form.author.data,
            date = date.today().strftime("%B %d, %Y")
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=post_form, is_edit=False)


@app.route('/edit-post/<int:index>', methods=['GET', 'POST'])
def edit_post(index):
    post = BlogPost.query.get(index)
    post_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if post_form.validate_on_submit():
        post.title = post_form.title.data,
        post.subtitle = post_form.subtitle.data,
        post.body = post_form.body.data,
        post.img_url = post_form.img_url.data,
        post.author = post_form.author.data,

        db.session.commit()

        return redirect(url_for('show_post', post_id=post.id))

    return render_template('make-post.html', form=post_form, is_edit=True)


if __name__ == '__main__':
    app.run()