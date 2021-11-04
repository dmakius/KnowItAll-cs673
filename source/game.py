from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from . import db
from .models import Game, Question

game = Blueprint('game', __name__)


@game.route('/game/settings', methods=['GET', 'POST'])
def gameSettings():
    # Set the game variables
    answer_location = 0

    # get the total number of questions and prepare array to track provided questions
    total_num_questions = Question.query.count()

    # Either create the game variables if they don't exist or set the game variables to the initial variables upon starting a game.
    if Game.query.count() < 1:
        game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                    skip_question = True, num_skip_question = 3, questions_left = str(0),
                    answer_location =  0, max_questions = total_num_questions)
        db.session.add(game)
        db.session.commit()
    else:
        game = Game.query.get(1)
        game.lives = 3
        game.question_time = 30
        game.score = 0
        game.skip_question = True
        game.num_skip_question = 3
        game.questions_left = str(0)
        game.answer_location = answer_location
        game.max_questions =  total_num_questions
        db.session.commit()

    # initialize the remaining questions array
    questions_left = random.sample(list(range(1, total_num_questions + 1)), total_num_questions)
    
    # select the random question for the first question
    str_id = random.randint(1, total_num_questions)
    q = Question.query.get(str_id)

    # Shuffle the 4 potential answers
    input = [q.answer, q.option_1, q.option_2, q.option_3]
    answers = random.sample(input, len(input))

    # Determine the location of the answer
    for x in range(4):
        if answers[x] == q.answer:
            answer_location = x + 1

    #Remove the question from the questions left array
    questions_left.remove(str_id)

    #pass all the question information to the game object
    game.questions_left = str(questions_left)
    print(game.questions_left)
    game.question = q.question
    game.option_1 = answers[0]
    game.option_2 = answers[1]
    game.option_3 = answers[2]
    game.option_4 = answers[3]
    game.answer_location = answer_location
    db.session.commit()

    # Define the data to be handed off to the template
    return_data = [{"Lives" : game.lives}, {"Question Time" : game.question_time}, {"Score" : game.score}, {"Number Question Skips" : game.num_skip_question},
                   {"Question": game.question}, {"Option_1": game.option_1}, {"Option_2": game.option_2}, {"Option_3": game.option_3}, {"Option_4": game.option_4}]
    print(return_data)

    return jsonify(return_data)

@game.route('/game/answer')
def gameAnswer():
    # get the game state
    game = Game.query.get(1)

    print(game.answer_location)

    # prepare ajax request
    return_data = [{"Answer_Location" : game.answer_location}]

    return(jsonify(return_data))

#Change Lives
#TODO currently this is changing the 'game' object, eventually we want it to be handling a game session which would be provided in the url
@game.route('/game/removelife')
def removeLife():
    
    #GameType is only a single entity table so (1) works here.
    game = Game.query.get(1)
    game.lives = game.lives - 1
    db.session.commit()

    print(game.lives)
    #return new lives
    return(str(game.lives))

        

#Change Question Skips
#TODO currently this is changing the 'game' object, eventually we want it to be handling a game session which would be provided in the url
@game.route('/game/skip_question')
def skipQuestion():
    
    #GameType is only a single entity table so (1) works here. Eventually we want the 
    game = Game.query.get(1)
    game.num_skip_question = game.num_skip_question - 1
    db.session.commit()

    print(game.num_skip_question)
    # return new number of question skips
    return(str(game.num_skip_question))



#Update Score

#Check Valid Time