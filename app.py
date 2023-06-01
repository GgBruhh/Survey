from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_home_page():

    return render_template('home.html', survey=survey)