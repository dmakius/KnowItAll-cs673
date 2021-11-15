from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Game, Question, Player

category = Blueprint("category", __name__)

@category.route('/category/select', methods=['POST'])
def mycategory():
    #TODO We need to dynamically get the game associated with the user/game instance and initiate that here.
    #TODO Right now the game table will be empty since you go to categories before the first game, so we're also initializing that first game instance here
    #create a game for the player
   
    total_num_questions = Question.query.count()
    if (current_user.is_authenticated):
        #bring up the players game and reinitialize the variables
        p = Player.query.get(current_user.id)
        new_game = Game.query.get(p.game_id)
        new_game.lives = 3
        new_game.question_time = 30
        new_game.score = 0
        new_game.num_skip_question = 3
        new_game.questions_left = str(0)
        new_game.answer_location = 0
        new_game.max_questions =  total_num_questions
        new_game.num_fifty_fifty = 3
        new_game.fifty_fifty_option = str(0)
        db.session.commit()
    else:
        #if player doesn't exit create a new game that is NOT associated with the user
        new_game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                num_skip_question = 3, questions_left = str(0),
                answer_location =  0, max_questions = total_num_questions,
                num_fifty_fifty = 3, fifty_fifty_option = str(0))
        db.session.add(new_game)
        db.session.commit()
       
    
    new_game.category = request.json['category']
    db.session.commit()
    print(new_game)
    print(new_game.category)
    return_data = [{"gameID": new_game.id}]
    return jsonify(return_data)