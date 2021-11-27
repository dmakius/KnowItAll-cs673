from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user
from . import db
from .models import Player, LeaderboardScore, Question

admin = Blueprint('admin', __name__)


@admin.route('/admin/question')
def questions():
    user = Player.query.filter_by(id=current_user.id).first()
    if user.admin == 1:
        question = Question.query.order_by(Question.category.desc()).all()
        print(Question.category)
        return render_template('questions.html', user=current_user, question=question)
    else:
        flash('You are not allow to go to admin page.', category='error')
    return render_template('main.html', user=current_user)


@admin.route('admin/question/new')
def new():
    user = Player.query.filter_by(id=current_user.id).first()
    if user.admin == 1:
        return render_template('new_question.html', user=current_user)
    else:
        flash('You are not allow to go to admin page.', category='error')
    return render_template('main.html', user=current_user)


@admin.route('admin/question/edit', methods=['GET', 'POST'])
def edit():
    user = Player.query.filter_by(id=current_user.id).first()
    if user.admin == 1:
        if request.method == 'POST':
            id = request.form.get('question_id')
            print(id)
            question = Question.query.filter_by(id=id).first()
            return render_template('edit_question.html', user=current_user, question=question)
    else:
        flash('You are not allow to go to admin page.', category='error')
    return render_template('main.html', user=current_user)


@admin.route('admin/question/add_question', methods=['POST'])
def add_question():
    if request.method == 'POST':
        category = request.form.get('category')
        question = request.form.get('question')
        answer = request.form.get('answer')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')

        # compare if the question is already exist.
        q = Question.query.filter_by(question=question).first()
        if q:
            flash('Question already exists.', category='error')
        else:
            new_question = Question(category=category, question=question,
                                    answer=answer, option_1=option1,
                                    option_2=option2, option_3=option3)
            db.session.add(new_question)
            db.session.commit()
            flash('Question added!', category='success')
            return redirect(url_for('admin.questions'))
    return render_template("new_question.html")


@admin.route('admin/question/edit_question', methods=['GET', 'POST'])
def edit_question():
    if request.method == 'POST':
        q_id = request.form.get('question_id')
        q = Question.query.filter_by(id=q_id).first()
        if request.form.get('category'):
            new_category = request.form.get('category')
            q.category = new_category
        if request.form.get('question'):
            new_question = request.form.get('question')
            q.question = new_question
        if request.form.get('answer'):
            new_answer = request.form.get('answer')
            q.answer = new_answer
        if request.form.get('option_1'):
            new_option1 = request.form.get('option_1')
            q.option_1 = new_option1
        if request.form.get('option_2'):
            new_option2 = request.form.get('option_2')
            q.option_2 = new_option2
        if request.form.get('option_3'):
            new_option3 = request.form.get('option_3')
            q.option_3 = new_option3
        db.session.commit()
        flash('Edit success!', category='success')
        return render_template("edit_question.html", question=q, user=current_user)


@admin.route('admin/delete_question', methods=['POST'])
def delete_question():
    id = request.form.get('question_id')
    print(id)
    question = Question.query.filter_by(id=id).first()
    db.session.delete(question)
    db.session.commit()
    flash('Delete success!', category='success')
    return redirect(url_for('admin.questions'))


@admin.route('admin/delete_score', methods=['POST'])
def delete_score():
    id = request.form.get('score_id')
    print(id)
    score = LeaderboardScore.query.filter_by(id=id).first()
    db.session.delete(score)
    db.session.commit()
    flash('Delete success!', category='success')
    return redirect(url_for('views.leaderBoard'))

