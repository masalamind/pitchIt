from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from config import config_options
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    return app


app.config.from_object(DevConfig)
from app import views

@app.route('/')
@app.route('/pitches')
def index():
    return render_template('index.html')



@app.route('/signup')
def register():
    return render_template('signup.html')


@app.route('/login')
def signin():
    return render_template('login.html')

@app.route('/bookmarks')
def bookmarks():
    return render_template('bookmarked.html')

@app.route('/profile')
def profile():
    return render_template('user_profile.html')


# bootstrap = Bootstrap()
db = SQLAlchemy()