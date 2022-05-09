from . import main_blueprint
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required

from ..models import User

from .forms import CommentForm, UpdateProfile
from .. import db


@main_blueprint.route('/')
def home():
    return render_template('index.html')


@main_blueprint.route('/pitches')
def pitches():
    pitches = [
        {
            "id": 1,
            'poster': "Michelle",
            "category": "Random",
            "body": "Like it and leav it",
            "comments": ["comment1", "comment2", "comment3", ],
            "upvotes": 8,
            "downvotes": 0
        },
    ]
    return render_template('pitches.html', pitches=pitches)

# fix
@main_blueprint.route('/pitches/review/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    """"""


@main_blueprint.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main_blueprint.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(name=uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.name))
    return render_template('profile/update.html', form=form)
