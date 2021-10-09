from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


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
	question = Question.query.all()
	print(question)
	return render_template('game.html')

@app.route('/leaderboard')
def leaderBoard():
	return render_template('leaderboard.html')