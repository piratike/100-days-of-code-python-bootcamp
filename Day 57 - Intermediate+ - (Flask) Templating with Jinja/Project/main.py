from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

@app.route('/')
def home():
    all_posts = [Post(info) for info in requests.get(url='https://api.npoint.io/ed99320662742443cc5b').json()]
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    all_posts = [Post(info) for info in requests.get(url='https://api.npoint.io/ed99320662742443cc5b').json()]
    the_post = [post for post in all_posts if post.id == post_id][0]
    return render_template("post.html", post=the_post)

if __name__ == "__main__":
    app.run(debug=True)
