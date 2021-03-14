import requests
import json

API_URL = "http://127.0.0.1:5000/api"
CREATE_USER = API_URL + "/admins/create"
USER_LOGIN = API_URL + "/admins/login"

def home_page(choice):
    params = {'choice': choice}
    req = requests.get(API_URL, params=params)
    # print(req.headers)
    # req_json = req.json()
    # return req_json['message']
    return req.status_code, req.json()

def user_create_page(data):
    data = dict(data)
    # req = requests.get(CREATE_USER, timeout=30)
    req = requests.post(CREATE_USER, json=data)
    # print(req.content)
    # print(req.headers)
    # return req_json['message']
    return req.status_code, req.json()

def user_login_page(data):
    datas = dict(data)
    print("#########datas##############")
    print(datas)
    # req = requests.post(USER_LOGIN, data=datas, headers={'Content-Type':'application/json'})
    dico = {'username':'Jianying', 'id':'006', 'password':'12345'}
    print("#########dico##############")
    print(dico)
    r = requests.post(USER_LOGIN, data=datas)
    # print(req)
    # print(req.content)
    # print(req.headers)
    print(r.json())
    return r.status_code, r.json()

# payload = {'username':'Jianying', 'id':'006', 'password':'12345'}
# r = requests.post(CREATE_USER, data=payload)
# print(r.text)

    # print(req_json['message'])
    # print(req_json)
    # print(req.headers)