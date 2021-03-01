  
import os
from gevent import monkey

monkey.patch_all()
import multiprocessing
debug = False
pidfile = "gunicorn.pid"
workers = multiprocessing.cpu_count()*2+1
workers_class = "gevent"
deamon = True