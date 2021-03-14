from flask import Blueprint, render_template, request, flash, redirect, url_for
from frontend.models.api_connect import user_create_page, user_login_page

auth_bp = Blueprint("auth", __name__, url_prefix='/admins')

@auth_bp.route('/create', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'GET':
        # return render_template('createAdmin.html')
        return render_template('add1.html')
    
    elif request.method == 'POST':
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')
        password2 = request.form.get('passwordconfirm')
        data = {'username':username, 'userid': userid, 'password':password, 'passwordconfirm':password2}
        # print(data)
        status_code, resp = user_create_page(data)
        if status_code != 201 :
            print(resp)
            api_error = True
            msg = resp['message']
            flash(msg)
            return render_template('add1.html', api_error=api_error, msg=msg)
        else:
            return redirect(url_for('auth.login'))

    

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')
        data = {"username":username, "id":userid, "password":password}
        status_code, resp = user_login_page(data)

        if status_code != 200:
            return resp
        else:
            print(resp)
            return "welcome, "+ resp['username']


# @app.route('/', methods=['GET'])
# def home():
#     # choice = request.args.get("choice")
#     message = home_page()
#     return render_template('index.html', msg=message)