from unicodedata import category
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    secure_password = db.Column(db.String(60),  nullable=False)
    bio = db.Column(
        db.String(60),  default="I love first impressions", nullable=False)
    profile_picture = db.Column(db.String(
        300),  nullable=False, default='https://cdn.pixabay.com/photo/2016/08/31/11/54/icon-1633249_960_720.png')
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.name}')"

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def secure_password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments =db.relationship("Pitch", backref="comments", lazy="dynamic")
    
    def __repr__(self):
        return f"User('{self.body}')"
    
    all_comments = []

    def __init__(self, user_id, body):
        self.user_id = user_id
        self.body = body


    def save_comment(self):
        Comments.all_comments.append(self)

    @classmethod
    def get_comments(cls):
        data = []
        for comment in cls.all_comments:
            data.append(comment)
        return data


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), index=True, nullable=False)
    body = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)

    def __init__(self, title, category, body, user_id):
        self.title = title
        self.category = category
        self.body = body
        self. user_id = user_id
