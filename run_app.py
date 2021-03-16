from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# from backend.api import app as back
from frontend.app import app as front


front

if __name__=='__main__':
    front.run(host='0.0.0.0', port=8088, use_evalex=True,
                  use_reloader=True, use_debugger=True)