from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from . import db
from .models import Game, Question

category = Blueprint("category", __name__)

@category.route('/category/select', methods=['POST'])
def mycategory():
    #TODO We need to dynamically get the game associated with the user/game instance and initiate that here.
    #TODO Right now the game table will be empty since you go to categories before the first game, so we're also initializing that first game instance here
    if Game.query.count() < 1:
        total_num_questions = Question.query.count()
        game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                    num_skip_question = 3, questions_left = str(0),
                    answer_location =  0, max_questions = total_num_questions,
                    num_fifty_fifty = 3, fifty_fifty_option = str(0))
        db.session.add(game)
        db.session.commit()

    game = Game.query.get(1)
    game.category = request.json['category']
    db.session.commit()
    print(game.category)
    return "1"