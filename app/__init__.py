from flask import Flask, render_template
from .config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)
from app import views

@app.route('/')
@app.route('/pitches')
def index():
    return render_template('index.html')