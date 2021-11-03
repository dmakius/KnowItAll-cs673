from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from . import db
from .models import Game, Question

game = Blueprint('game', __name__)


@game.route('/game/settings')
def gameSettings():
    # Set the game variables
    lives = 3
    timer = 30
    score = 0
    skip_question = True #eventually this functionality would be used to disable lifelines if desired.
    num_skip_question = 3

    # Either create the game variables if they don't exist or set the game variables to the initial variables upon starting a game.
    if Game.query.count() < 1:
        game = Game(type = 'TEST', lives = lives, score = score, question_time = timer, skip_question = skip_question, num_skip_question = num_skip_question)
        db.session.add(game)
        db.session.commit()
    else:
        game = Game.query.get(1)
        game.lives = lives
        game.question_time = timer
        game.score = score
        game.skip_question = skip_question
        game.num_skip_question = num_skip_question
        db.session.commit()

    # get the total number of questions
    total_num_questions = Question.query.count()
    
    # prepare strings off data to be passed off

    # Define the data to be handed off to the template
    return_data = [{"Lives" : game.lives}, {"Question Time" : game.question_time}, {"Score" : game.score}, {"Number Question Skips" : game.num_skip_question},
                   {'numberQuestions': total_num_questions}]
    print(return_data)

    return jsonify(return_data)