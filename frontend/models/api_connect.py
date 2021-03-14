import requests
import json

API_URL = "http://127.0.0.1:5000/api"
CREATE_USER = API_URL + "/admins/create"
USER_LOGIN = API_URL + "/admins/login"
USER_LOGOUT = API_URL + "/admins/logout"

def home_page(choice):
    params = {'choice': choice}
    req = requests.get(API_URL, params=params)
    # print(req.headers)
    # req_json = req.json()
    # return req_json['message']
    return req.status_code, req.json()

def user_create_page(data):
    datas = dict(data)
    req = requests.post(CREATE_USER, data=datas)
    # print(req.json())
    return req.status_code, req.json()

def user_login_page(data):
    datas = dict(data)
    resp = requests.post(USER_LOGIN, data=datas)
    # print(req)
    # print(req.content)
    # print(req.headers)
    # print(resp.json())
    return resp.status_code, resp.json()

# payload = {'username':'Jianying', 'id':'006', 'password':'12345'}
# r = requests.post(CREATE_USER, data=payload)
# print(r.text)

    # print(req_json['message'])
    # print(req_json)
    # print(req.headers)