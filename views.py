from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def mainpage():
    return render_template("main.html", user=current_user)


@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/diaristas')
@login_required
def diaristas():
    return render_template("diaristas.html", user=current_user)
