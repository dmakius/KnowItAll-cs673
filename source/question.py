from flask import Flask, Blueprint, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
import random

from .models import Question

question = Blueprint('question', __name__)

@question.route('/question/<int:id>')
def getSingleQuestion(id):
    str_id = str(id)
    q = Question.query.get(str_id)


    # Shuffle the 4 potential answers

    answer_location = 0
    input = [q.answer, q.option_1, q.option_2, q.option_3]
    answers = random.sample(input, len(input))


    # Determine the location of the answer

    for x in range(4):
        if answers[x] == q.answer:
            answer_location = x + 1

    # convert data into JSON object
    # TODO: fix labels as the 'Answer' corresponds to a random answer, not the answer

    return_data = [{"Category": q.category}, {"Question": q.question}, {"Option_1": answers[0]}, {"Option_2": answers[1]},
                   {"Option_3": answers[2]}, {"Option_4": answers[3]}, {"Answer_Location": answer_location}]

    # print data to be retuned on back end
    print(return_data)
    # return data as json
    return jsonify(return_data)
