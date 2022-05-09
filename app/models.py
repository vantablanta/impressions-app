from email.policy import default
from . import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(60),  nullable = False)
    bio = db.Column(db.String(60), nullable = False, default="Change Bio" )
    profile_picture = db.Column(db.String(300),  nullable = False, default='https://cdn.pixabay.com/photo/2016/08/31/11/54/icon-1633249_960_720.png')
    comment = db.relationship("Comments",backref='poster', lazy=True)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.password}', '{self.profile_picture}')"
    
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password,password)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120),nullable = False)
    body = db.Column(db.String(120),nullable = False )
    comments = db.Column(db.String(300),nullable = False)
    upvotes = db.Column(db.Integer,nullable = False)
    downvotes = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f"User('{self.category}', '{self.body}', '{self.comments}', '{self.upvotes}', '{self.downvotes}')"

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




