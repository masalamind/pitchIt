from flask import Flask, render_template, request, redirect, url_for
# from flask_bootstrap import Bootstrap
# from config import config_options
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


app = Flask(__name__)

def create_app(config_name):

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
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

@app.route('/add-pitch')
def new_pitch():
    return render_template('new_pitch.html')

@app.route('/add-comment')
def new_comment():
    return render_template('new_comment.html')


@app.route('/thankyou', methods=['GET', 'POST'])
def thankspage():
    new_pitch = request.form.get("new-pitch")
    new_pitch_tag = request.form.get("pitch-tag")
    thanks = 'comment'
    return render_template('thankyou.html', thanks_type=thanks, pitch=new_pitch, tag=new_pitch_tag)

# bootstrap = Bootstrap()
db = SQLAlchemy()
