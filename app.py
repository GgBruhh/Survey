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
    question = survey.questions[0]
    choices = question.choices
    print(choices)
    return render_template('question1.html',survey=survey,question=question,choices=choices)

@app.route('/questions/1')
def show_question2():
    question = survey.questions[1]
    choices = question.choices
    return render_template('question2.html',survey=survey,question=question,choices=choices)

@app.route('/questions/2')
def show_question3():
    question = survey.questions[2]
    choices = question.choices
    return render_template('question3.html',survey=survey,question=question,choices=choices)

@app.route('/questions/3')
def show_question4():
    question = survey.questions[3]
    choices = question.choices
    return render_template('question4.html',survey=survey,question=question,choices=choices)
