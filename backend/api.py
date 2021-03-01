from flask import Flask, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from pathlib import Path
from .resources import *
from flask_login import LoginManager
import os


app = Flask(__name__)
app.secret_key = '23rfqssjmnkcj'   # random string， top secret

# configuration de l'app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(DB_DATA)
app.config['SECRET_KEY'] = "random_string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

#redirect to HTTPS
app.config['SSL_REDIRECT'] = True if os.environ.get('DYNO') else False
if app.config['SSL_REDIRECT']:
    from flask_sslify import SSLify
    sslify = SSLify(app)

    from Werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

# initier les module pour login_manager et database
login_manager.init_app(app)
db.init_app(app)
api = Api(app)

api.add_resource(Home, '/', '/home', endpoint='home_ep')    #pade d'accueil GET
api.add_resource(Login, '/admins/login', endpoint='login_ep')  #se connecter GET POST
api.add_resource(Logout, '/admins/logout', endpoint='logout_ep') # déconnecter  GET
api.add_resource(CreateAdmin, '/admins/create', endpoint='admincreate_ep')  #s'inscrire GET POST
api.add_resource(AddPlace, '/geonames/add', endpoint='place_add') #GET     POST add info
api.add_resource(SearchPlaces, '/geonames', endpoint='db_ep')   # GET
api.add_resource(PlaceInfoPage, '/geonames/<geonameid>', endpoint='placeinfo_ep')  # info de chaque endroit GET PUT DELETE


if __name__ == '__main__':
    app.run(debug=True)

    