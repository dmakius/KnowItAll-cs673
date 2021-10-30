from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

from .import_questions import populate_db

db = SQLAlchemy()
DB_NAME = "test.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from .views import views
    from .game import game
    from .leaderboard import leaderboard
    
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(game, url_prefix='/') 
    app.register_blueprint(leaderboard, url_prefix='/') 
    
    create_database(app)
    
    return app

def create_database(app):
    os.chdir("source")
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
        populate_db()
        
    else:
        print("Database found")