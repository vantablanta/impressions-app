from . import db
from . import  login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    comments = db.relationship('Comments', backref='user', lazy=True)

    # hash the password
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Comments:
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text, db.ForeignKey('person.id'))

    all_comments = []

    def __init__(self, user_id, username, body):
        self.user_id = user_id
        self.username = username
        self.body = body

    def save_comment(self):
       Comments.all_comments.append(self)

    @classmethod 
    def get_comments(cls):
        data = []

        for comment in cls.all_comments:
           data.append(comment)

        return data

