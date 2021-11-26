from flask import Flask, Blueprint, render_template, jsonify, request,  url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import json
from . import db
from .models import Question, LeaderboardScore, Player, Game
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

# ROUTES
@views.route('/')
def main():
    print(current_user)
    return render_template('main.html', user=current_user)


@views.route('/game')
def game():
    print(current_user)
    return render_template('game.html', user=current_user)

@views.route('/category')
def category():
    print(current_user)
    return render_template('category.html', user=current_user)



@views.route('/playerProfile')
def userProfile():
    scores = LeaderboardScore.query.filter_by(userid=current_user.id)
    return render_template('player_profile.html', user=current_user, scores=scores)

# route to the test-feature page
@views.route('/test-feature', methods=['GET', 'POST'])
@login_required
def show_players():
    players = Player.query.all()
    return render_template('delete_player.html', user=current_user, players=players)


@views.route('/leaderboard')
def leaderBoard():
    scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    return render_template('leaderboard.html', user=current_user, scores=scores)


@views.route('/leaderBoard-chooseCategory', methods=['POST'])
def leaderBoardchooseCategory():
    select = request.form.get('category')
    if select == 'All':
        scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    else:
        scores = LeaderboardScore.query.filter( LeaderboardScore.category==select).all()
    print(select)

    return render_template('leaderboard.html', user=current_user, scores=scores)


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