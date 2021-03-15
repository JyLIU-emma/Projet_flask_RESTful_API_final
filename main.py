from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from backend.api import app as back
from frontend.app import app as front
# from werkzeug.middleware.dispatcher import DispatcherMiddleware

# application = DispatcherMiddleware(front, back)
application = DispatcherMiddleware(front, {
    '/api': back
})

app = Flask(__name__)
app.wsgi_app = application

if __name__=='__main__':
    from os import environ
    app.run(host='0.0.0.0', port=environ['PORT'], use_evalex=True,
                  use_reloader=True, use_debugger=True)
