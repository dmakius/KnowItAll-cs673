from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

from helper_functions.import_questions import populate_db

db = SQLAlchemy()
DB_NAME = "test.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    from .views import views
    from .question import question
    from .leaderboard import leaderboard
    from .game import game
    from .auth import auth
    from .category import category
    from .player_profile import player_profile


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(question, url_prefix='/')
    app.register_blueprint(leaderboard, url_prefix='/')
    app.register_blueprint(game, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(category, url_prefix='/')
    app.register_blueprint(player_profile, url_prefix='/')

    from .models import Player

    create_database(app)

    # login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

        # define a function for loading the player
    @login_manager.user_loader
    def load_user(id):
        print("GETTING USER")
        return Player.query.get(int(id))

    return app

def create_database(app):

    if not path.exists("source/" + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        os.chdir("source")
        populate_db()
        # it will cause issues if does to change the working directory back
        os.chdir("../")
    else:
        print("Database found")
