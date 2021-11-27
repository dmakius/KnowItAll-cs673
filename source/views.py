from flask import Flask, Blueprint, render_template, jsonify, request, url_for, redirect, flash
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
    return render_template('main.html', user=current_user)


@views.route('/game')
def game():
    return render_template('game.html', user=current_user)

@views.route('/category')
def category():
    return render_template('category.html', user=current_user)

@views.route('/leaderboard')
def leaderBoard():
    scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    return render_template('leaderboard.html', user=current_user, scores=scores)

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


@views.route('/admin', methods=['GET','POST'])
@login_required
def display_admin():
    user = Player.query.filter_by(id=current_user.id).first()
    if user.admin == 1:
        return render_template('admin.html', user=current_user)
    else:
        flash('You are not allow to go to admin page.', category='error')
    return render_template('main.html', user=current_user)
