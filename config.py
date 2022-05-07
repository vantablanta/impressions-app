from distutils.command.config import config
import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config():
    """"""
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevConfig(Config):
    # SQLALCHEMY_DB_URI = os.getenv('LOCAL_DATABASE_URI')
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

class ProdConfig(Config):
    """"""



config_options = {
    'prod': ProdConfig,
    'dev': DevConfig
}

    

    

