from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', current_year=datetime.now().year, author='MRosa')

@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(url=f'https://api.genderize.io?name={name}').json()['gender']
    age = requests.get(url=f'https://api.agify.io?name={name}').json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    all_posts = requests.get(url='https://api.npoint.io/ed99320662742443cc5b').json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
