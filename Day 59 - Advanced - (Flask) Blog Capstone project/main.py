from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    all_posts = [Post(info) for info in requests.get(url='https://api.npoint.io/e42b353ee387383898c7').json()]
    return render_template('index.html', page='home', posts=all_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    all_posts = [Post(info) for info in requests.get(url='https://api.npoint.io/e42b353ee387383898c7').json()]
    the_post = [post for post in all_posts if post.id == post_id][0]
    return render_template('post.html', page='home', post=the_post)

@app.route('/about')
def about():
    return render_template('about.html', page='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')

if __name__ == '__main__':
    app.run(debug=True)
