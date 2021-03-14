from flask import Flask, request, url_for, redirect, session, flash, jsonify, abort
import json
from flask_login import login_user, logout_user, login_required
import os
from flask_restful import Resource, Api
from passlib.apps import custom_app_context as pwd_context

from .lib.utils import *


__all__ =['Login', 'CreateAdmin', 'Logout']

# importer l'info des collaborateurs stockée dans "users.json"
false = False
true = True
users = load_data('users')

"""
route de cette page:
/admins/add
"""


class Login(Resource):
    """
    route : /admins/login
    """
    def get(self):
        return {'message' : 'login page'}
    
    def post(self):
        """
        cette méthode 
        1) vérifie d'abord l'intégralité des infos (nom, id et mot de passe);
        2) comparé l'entrée avec l'info stocké dans db
        3) mémoriser l'user dans session
        """
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')

        if not all([username, password, userid]):
            msg = "Rempliez tous les champs, s'il vous plaît!"
            return output_json({"massage" : msg}, code=400)

        user = User.query.filter_by(id = userid).first()
        if not user or not user.verify_password(password) or not username == user.username:
            msg = "Verifiez votre nom, votre id ou votre mot de passe, s'il vous plaît !"
            return output_json({"massage" : msg}, code=400)
        else:
            login_user(user)
            return output_json({'username': username}, code=200)
            # return {'username': username}, 200
        

class Logout(Resource):
    """
    route : /admins/logout
    """
    @login_required
    def get(self):
        """
        cette méthode supprime l'info stocké dans session et réoriente vers la page d'accueil
        """
        logout_user()
        return redirect(url_for('home_ep'))


class CreateAdmin(Resource):
    """
    route: /admins/create
    """
    def get(self):
        return output_json({'message': 'page de création du compte'}, code=200)
    
    def post(self):
        """
        cette méthode va créer une entrée de user dans le tableau "users" du db "locations.db":
        1) reccueillit les infos remplies dans cette page;
        2) teste tous les infos
        3) écrit dans le db
        4) renvoie un message indiquant le résultat de l'opération
        """
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')
        password2 = request.form.get('passwordconfirm')

        if not all([username, userid, password, password2]):
            return output_json({'massage':"Veuillez remplir tous les champs."}, code=400) #missing arguments
        elif userid not in users.keys():
            return output_json({'massage':"Désolée, vous n'êtes pas notre collaborateur, vous ne pouvez pas créer un compte."}, code=400)
        elif User.query.filter_by(username = username).first() is not None:
            return output_json({'massage':"Vous avez déjà un compte."}, code=400) #existing user
        elif username != users[userid]["nom"] :
            return output_json({'massage':"Votre id ne conforme pas à votre nom. "}, code=400)
        elif password != password2 :
            return output_json({'massage':"Les deux mots de passe remplis doivent être identiques."}, code=400)

        user = User(username = username, id = userid)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        msg = "Votre compte admin a bien été créé."
        return output_json({"massage" : msg}, code=201)