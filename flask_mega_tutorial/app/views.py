from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lars'}
    posts = [ # Fake array of posts
        {
            'author': {'nickname': 'Lars'},
            'body': "Beautiful day!"
        },
        {
            'author': {'nickname': 'Lars'},
            'body': "Beep boop!"
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
