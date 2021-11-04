from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

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
    username = db.Column(db.String(129), unique=False, nullable=False)
    score = db.Column(db.Integer)
    
# Define user table Schema
class Player(db.Model, UserMixin):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    player_name = db.Column(db.String(150))
    # TODO: add a relationship with the leaderboardScore using the foreign key.
    # TODO: need to add and change some vairable.


# Define Game table Schema
# TODO Eventually this will need to be split between 'GameType' and 'GameSession' where 
# 'GameType' defines initial variables and 'GameSession' stores the user's current game which updates during play
class Game(db.Model):
    __tablename__ = "Game"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(129), unique=False, nullable=False)
    lives = db.Column(db.Integer, unique=False, nullable = False)
    score = db.Column(db.Integer, unique=False, nullable = False)
    question_time = db.Column(db.Integer, unique=False, nullable = False)
    skip_question = db.Column(db.Boolean, unique=False, nullable = False)
    num_skip_question = db.Column(db.Integer, unique=False, nullable = False)
    questions_left = db.Column(db.String(300), unique=True, nullable=False) #if we have significantly more questions this needs to be longer
    max_questions = db.Column(db.Integer, unique=False, nullable = False)
    question = db.Column(db.String(129), unique=False, nullable=True)
    option_1 = db.Column(db.String(129), unique=False, nullable=True)
    option_2 = db.Column(db.String(129), unique=False, nullable=True)
    option_3 = db.Column(db.String(129), unique=False, nullable=True)
    option_4 = db.Column(db.String(129), unique=False, nullable=True)
    answer_location = db.Column(db.Integer, unique=False, nullable = False)