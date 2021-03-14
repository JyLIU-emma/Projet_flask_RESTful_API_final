import requests, base64
from flask import session
from requests.auth import HTTPBasicAuth
import json

"""
Connecter le frondend avec backend par librairie requests
"""

__all__ =['home_page', 'user_create_page', 'user_login_page','user_search_page', 'user_add_page','user_info_page','user_info_page_delete','user_info_page_change']

API_URL = "http://127.0.0.1:5000/api"
CREATE_USER = API_URL + "/admins/create"
USER_LOGIN = API_URL + "/admins/login"
USER_LOGOUT = API_URL + "/admins/logout"
USER_SEARCH = API_URL + "/geonames"
USER_ADD = API_URL + "/geonames/add"
USER_INFO = API_URL + "/geonames/{geonameid}"

def home_page(choice):
    params = {'choice': choice}
    req = requests.get(API_URL, params=params)
    return req.status_code, req.json()

def user_create_page(data):
    datas = dict(data)
    req = requests.post(CREATE_USER, data=datas)
    return req.status_code, req.json()

def user_login_page(data):
    datas = dict(data)
    resp = requests.post(USER_LOGIN, data=datas)
    print(resp.headers)
    return resp.status_code, resp.json()

def user_search_page(data):
    datas = dict(data)
    token = session['token']
    resp = requests.get(USER_SEARCH, params=datas, auth=HTTPBasicAuth(token, ''))
    return resp.json()

def user_add_page(data):
    datas = dict(data)
    token = session['token']
    resp = requests.post(USER_ADD, data=datas, auth=HTTPBasicAuth(token, ''))
    return resp.status_code, resp.json()

def user_info_page(geonameid):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session['token']
    resp = requests.get(URL_INFO, auth=HTTPBasicAuth(token, ''))
    return resp.status_code,resp.json()

def user_info_page_delete(geonameid):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session['token']
    resp = requests.delete(URL_INFO, auth=HTTPBasicAuth(token, ''))
    return resp.status_code, resp.json()

def user_info_page_change(geonameid):
    URL_INFO = USER_INFO.format(geonameid=geonameid)
    token = session['token']
    resp = requests.put(URL_INFO, auth=HTTPBasicAuth(token, ''))
    return resp.status_code, resp.json()

