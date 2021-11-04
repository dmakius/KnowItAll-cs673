from flask import Flask, Blueprint, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
import random

from . import db
from .models import Question, Game

question = Blueprint('question', __name__)

@question.route('/question/')
def getSingleQuestion():
    game = Game.query.get(1)

    # get random question from ID's remaining
    questions_left = game.questions_left.split(',')
    
    # the first question has a [ at the beginning which needs to be removed
    str_id = int(''.join(filter(str.isdigit, questions_left[0])))
    questions_left.remove(questions_left[0])
    print(str_id)
    q = Question.query.get(str_id)

    # Shuffle the 4 potential answers
    answer_location = 0
    input = [q.answer, q.option_1, q.option_2, q.option_3]
    answers = random.sample(input, len(input))


    # Determine the location of the answer
    for x in range(4):
        if answers[x] == q.answer:
            answer_location = x + 1

    #clean up the questions_left string into just ints, for some reason it grows otherwise
    for i in range(0, len(questions_left)):
        if (i < len(questions_left) - 1):
            questions_left[i] = int(questions_left[i])
        else:
            #the last question has a ] at the end which needs to be removed
            questions_left[i] = int(questions_left[i].rstrip(questions_left[i][-1]))

    #if the questions_left array is empty, reinitialize it with all of the questions.
    if len(questions_left) == 0:
        questions_left = random.sample(list(range(1, game.max_questions + 1)), game.max_questions)

    # Update all of these parameters in the game object
    game.questions_left = str(questions_left)
    print(game.questions_left)
    game.question = q.question
    game.option_1 = answers[0]
    game.option_2 = answers[1]
    game.option_3 = answers[2]
    game.option_4 = answers[3]
    game.answer_location = answer_location
    db.session.commit()

    # convert data into JSON object
    return_data = [{"Question": q.question}, {"Option_1": answers[0]}, {"Option_2": answers[1]},
                   {"Option_3": answers[2]}, {"Option_4": answers[3]}]

    # print data to be retuned on back end
    print(return_data)
    # return data as json
    return jsonify(return_data)
