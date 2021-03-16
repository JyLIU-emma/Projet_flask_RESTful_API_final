from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from backend.api_sep import app as back
# from frontend.app import app as front


back

if __name__=='__main__':
    back.run(host='0.0.0.0', port=5000, use_evalex=True,
                  use_reloader=True, use_debugger=True)