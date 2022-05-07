import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config(object):
    SQLALCHEMY_DB_URI = os.getenv('LOCAL_DATABASE_URI')
    DEBUG = os.getenv('DEBUG')

    

    

