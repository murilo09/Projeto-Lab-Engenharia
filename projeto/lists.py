from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import User
from . import db


lists = Blueprint('diaristas', __name__)


@lists.route('/diaristas', methods=['GET', 'POST'])
@login_required
def diaristas():
    users = User.query.filter_by(tipo='diarista').all()
    if request.method == 'POST':
        idUser = user.id
    return render_template("diaristas.html", user=current_user, users=users)
