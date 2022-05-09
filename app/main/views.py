from wsgiref import validate
from . import main_blueprint
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from ..models import User, Comments, Pitch

from .forms import CommentForm, UpdateProfile, PitchForm
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

# @main_blueprint.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
# @login_required
# def comment(pitch_id):
#     form = CommentForm()
#     pitch = Pitch.query.get(pitch_id)
#     all_comments = Comments.query.filter_by(pitch_id = pitch_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data 
#         pitch_id = pitch_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comments(comment = comment,user_id = user_id,pitch_id = pitch_id)
#         db.session.add(new_comment)
#         db.commit()
#         return redirect(url_for('.comment', pitch_id = pitch_id))
#     return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

@main_blueprint.route('/comment', methods=['GET', 'POST'])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        return redirect(url_for('main_blueprint.pitches'))
    return render_template("new_comment.html", form = form )




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


@main_blueprint.route('/pitch/add_new', methods=['GET', 'POST'])
@login_required
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        # title = form.title.data
        # category = form.category.data
        # body = form.body.data
        # user_id = current_user
        # pitch = Pitch(title=title, category=category, body=body, user_id=current_user._get_current_object())
        # db.session.add(pitch)
        # db.session.commit()
        return redirect(url_for('main_blueprint.home'))
    return render_template('new_pitch.html', form = form)




    
        
