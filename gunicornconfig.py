  
import os
from gevent import monkey

monkey.patch_all()
import multiprocessing
debug = False
pidfile = "gunicorn.pid"

accesslog = os.path.abspath(os.path.join(os.getcwd(), "logs/gunicorn.log"))
# accesslog = "/mnt/d/1-M2-S2/3-tech-web/logs/gunicorn.log"
workers = multiprocessing.cpu_count()*2+1
workers_class = "gevent"
deamon = True