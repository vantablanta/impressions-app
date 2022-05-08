from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique= True)
    email = db.Column(db.String, unique= True )
    password = db.Column(db.String)

    # hash the password 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


