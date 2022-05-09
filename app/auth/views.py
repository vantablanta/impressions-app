from flask import render_template, redirect, url_for, flash, request
from . import auth_blueprint
from .forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from .. import db
from ..models import User
from ..email import mail_message


@auth_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main_blueprint.home'))
        flash('Invalid username or Password', "danger")
    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        flash("You have successfully created an acount", "success")
        db.session.add(user)
        db.session.commit()
        # mail_message("Welcome to Impressions","email/welcome",user.email,user=user)
        return redirect(url_for('auth_blueprint.login'))
    return render_template('auth/register.html', form=form)



@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_blueprint.home"))
