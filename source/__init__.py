from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

from .import_questions import populate_db

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
   
    
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(question, url_prefix='/') 
    app.register_blueprint(leaderboard, url_prefix='/') 
    app.register_blueprint(game, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/') 
    
    create_database(app)
    
    from .models import Player
    # login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # define a function for loading the user
    @login_manager.user_loader
    def loads_user(id):
        return Player.query.get(int(id))
    
    return app

def create_database(app):
    os.chdir("source")
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        populate_db()
        
    else:
        print("Database found")

