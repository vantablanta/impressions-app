from flask import render_template, redirect, url_for
from . import auth_blueprint
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User



@auth_blueprint.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/register', methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name = form.name.data, email= form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        title = "New Account"
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)