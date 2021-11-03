from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from . import db
from .models import Player

auth = Blueprint("auth", __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check the email exist in the database
        user = Player.query.filter_by(email=email).first()
        
        if user:
            # Check the password equal to the user's password in database
            if check_password_hash(user.password, password):
                flash('Logged in successful', category='success')
                
                # User login and remember the user
                login_user(user, remember=True)
                
                # TODO: need to redirect to the home page
                return redirect(url_for('views.main',user=current_user))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('email does not exist.', category='error')
    return render_template("login.html", user=current_user)

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful', category='success')
    return redirect(url_for('views.main'))

# Sign up route
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        player_name = request.form.get('playerName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = Player.query.filter_by(email=email).first()
        # Check the email already exists or not
        if user:
            flash('Email already exists.', category='error')
        # Check length of the email
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        # Check the username
        elif len(player_name) < 2:
            flash('Player name must be greater than 1 characters.', category='error')
        # Check the length of password and
        # TODO: add regular expression later
        elif len(password1) < 7:
            flash('password must be at least 7 characters.', category='error')
        # Check the password and comfirmed password
        elif password1 != password2:
            flash('password don\'t match', category='error')
        else:
            # add user to the test database
            new_user = Player(email=email, player_name = player_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.main',user=current_user))
            # login the user after created account, and remember it
            # TODO: after we sign up, where should we direct to?
    return render_template('sign_up.html', user=current_user)