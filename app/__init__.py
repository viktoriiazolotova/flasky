from pickle import FALSE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

load_dotenv()

def create_app(testing=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)


    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SQLALCHEMY_ECHO"] = True
    
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .routes.breakfast import breakfast_bp
    from .routes.menu import menu_bp
    
    app.register_blueprint(breakfast_bp)
    app.register_blueprint(menu_bp)

    from app.models.breakfast import Breakfast
    from app.models.menu import Menu


    return app