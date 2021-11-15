from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy import DateTime

# Define question table Schema
class Question(db.Model):
    __tablename__ = "Question"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(129), unique=False, nullable=False)
    question = db.Column(db.String(129), unique=True, nullable=False)
    answer = db.Column(db.String(129), unique=False, nullable=False)
    option_1 = db.Column(db.String(129), unique=False, nullable=False)
    option_2 = db.Column(db.String(129), unique=False, nullable=False)
    option_3 = db.Column(db.String(129), unique=False, nullable=False)

# Define LeaderboardScore table Schema
class LeaderboardScore(db.Model):
    __tablename__ = "LeaderboardScore"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(129), unique=False, nullable=False)
    userid = db.Column(db.Integer, unique=False, nullable=False)
    username = db.Column(db.String(129), unique=False, nullable=False)
    score = db.Column(db.Integer)

# Define user table Schema
class Player(db.Model, UserMixin):
    __tablename__ = "Player"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    player_name = db.Column(db.String(150))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))
    # TODO: add a relationship with the leaderboardScore using the foreign key.
    # TODO: need to add and change some variable.


# Define Game table Schema
class Game(db.Model):
    __tablename__ = "Game"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(129), unique=False, nullable=False)
    category = db.Column(db.String(129), unique=False, nullable=True)
    lives = db.Column(db.Integer, unique=False, nullable = False)
    score = db.Column(db.Integer, unique=False, nullable = False)
    question_time = db.Column(db.Integer, unique=False, nullable = False)
    num_skip_question = db.Column(db.Integer, unique=False, nullable = False)
    questions_left = db.Column(db.String(300), unique=False, nullable=False) #if we have significantly more questions this needs to be longer
    max_questions = db.Column(db.Integer, unique=False, nullable = False)
    question_id = db.Column(db.Integer, unique=False, nullable = True)
    answer_location = db.Column(db.Integer, unique=False, nullable = False)
    cr_time = db.Column(DateTime(timezone=True), server_default=func.now())
    num_fifty_fifty = db.Column(db.Integer, unique=False, nullable = False)
    fifty_fifty_option = db.Column(db.String(100), unique=False, nullable = False)
    player_id = db.relationship("Player", backref="Player", uselist=False)