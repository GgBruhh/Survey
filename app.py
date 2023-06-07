from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET'
debug = DebugToolbarExtension(app)


questions = []


def get_questions():
    for question in survey.questions:
        questions.append(question.question)

get_questions()

@app.route('/')
def show_home_page():
    return render_template('home.html', survey=survey)

@app.route('/begin', methods=['POST'])
def begin_survey():
    session['responses'] = []
    return redirect("/questions/0")

@app.route('/questions/0')
def show_question1():
    question = questions[0]
    choices = survey.questions[0].choices
    print(choices)
    return render_template('question1.html',survey=survey,question=question,choices=choices)

@app.route('/questions/<id>')
def show_questions(id):
    responses = session.get('responses')
    id = len(responses)
    question = questions[id]
    choices = survey.questions[id].choices
    return render_template('question1.html',survey=survey,question=question,choices=choices)



@app.route("/answer", methods=['POST'])
def get_answer():
    print(request)
    choice = request.form['answer']
    responses = session['responses']
    responses.append(choice)

    session['responses'] = responses
    
    
    
    if len(responses) == len(questions):
        return redirect('/complete')
    
    if (len(responses) != id):
        # Trying to access questions out of order.
        flash(f"Invalid question id: {id}.")
        return redirect(f"/questions/{len(responses)}")
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route('/complete')
def show_complete():
    return render_template('complete.html')
