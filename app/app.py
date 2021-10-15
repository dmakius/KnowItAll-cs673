from flask import Flask, render_template, request, redirect, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
import random

# create Flask opbject
app = Flask(__name__)

# create SQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create DB Object
db = SQLAlchemy(app)

from models import Question, LeaderboardScore


# ROUTES
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/game')
def game():
    # get the total number of questions
    total_num_questions = Question.query.count()
    # select a randon number annd conver to int
    random_question_number = random.randint(1, total_num_questions)
    random_question_number = str(random_question_number)

    # select a random question
    q = Question.query.get(random_question_number)
    return render_template('game.html', q=q, num=total_num_questions)


@app.route('/question/<int:id>')
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


@app.route('/leaderboard/create', methods=['POST'])
def leaderBoard_create():
    username = request.form['username']
    score = request.form['score']
    new_score = LeaderboardScore(category='TEST', username=username, score=score)

    db.session.add(new_score)
    db.session.commit()
    return redirect(url_for('leaderBoard'))


@app.route('/leaderboard')
def leaderBoard():
    scores = LeaderboardScore.query.all()
    return render_template('leaderboard.html', scores=scores)