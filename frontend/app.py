# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_cors import CORS
# from .models.api_connect import home_page, user_create_page
from .resources import auth, home, location


bootstrap = Bootstrap()

class Config():
    SECRET_KEY = "geonames_2021_key"


def create_app():
    app_front = Flask(__name__)
    app_front.config.from_object(Config)
    bootstrap.init_app(app_front)
    CORS(app_front, supports_credentials=True)

    app_front.register_blueprint(auth.auth_bp)
    app_front.register_blueprint(home.home_bp)
    app_front.register_blueprint(location.place_bp)

    return app_front

app = create_app()

# app.secret_key = "jianying"


# def form():
#     # request: 请求对象  --> 获取请求方式、数据
#     if request.method == 'POST' :    # 判断请求方式

#         # 获取请求参数
#         name = request.form.get('nom')
#         password = request.form.get('password')
#         print(name)

#         if not all([name, password]):
#             # print("Not all field is filled.")
#             flash("请填写所有信息")
#         else:
#             return render_template('home.html')

#     if request.method == "GET" :
#         print(request.data)

#     return render_template('index.html')

# if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=8802, debug=True)