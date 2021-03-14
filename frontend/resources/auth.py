from flask import Blueprint, render_template, request, flash, redirect, url_for
from frontend.models.api_connect import user_create_page, user_login_page


__all__ =['auth_bp', 'add_admin', 'login', 'logout']


auth_bp = Blueprint("auth", __name__, url_prefix='/admins')

@auth_bp.route('/create', methods=['GET', 'POST'])
def add_admin():
    if request.method == 'GET':
        return render_template('add.html')
    
    elif request.method == 'POST':
        username = request.form.get('username')
        userid = request.form.get('id')
        password = request.form.get('password')
        password2 = request.form.get('passwordconfirm')
        data = {'username':username, 'id': userid, 'password':password, 'passwordconfirm':password2}
        status_code, resp = user_create_page(data)
        if status_code != 201 :
            api_error = True
            msg = resp['message']
            flash(msg)
            return render_template('add.html', api_error=api_error, msg=msg)
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
            api_error = True
            msg = resp['message']
            flash(msg)
            return render_template('login.html', api_error=api_error, msg=msg)
        else:
            return redirect(url_for('locations.search_results_page'))

@auth_bp.route('/logout', methods=['GET'])
def logout():
    status_code, resp = user_logout()


# @app.route('/', methods=['GET'])
# def home():
#     # choice = request.args.get("choice")
#     message = home_page()
#     return render_template('index.html', msg=message)