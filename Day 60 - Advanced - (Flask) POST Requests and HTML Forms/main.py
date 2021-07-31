from flask import Flask, render_template, request
from post import Post
import requests, smtplib

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

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['message']
        my_email = 'email@gmail.com'
        my_password = 'password'

        with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs='kevin.mrosa96@gmail.com',
                    msg=f'Name: {name}\nE-mail: {email}\nPhone Number: {phone}\nMessage: {msg}'
                )

    return render_template('contact.html', page='contact')

if __name__ == '__main__':
    app.run(debug=True)
