from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, logout_user, current_user
from .auth import auth


configs = Blueprint('configs', __name__)


@configs.route('/config')
@login_required
def config():
    return render_template("config.html", user=current_user)


@configs.route('/config/changepassword', methods=['GET', 'POST'])
@login_required
def changepassword():
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        newpassword = request.form.get('newpassword')
        newpasswordconf = request.form.get('newpasswordconf')

        user = current_user
        if not check_password_hash(user.password, oldpassword):
            flash('Senhas atuais são diferentes.', category='error')
        elif oldpassword == newpassword:
            flash('As senhas são iguais.', category='error')
        elif len(newpassword) < 6:
            flash('Senha muito curta', category='error')
        elif newpassword != newpasswordconf:
            flash('Senhas novas são diferentes.', category='error')
        else:
            user.password = generate_password_hash(newpassword, method='sha256')
            db.session.commit()
            logout_user()
            flash('Senha alterada com sucesso!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("changepassword.html", user=current_user)
