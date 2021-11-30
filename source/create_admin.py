from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required
from . import db
from .models import Player, LeaderboardScore, Question
from werkzeug.security import generate_password_hash

email = 'admin@test.com'
player_name='admin'
password1= "admin1234"
new_admin = Player(email=email, player_name=player_name, password=generate_password_hash(password1, method='sha256'), admin=False)

db.session.add(new_admin)
db.session.commit()