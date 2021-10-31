from flask import Flask, Blueprint, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
import random

from .models import Question, LeaderboardScore

views = Blueprint('views', __name__)
  
# ROUTES
@views.route('/')
def main():
    return render_template('main.html')


@views.route('/game')
def game():
    # get the total number of questions
    total_num_questions = Question.query.count()
    # select a randon number annd conver to int
    random_question_number = random.randint(1, total_num_questions)
    random_question_number = str(random_question_number)

    # select a random question
    q = Question.query.get(random_question_number)
    return render_template('game.html', q=q, num=total_num_questions)


@views.route('/leaderboard')
def leaderBoard():
    scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    return render_template('leaderboard.html', scores=scores)