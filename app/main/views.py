from . import main_blueprint
from flask import render_template
from .forms import RegisterForm
from flask_login import login_required
from ...data import pitches


@main_blueprint.route('/')
def home():
    form  = RegisterForm()
    return render_template('index.html', form = form)

@main_blueprint.route('/pitches')
def pitches():
    return render_template('pitches.html', pitches = pitches)