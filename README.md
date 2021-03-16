# Projet-techweb

use flask to create a RESTful Api

## Explication du repository

- `main.py` : programme principale pour lancer l'app
- dans `backend` :
    program principal: api.py

    L'apidoc est dans son sous-répertoire `static\index.html`

- dans `frontend` :
    program principal: app.py

- `api.conf` : fichier de configuration nginx pour l'api
- `config.py` : exemple de fichier de configuration pour gunicorn
- `gunicornconfig.py` : fichier de configuration finalement utiliser pour le déploiement sur Heroku de l'api
- `equipe.txt` : Expliquer la répartition de tâches
- `guni_run` : nécessaire pour le lancement séparé de frontend et backend avec gunicorn
- `run_api.py` et `run_app.py` : les programs principaux pour le lancement séparé

## Explication du teste local

- Manière 1:
    dans le répertoire le plus haut, lancer:
    `$ python main.py`

    Et puis consulter l'app dans http://127.0.0.1:5000/

- Manière 2:
    dans le répertoire le plus haut, avec 2 terminals, lancer séparément en même temps:
    ```bash
    # terminal 1
    $ gunicorn -c gunicornconfig_back.py run_api:back

    # terminal 2
    $ gunicorn -c gunicornconfig_front.py run_app:front
    ```

    Pour consulter le frontend, allez à http://127.0.0.1:8088
    Pour consulter le backend, allez à http://127.0.0.1:5000/api

- un compte déjà créé pour effectuer les tests:

    - username: Jianying
    - ID: 006
    - Password: 12345
    **Attention: chaque token expirera dans 10 minutes, après, il faut se reconnecter**



## Manuel technique (suite) : Déploiement sur Heroku

**Système utilisé: Ubuntu (wsl)**

#### Avant de commencer le déploiement, heroku exige que l'app est stocké sous forme de git repository. Initier git dans le plus haut niveau de votre app (répertoire du programme principale). 

**Structure d'exemple:**

```
|-- repository_name
    |-- .git
    |-- logs
    |   |-- gunicorn.log
    |-- README.md
    |-- .env
    |-- Procfile
    |-- .gitignore
    |-- gunicornconfig.py
    |-- LICENSE
    |-- main.py
    |-- README.md
    |-- requirements.txt
    |-- backend
        |-- api.py
        |-- __init__.py
        |-- resources
        |-- data
             ...

```

#### En plus, le fichier `requirements.txt` est également obligatoire. Pour le construire:
```bash
$ pip freeze > requirements.txt
```

### 1. Créer un compte sur le site officiel [Heroku](https://signup.heroku.com/login)

Les opérations suivantes sont toutes faites dans le terminal.

### 2. Télécharger Héroku

```bash
$ curl https://cli-assets.heroku.com/install.sh | sh
```

### 3. Login Heroku dans Terminal

```bash
$ heroku login
```
Une fenêtre va s'ouvrir dans votre navigateur après avoir lancé cette commande.

### 4. Créer votre application

```bash
$ heroku create <nom-de-votre-app>

# exemple:
$ heroku create flask-geonames-projet-backend
```

**Attention: le nom de votre app ne doit pas être utilisé avant.**

### 5. Lier votre app à la base de données fournie par Héroku

```bash
$ heroku addons:create heroku-postgresql:hobby-dev
```

Heroku permet d'utiliser les base de données *Postgres*, il y a certaines limites pour les compte gratruit, pour vérifier les limites/avoir un tuto plus détaillé, veuillez consulter le [site officiel](https://devcenter.heroku.com/articles/heroku-postgresql).

### Étape optionnelle
Pour sécuriser votre app, on doit d'abord reconfigurer `SECRET_KEY` avec variable d'environnement：
`$ heroku config:set SECRET_KEY=random_string_genere`

Astuce: pour générer un string aléatoire :
`$ python -c "import uuid; print(uuid.uuid4().hex)"`

Deuxièmement, si on veut changer de HTTP à HTTPS, deux autres extension/outil sont nécessaires: `Flask-SSLify` et `ProxyFix`.

