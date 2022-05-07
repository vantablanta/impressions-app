from distutils.command.config import config
import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config():
    """"""
    # SQLALCHEMY_DB_URI = os.getenv('LOCAL_DATABASE_URI')

class DevConfig(Config):
    # SQLALCHEMY_DB_URI = os.getenv('LOCAL_DATABASE_URI')
    DEBUG = os.getenv('DEBUG')

class ProdConfig(Config):
    SQLALCHEMY_DB_URI = os.getenv('LOCAL_DATABASE_URI')


config_options = {
    'prod': ProdConfig,
    'dev': DevConfig
}

    

    

