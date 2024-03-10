from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user={'username':'Marveric'}
    posts=[
        {
            'author':{'username':'Jordan'},
            'body':'Glory is fleeting'

        },

        {
            'author':{'username':'Iverson'},
            'body':'obscurity is forever'
        }
    ]
    return render_template('index2.html',title='Home',user=user,posts = posts)
