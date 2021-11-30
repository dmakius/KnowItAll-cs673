from flask import Blueprint, render_template, jsonify, request, flash
import json
from main import ENV
from . import db
from .models import LeaderboardScore, Player
from flask_login import login_required, current_user
from sqlalchemy import desc, func
import psycopg2

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
    if ENV == "DEV":
        scores = db.session.query(LeaderboardScore.category, LeaderboardScore.username, LeaderboardScore.score). \
        filter_by(userid=current_user.id). \
        group_by(LeaderboardScore.category). \
        order_by(func.max(LeaderboardScore.score).desc())
    else:
        
        db_connection_url="postgres://isjsgcztftfslw:74317591be27ee99df92e8860a110f5cf7f6ed0d26719378815c8e554bf3a521@ec2-23-23-219-25.compute-1.amazonaws.com:5432/dfrqcekr8skvl"
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(db_connection_url)
        print("Connection successful")
        cursor = conn.cursor()
        userID =  current_user.id
        print("Looking for top scores for user:" + str(userID))
        scores = cursor.execute(''' SELECT category, MAX(score) FROM "LeaderboardScore" where userid = '%s' group by category ''', [userID] )
        conn.close()
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
