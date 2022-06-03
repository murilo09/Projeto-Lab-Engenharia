from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    sobrenome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    tipo = db.Column(db.String(10))
    mostrar = db.Column(db.String(10))

class Contratados(db.Model, UserMixin):
    idcont = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer)
    idDiarista = db.Column(db.Integer)