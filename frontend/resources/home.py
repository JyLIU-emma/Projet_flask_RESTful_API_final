from flask import Blueprint, render_template, request, redirect, url_for
from frontend.models.api_connect import home_page
from .auth import auth_bp

home_bp = Blueprint("home", __name__)



@home_bp.route('/', methods=['GET'], endpoint='home')
def index():
    choice = request.args.get('choice')
    if choice == None:
        status_code, msg = home_page(choice)
        return render_template('index.html', msg=msg['message'])
    
    if choice == "créer un compte":
        return redirect(url_for('auth.add_admin'))
    elif choice == "Login":
        return redirect(url_for('auth.login'))  ########################33
    
    # if status_code
    # print(status_code)
    # print(msg)
    