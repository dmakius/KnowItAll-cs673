from flask import Flask, Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random
import json
from . import db
from .models import Question, LeaderboardScore, Player
from flask_login import login_required, current_user


views = Blueprint('views', __name__)
  
# ROUTES
@views.route('/')
def main():
    return render_template('main.html' ,user ="")


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

@views.route('/playerProfile')
def userProfile():
    return "<P>This is the user Profile Page, implement later</p>"

# route to the test-feature page
@views.route('/test-feature', methods=['GET', 'POST'])
@login_required
def show_players():
    players = Player.query.all()
    return render_template('delete_player.html', user=current_user, players=players)


# route for the delete-user function
@views.route('/delete-player', methods=['POST'])
def delete_player():
    player = json.loads(request.data)
    playerId = player['playerId']
    player = Player.query.get(playerId)
    if player:
        db.session.delete(player)
        db.session.commit()

    return jsonify({})