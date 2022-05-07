from flask import Flask
from .main import main_blueprint
from config import config_options

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)

    return app



