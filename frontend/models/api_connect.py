import requests
from flask import session
from requests.auth import HTTPBasicAuth
import json

"""
Connecter le frondend avec backend par librairie requests
"""

__all__ =['home_page', 'user_create_page', 'user_login_page','user_search_page', 'user_add_page','user_info_page','user_info_page_delete','user_info_page_change']

API_URL = "http://0.0.0.0:5000/api"

# pour le déploiement du Heroku, utilise URL suivant:
# API_URL = "https://flask-geonames-projet-backend.herokuapp.com/"

CREATE_USER = API_URL + "/admins/create"
USER_LOGIN = API_URL + "/admins/login"
USER_LOGOUT = API_URL + "/admins/logout"
USER_SEARCH = API_URL + "/geonames"
USER_ADD = API_URL + "/geonames/add"
USER_INFO = API_URL + "/geonames/{geonameid}"

def home_page(choice):
    params = {'choice': choice}
    req = requests.get(API_URL, params=params)
    
    # utiliser avec PERMANENT_SESSION_LIFETIME dans config
    # pour la fermeture automatique d'une session dans 1 heure
    sess = requests.session()
    sess.keep_alive = False

    return req.status_code, req.json()

def user_create_page(data):
    datas = dict(data)
    req = requests.post(CREATE_USER, data=datas)
    sess = requests.session()
    sess.keep_alive = False
    return req.status_code, req.json()

def user_login_page(data):
    datas = dict(data)
    resp = requests.post(USER_LOGIN, data=datas)
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

def user_search_page(data):
    datas = dict(data)
    token = session.get('token')
    resp = requests.get(USER_SEARCH, params=datas, auth=HTTPBasicAuth(token, ''))
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

def user_add_page(data):
    datas = dict(data)
    token = session.get('token')
    resp = requests.post(USER_ADD, data=datas, auth=HTTPBasicAuth(token, ''))
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

def user_info_page(geonameid):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session.get('token')
    resp = requests.get(URL_INFO, auth=HTTPBasicAuth(token, ''))
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

def user_info_page_delete(geonameid):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session.get('token')
    resp = requests.delete(URL_INFO, auth=HTTPBasicAuth(token, ''))
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

def user_info_page_change(geonameid, data):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session.get('token')
    resp = requests.put(URL_INFO, data=data, auth=HTTPBasicAuth(token, ''))
    sess = requests.session()
    sess.keep_alive = False
    return resp.status_code, resp.json()

