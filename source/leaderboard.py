from flask import Flask, Blueprint, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy

from . import db
from .models import LeaderboardScore, Game

leaderboard = Blueprint('leaderboard', __name__)

@leaderboard.route('/leaderboard/create', methods=['POST'])
def leaderBoard_create():
    game = Game.query.get(1)
    username = request.form['username']
    score = game.score
    new_score = LeaderboardScore(category='TEST', username=username, score=score)

    db.session.add(new_score)
    db.session.commit()
    return redirect(url_for('views.leaderBoard'))