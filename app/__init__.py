from flask import Flask, render_template

app = Flask(__name__)

from app import views

@app.route('/')
@app.route('/pitches')
def index('/'):
    return render_template('index.html')