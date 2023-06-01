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

@app.route('/questions/0')
def show_question1():
    return render_template('question1.html')

@app.route('/questions/1')
def show_question1():
    return render_template('question2.html')

@app.route('/questions/2')
def show_question1():
    return render_template('question3.html')

@app.route('/questions/3')
def show_question1():
    return render_template('question4.html')