Partie rajoutée (sur la configuration de l'app) pour réaliser ce but:

```python
# fichier: api.py
# redirect to HTTPS
app.config['SSL_REDIRECT'] = True if os.environ.get('DYNO') else False
if app.config['SSL_REDIRECT']:
    from flask_sslify import SSLify
    sslify = SSLify(app)

    # cette ligne ne marche pas:
    # from werkzeug.contrib.fixers import ProxyFix
    # Utiliser Werkzeug version 1.0.0 et puis importer avec ligne suivante
    # Pour en savoir plus: https://github.com/Azure-Samples/ms-identity-python-webapp/issues/16
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
```


### 6. Tester l'app dans gunicorn avec un fichier de configuration

**Attention: À part ce test, il y a encore 3 manières pour lancer l'app. Il vaux mieux de tous tester, même si l'app marche dans une manière, cela ne signifie pas qu'il marche dans tous les cas.**

```bash
$ gunicorn -c fichier_config.py nom_du_programme_principal:nom_de_app_dans_fichier

# exemple
$ gunicorn -c gunicornconfig.py main:app

```
**Contenu dans gunicornconfig.py**

```python
import os
from gevent import monkey

monkey.patch_all()
import multiprocessing
debug = False
pidfile = "gunicorn.pid"

# il faut d'abord créer le fichier dans ce chemin, et puis cette ligne permet de stocker les infos de connection dans "gunicorn.log"

# Attention: le nom du fichier doit être identique

accesslog = os.path.abspath(os.path.join(os.getcwd(), "logs/gunicorn.log"))
workers = multiprocessing.cpu_count()*2+1
workers_class = "gevent"
deamon = True
```

**Contenu dans main.py**

```python
from flask import Flask
from backend.api import app

app

if __name__=='__main__':
    app.run(debug=True)
```

#### Méthode 1

```bash
$ python main.py
```

#### Méthode 2

```bash
$ export FLASK_APP=main.py

$ flask run

# donner un port
$ flask run -p 8088
```

#### Méthode 3

```bash
# tester avec gunicorn sans fichier de configuration
$ gunicorn main:app
# gunicorn run_app:front

# spécifier un autre port si on veut voir l'effet de gunicorn
$ gunicorn main:app -b 0.0.0.0:2021
```

Après avoir vérifié l'app marche dans tous les cas, vous pouvez continuer à faire tester avec "heroku local".

### 7. Un seul lancement pour tester

```bash
$ heroku local:run flask run
```

Mais cette ligne demande un fichier `.env`, dans la quelle on donne des variables d'environnement, exemple du contenu de ce fichier: (1ère ligne obligatoire(c'est suffit pour cette app), les suivants est à votre choix selon votre app)

```
FLASK_APP=main.py
FLASK_CONFIG=heroku
MAIL_USERNAME=<your-gmail-username>
MAIL_PASSWORD=<your-gmail-password>
```
**Attention: ce fichier contient des infos confidentiels, donc il faut l'ajouter dans `.gitignore`**

### 8. 2e test avec heroku

```
heroku local
```

Cette ligne demande un autre fichier spécifique, nommé `Procfile` **(fixé, sans extension)**, dans la quelle:

```
web: gunicorn -c gunicornconfig.py main:app 
```

Pour lancer l'app, sa formule est:
`web: ligne_de_commande`

On peut également écrit comme:
`web: gunicorn main:app`


### 9. Pusher au heroku

Après avoir vérifié que tout est bon et passé des tests locaux, vous pourrez maintenant pucher votre app sur heroku.

```bash
$ git push heroku master

...
remote: Verifying deploy... done.
To https://git.heroku.com/flask-geonames-projet-backend.git
* [new branch]      master -> master
```

L'info en bas montre que le push a réussi.

Vous pouvez maintenant consulter votre app en ligne.

**Astuces:**
En cas d'oublier l'adresse de vos apps:
```bash
$ git remote show heroku
```

Vérifier tous les noms de apps du compte
```bash
$ heroku apps
```

Vérifier tous les releases de l'app (dans son répertoire)
```bash
$ heroku releases
```


Si malheureusement vous rencontrez des erreurs, vous pouvez consulter les logs avec:
```bash
$ heroku logs
``` 
ou 
```bash
$ heroku logs --tail
```

Référence:
Un manuel chinois: [Heroku 使用教程](https://www.jianshu.com/p/7bc34e56fa39)
Flask Web Development, 2nd Edition, by Miguel Grinberg(O’Reilly). Copyright 2018 Miguel Grinberg, 978-1-491-99173-2