heroku login
heroku create flask-geonames-projet-backend
heroku addons:create heroku-postgresql:hobby-dev

gunicorn -c gunicornconfig.py main:app

heroku local:run flask run

# in .env
FLASK_APP=main.py


heroku local
#in Procfile
web: gunicorn -c gunicornconfig.py main:app