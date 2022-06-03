from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login feito com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incoreta, tente novamente', category='error')
        else:
            flash('Email não existe', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Volte sempre!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        tipo = request.form.get('tipo')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email já cadastrado', category='error')
        elif len(email) < 7:
            flash('Email inválido', category='error')
        elif senha1 != senha2:
            flash('As senhas não são iguais', category='error')
        elif len(senha1) < 6:
            flash('Senha muito curta', category='error')
        else:
            if tipo == 'diarista':
                new_user = User(nome=nome, sobrenome=sobrenome, email=email,
                            password=generate_password_hash(senha1, method='sha256'), tipo=tipo, mostrar='true')
            else:
                new_user = User(nome=nome, sobrenome=sobrenome, email=email,
                            password=generate_password_hash(senha1, method='sha256'), tipo=tipo, mostrar='false')
            db.session.add(new_user)
            db.session.commit()
            flash('Conta criada com sucesso!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)
