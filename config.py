import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config():
    """"""
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    SECRET_KEY = os.getenv('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_DEBUG = 0

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_SQLALCHEMY_DATABASE_URI')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')



config_options = {
    'prod': ProdConfig,
    'dev': DevConfig
}

    

    

