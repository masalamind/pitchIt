from flask import Flask, render_template
from .config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)
from app import views

@app.route('/')
@app.route('/pitches')
def index():
    return render_template('index.html')



@app.route('/signup')
def register():
    return render_template('signup.html')

@app.route('/signin')
@app.route('/login')
def signin():
    return render_template('login.html')