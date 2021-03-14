import requests
import json

API_URL = "http://127.0.0.1:5000/api"
CREATE_USER = API_URL + "/admins/create"
USER_LOGIN = API_URL + "/admins/login"

dico = {'username':'Jianying', 'id':'006', 'password':'12345'}
r = requests.post(USER_LOGIN, data=dico)
print(r.text)
print(r.json())