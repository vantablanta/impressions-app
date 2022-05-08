from . import main_blueprint
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import User

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/pitches')
def pitches():
    pitches = [
        {
            "id" : 1,
            'poster': "Michelle",
            "category": "Random",
            "body": "Like it and leav it",
            "comments": ["comment1","comment2","comment3",],
            "upvotes": 8,
            "downvotes": 0
        },
    ]
    return render_template('pitches.html', pitches = pitches)

# fix
@main_blueprint.route('/pitches/review/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    """"""

@main_blueprint.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


