from flask import Flask, Blueprint, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy

from . import db
from .models import LeaderboardScore, Game
from flask_login import current_user


leaderboard = Blueprint('leaderboard', __name__)

@leaderboard.route('/leaderboard/create', methods=['POST'])
def leaderBoard_create():
    #TODO We need to dynamically get the game associated with the user/game instance
    game = Game.query.get(1)
    username = request.form['username']
    score = game.score
    userid = current_user.id if current_user.is_authenticated else 0
    new_score = LeaderboardScore(category='TEST', userid=userid, username=username, score=score)

    db.session.add(new_score)
    db.session.commit()
    return redirect(url_for('views.leaderBoard'))