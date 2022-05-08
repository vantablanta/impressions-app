from . import auth_blueprint
from flask import render_template
from ..main.forms import LoginForm

@auth_blueprint.route('/login')
def login():
    form = form
    return render_template('auth/login.html', form =form)