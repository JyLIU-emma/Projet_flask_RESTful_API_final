# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash, session
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from datetime import  timedelta
from .resources import auth, home, location

__all__ =['app']

bootstrap = Bootstrap()

class Config():
    SECRET_KEY = "geonames_2021_key"
    PERMANENT_SESSION_LIFETIME =  timedelta(hours=1)


def create_app():
    app_front = Flask(__name__)
    app_front.config.from_object(Config)
    bootstrap.init_app(app_front)

    app_front.register_blueprint(auth.auth_bp)
    app_front.register_blueprint(home.home_bp)
    app_front.register_blueprint(location.place_bp)

    return app_front

app = create_app()
app.app_context().push()
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8802, debug=True)