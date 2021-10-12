from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
import random

#create Flask opbject
app = Flask(__name__)

#create SQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create DB Object
db = SQLAlchemy(app)

from models import Question

   
#ROUTES
@app.route('/')
def main():
	return render_template('main.html')

@app.route('/game')
def game():
    #get the total number of questions
    total_num_questions = Question.query.count()
    #select a randon number annd conver to int
    random_question_number = random.randint(1,total_num_questions)
    random_question_number = str(random_question_number)
    
    #select a random question
    q = Question.query.get(random_question_number)
    return render_template('game.html' , q = q, num =total_num_questions )

@app.route('/question/<int:id>')
def getSingleQuestion(id):  
    str_id = str(id)                      
    q = Question.query.get(str_id)
    print(q.question)
    return (str(q.question))
    	
@app.route('/leaderboard')
def leaderBoard():
	return render_template('leaderboard.html')


