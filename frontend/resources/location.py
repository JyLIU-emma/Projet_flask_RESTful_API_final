from flask import Blueprint, render_template, request
from frontend.models.api_connect import home_page

place_bp = Blueprint("locations", __name__, url_prefix="/geonames")


@place_bp.route('/', methods=['GET'])
def search_results_page():
    if request.method == 'GET':
        city = request.args.get('name')
        if city == None:
            return render_template('chercher.html')
        else:
            return render_template('chercher.html', city=city)

@place_bp.route('/add', methods=['GET', 'POST'])
def add_location_page():
    # choice = request.args.get("choice")
    message = home_page()
    return render_template('index.html', msg=message)

@place_bp.route('/<geonameid>', methods=['GET', 'POST', 'DELETE'])
def one_location_page(geonameid):
    # choice = request.args.get("choice")
    message = home_page()
    return render_template('index.html', msg=message)
