from flask import Flask, request, flash, url_for, redirect, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import json
from passlib.apps import custom_app_context as pwd_context
from flask_login import UserMixin, LoginManager, logout_user, login_required


__all__ = ["User", 'fr', 'db', 'DB_DATA', "load_data", 'load_user', 'login_manager', 'output_json']


login_manager = LoginManager()
login_manager.login_view = 'login_ep'

# Créer des chemins vers les bases de données
BACKEND = Path(__file__).parent.parent.parent
DATA = BACKEND / "data"
USERS_DATA = DATA / "users.json"
ADMINS_DATA = DATA / "admins.json"
DB_DATA = DATA / "locations.db"
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    cette classe lie le tableau "users" dans base de données et crée une instance de user
    """
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        """
        encrypter le mot de passe
        """
        self.password_hash = pwd_context.encrypt(password)
    def verify_password(self, password):
        """
        vérifier le mot de passe
        """
        return pwd_context.verify(password, self.password_hash)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def load_data(tablename):
    """
    cette fonction lit le fichier users.json et renvoie un dictionnaire de l'info de collaborateurs
    """
    if tablename == "users":
        with USERS_DATA.open() as f:
            data_dico = json.load(f)
    return data_dico

def output_json(data, header={}, code=200):
    head = {
            "project": "Techniques web - 2021",
            "license": "Creative Common 2.0",
            "Access-Control-Allow-Origin":"*"
        }
    headers = dict(head, **header)
    resp = Response(json.dumps(data), status=code, headers=headers,
                    content_type='application/json')
    return resp

class fr(db.Model):
    """
    cette classe lie le tableau "fr" dans base de données
    """
    geonameid = db.Column('geonameid', db.Integer, primary_key = True)
    name = db.Column(db.String)
    asciiname = db.Column(db.String)
    alternatenames = db.Column(db.String) 
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    feature_class = db.Column(db.String)
    feature_code = db.Column(db.String)
    country_code = db.Column(db.String)
    cc2 = db.Column(db.String)
    admin1_code = db.Column(db.Integer)
    admin2_code = db.Column(db.Integer)
    admin3_code = db.Column(db.Integer)
    admin4_code = db.Column(db.Integer)
    population = db.Column(db.Integer)
    elevation = db.Column(db.String)
    dem = db.Column(db.String)
    timezone = db.Column(db.String)
    modification_date = db.Column(db.String)

    def __init__(self, geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, admin3_code, admin4_code, population, elevation, dem,
    timezone, modification_date):
        self.geonameid = geonameid
        self.name = name
        self.asciiname = asciiname
        self.alternatenames = alternatenames
        self.latitude = latitude
        self.longitude = longitude
        self.feature_class = feature_class
        self.feature_code = feature_code
        self.country_code = country_code
        self.cc2 = cc2
        self.admin1_code = admin1_code
        self.admin2_code = admin2_code
        self.admin3_code = admin3_code
        self.admin4_code = admin4_code
        self.population = population
        self.elevation = elevation
        self.dem = dem
        self.timezone = timezone
        self.modification_date = modification_date