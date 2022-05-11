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


@main_blueprint.route('/pitches')
def pitches():  
    pitches = Pitch.query.all()
    comments = Comments.query.all()
    return render_template('pitches.html', pitches=pitches, comments=comments)

@main_blueprint.route('/pitch/add_new', methods=['GET', 'POST'])
@login_required
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        body = form.body.data
        user_id = current_user._get_current_object().id
        pitch = Pitch(title=title, category=category, body=body, user_id=user_id)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main_blueprint.pitches'))
    return render_template('new_pitch.html', form = form)

@main_blueprint.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    all_comments = Comments.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html',all_comments=all_comments)

@main_blueprint.route('/comment', methods=['GET', 'POST'])
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
            body = form.body.data
            user_id = current_user._get_current_object().id
            # pitch_id = current_user._get_current_object().id
            comment = Comments(user_id=user_id, body=body)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('main_blueprint.pitches', comment =comment))
    return render_template("new_comment.html", form = form )



    
        
