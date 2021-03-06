from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
from .models import User

# 
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')
 
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager.init_app(app)

    mail.init_app(app) 

    return app



