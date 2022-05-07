from . import main_blueprint
from flask import render_template
from .forms import RegisterForm


@main_blueprint.route('/')
def home():
    form  = RegisterForm()
    return render_template('index.html', form = form)