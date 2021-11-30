from flask import Blueprint, render_template, jsonify, request, flash
import json

from . import db
from .models import LeaderboardScore, Player
from flask_login import login_required, current_user
from sqlalchemy import desc, func

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


@views.route('/playerProfile')
@login_required
def userProfile():
    print('GETTING PLAYERS SCORES')
    #scores = db.session.query(LeaderboardScore.category, LeaderboardScore.username, LeaderboardScore.score). \
   #     filter_by(userid=current_user.id). \
    #    group_by(LeaderboardScore.category). \
    #    order_by(func.max(LeaderboardScore.score).desc())
    scores = db.session.query(LeaderboardScore.category, LeaderboardScore.score, func.max(LeaderboardScore.score)).filter_by(userid=current_user.id).group_by(LeaderboardScore.category).all()
    #scores = LeaderboardScore.query().filter_by(userid=current_user.id).group_by(LeaderboardScore.category).order_by(func.max(LeaderboardScore.score).desc())
    print(scores)
    return render_template('player_profile.html', user=current_user, scores=scores)


# route to the test-feature page
@views.route('/test-feature', methods=['GET', 'POST'])
@login_required
def show_players():
    players = Player.query.all()
    return render_template('delete_player.html', user=current_user, players=players)


@views.route('/leaderboard')
@login_required
def leaderBoard():
    scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    return render_template('leaderboard.html', user=current_user, scores=scores)


@views.route('/leaderBoard-chooseCategory', methods=['POST'])
def leaderBoardchooseCategory():
    select = request.form.get('category')
    if select == 'All':
        scores = LeaderboardScore.query.order_by(LeaderboardScore.score.desc()).all()
    else:
        scores = LeaderboardScore.query.filter(LeaderboardScore.category == select).all()
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


# route admin page
@views.route('/admin', methods=['GET', 'POST'])
@login_required
def display_admin():
    user = Player.query.filter_by(id=current_user.id).first()
    if user.admin == 1:
        return render_template('admin.html', user=current_user)
    else:
        flash('You are not allow to go to admin page.', category='error')
    return render_template('main.html', user=current_user)
