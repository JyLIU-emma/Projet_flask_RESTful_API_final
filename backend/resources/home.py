from flask import Flask, request, redirect, url_for
from flask_restful import Resource, Api

__all__ =['Home']

"""
route de cette ressource:
'/', '/home'
"""

class Home(Resource):
    """
    avoir un seul méthode : GET
    selon les données fournies, cette page va reorienter vers la page de login ou la page de création du compte
    """
    def get(self):
        choice = request.args.get('choice')
        if choice == 'login':
            return redirect(url_for('login_ep'))
        elif choice == 'create':
            return redirect(url_for('admincreate_ep'))
        return {'message':'home page'}