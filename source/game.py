from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random, math
from . import db
from .models import Game, Question

game = Blueprint('game', __name__)


@game.route('/game/settings', methods=['GET', 'POST'])
def gameSettings():
    # Set the game variables
    answer_location = 0

    # get the total number of questions and prepare array to track provided questions
    total_num_questions = Question.query.count()

    #TODO We need to dynamically get the game associated with the user/game instance and initiate that here.
    if Game.query.count() < 1:
        game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                    num_skip_question = 3, questions_left = str(0),
                    answer_location =  0, max_questions = total_num_questions)
        db.session.add(game)
        db.session.commit()
    else:
        game = Game.query.get(1)
        game.lives = 3
        game.question_time = 30
        game.score = 0
        game.num_skip_question = 3
        game.questions_left = str(0)
        game.answer_location = answer_location
        game.max_questions =  total_num_questions
        db.session.commit()

    #Check if the category is defined, and if so set the game.category data to the category. Parse the questions table to get every id from that category
    #Set up the conditional logic for the initialization of the questions_left array to only populate with valued from the category.

    # initialize the remaining questions array 
    questions_left = random.sample(list(range(1, total_num_questions + 1)), total_num_questions)
    
    # select the random question for the first question
    str_id = questions_left[0]
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
    game.question = str_id
    game.answer_location = answer_location
    game.cr_time = datetime.now()
    db.session.commit()

    # Define the data to be handed off to the template
    return_data = [{"Lives" : game.lives}, {"Question Time" : game.question_time}, {"Score" : game.score}, {"Number Question Skips" : game.num_skip_question},
                   {"Question": q.question}, {"Option_1": answers[0]}, {"Option_2": answers[1]}, {"Option_3": answers[2]}, {"Option_4": answers[3]}]
    print(return_data)

    return jsonify(return_data)

# Return the answer to the current question
@game.route('/game/answer')
def gameAnswer():
    #TODO We need to dynamically get the game associated with the user/game instance
    game = Game.query.get(1)
    return_data = [{"Answer_Location" : game.answer_location}]
    return(jsonify(return_data))

# Modify the game's lives
@game.route('/game/removelife')
def removeLife():
    #TODO We need to dynamically get the game associated with the user/game instance
    game = Game.query.get(1)
    game.lives = game.lives - 1
    db.session.commit()
    return(str(game.lives))

        
#Modify the game's remaining question skips
@game.route('/game/skip_question')
def skipQuestion():
    #TODO We need to dynamically get the game associated with the user/game instance
    game = Game.query.get(1)
    game.num_skip_question = game.num_skip_question - 1
    db.session.commit()

    return(str(game.num_skip_question))



#Update Score and reset question Time
@game.route('/game/update_score')
def updateScore():
    #TODO We need to dynamically get the game associated with the user/game instance
    game = Game.query.get(1)

    #Sent the current time for the next question, and take the difference for the passed time
    previous_time = game.cr_time
    game.cr_time = datetime.now()
    passed_time = (game.cr_time - previous_time)

    #Update the score based on how much time has passed.
    game.score = game.score + math.floor(float(100) * float(max(31 - passed_time.seconds, 0 ))/30)
    db.session.commit()

    return(str(game.score))