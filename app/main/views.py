from . import main_blueprint
from flask import render_template
from .forms import RegisterForm
# from flask_login import login_required


@main_blueprint.route('/')
def home():
    form = RegisterForm()
    return render_template('index.html', form=form)


@main_blueprint.route('/pitches')
def pitches():
    pitches = [
        {
            'poster': "Michelle",
            "category": "Random",
            "body": "Like it and leav it",
            "upvotes": 8,
            "downvotes": 0
        },
        {
            'poster': "Avana",
            "category": "Cars",
            "body": "Like it and leav it",
            "upvotes": 8,
            "downvotes": 0
        },
        {
            'poster': "Butile",
            "category": "Crabs",
            "body": "Like it and leav it",
            "upvotes": 8,
            "downvotes": 0
        },
        {
            'poster': "Bankok",
            "category": "Cake",
            "body": "Like it and leav it",
            "upvotes": 8,
            "downvotes": 0
        },
        {
            'poster': "Bamudo",
            "category": "Health",
            "body": "Like it and leav it",
            "upvotes": 8,
            "downvotes": 0
        },
    ]
    return render_template('pitches.html', pitches = pitches)
