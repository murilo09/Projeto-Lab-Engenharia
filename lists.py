from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import User
from . import db


lists = Blueprint('diaristas', __name__)


@lists.route('/diaristas')
@login_required
def diaristas():
    users=User.query.filter_by(tipo='diarista').all()
    return render_template("diaristas.html", user=current_user, users=users)
