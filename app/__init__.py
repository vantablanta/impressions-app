from flask import Flask
from .main import main_blueprint
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    return app



