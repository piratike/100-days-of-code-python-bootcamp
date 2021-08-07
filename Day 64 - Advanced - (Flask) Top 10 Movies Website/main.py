from enum import unique
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = 'd3b838c838b9d021fe5a37322496df96'
TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie/'
TMDB_FIND_URL = 'https://api.themoviedb.org/3/movie/'
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500/'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}'


class RateMovieForm(FlaskForm):
    movie_rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    movie_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


db.create_all()


@app.route('/')
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template('index.html', movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    movie_form = RateMovieForm()
    if movie_form.validate_on_submit():
        movie_to_update = Movie.query.get(request.args.get('movie_id'))
        movie_to_update.rating = movie_form.movie_rating.data
        movie_to_update.review = movie_form.movie_review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', form=movie_form)


@app.route('/delete')
def delete():
    movie_to_delete = Movie.query.get(request.args.get('movie_id'))
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_form = AddMovieForm()
    if movie_form.validate_on_submit():
        movie_title = movie_form.movie_title.data
        response = requests.get(TMDB_SEARCH_URL, params={'api_key': TMDB_API_KEY, 'query': movie_title})
        data = response.json()['results']
        return render_template('select.html', options=data)

    return render_template('add.html', form=movie_form)


@app.route('/find', methods=['GET'])
def find():
    response = requests.get(TMDB_FIND_URL + request.args.get('movie_id'), params={'api_key': TMDB_API_KEY}).json()
    poster_path = response['poster_path']
    new_movie = Movie(
        title = response['title'],
        year = response['release_date'].split('-')[0],
        description = response['overview'],
        img_url = f'{TMDB_IMAGE_URL}{poster_path}'
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
