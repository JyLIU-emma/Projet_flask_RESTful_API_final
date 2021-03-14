# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash, session
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import UserMixin, LoginManager, logout_user, login_required
# from .models.api_connect import home_page, user_create_page
from .resources import auth, home, location

__all__ =['app']

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

class Config():
    SECRET_KEY = "geonames_2021_key"


def create_app():
    app_front = Flask(__name__)
    app_front.config.from_object(Config)
    bootstrap.init_app(app_front)
    # CORS(app_front, supports_credentials=True)

    app_front.register_blueprint(auth.auth_bp)
    app_front.register_blueprint(home.home_bp)
    app_front.register_blueprint(location.place_bp)

    return app_front

app = create_app()
#########################################################
app.app_context().push()
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
#########################################################
# app.secret_key = "jianying"

# @app.before_request
# def load_user():
#     if session["user"]:
#         user = User.query.filter_by(username=session["user_id"]).first()
#     else:
#         user = {"name": "Guest"}  # Make it better, use an anonymous User instead

#     g.user = user

# if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=8802, debug=True)