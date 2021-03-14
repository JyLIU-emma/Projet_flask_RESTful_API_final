from flask import Blueprint, render_template, request, flash, redirect, url_for
from frontend.models.api_connect import home_page, user_search_page, user_add_page, user_info_page, user_info_page_delete, user_info_page_change

__all__ =['place_bp', 'search_results_page', 'add_location_page', 'one_location_page']

place_bp = Blueprint("locations", __name__, url_prefix="/geonames")

@place_bp.route('/', methods=['GET'])
def search_results_page():
    if request.method == 'GET':
        city = request.args.get('name')
        data = {'name' : city}
        results = user_search_page(data)
        return render_template('chercher.html', city=city, results=results)


@place_bp.route('/add', methods=['GET', 'POST'])
def add_location_page():
    if request.method == 'GET':
        return render_template('ajouter.html')

    elif request.method == 'POST':
        geonameid = request.form.get('geonameid')
        name = request.form.get('name')
        asciiname = request.form.get('asciiname') 
        alternatenames = request.form.get('alternatenames')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        feature_class = request.form.get('feature_class')
        feature_code = request.form.get('feature_code')
        country_code = request.form.get('country_code')
        cc2 = request.form.get('cc2')
        admin1_code = request.form.get('admin1_code')
        admin2_code = request.form.get('admin2_code')
        admin3_code = request.form.get('admin3_code')
        admin4_code = request.form.get('admin4_code')
        population = request.form.get('population')
        elevation = request.form.get('elevation')
        dem = request.form.get('dem')
        timezone = request.form.get('timezone')
        modification_date = request.form.get('modification_date')

        data = {"geonameid":geonameid, "name":name, "asciiname":asciiname, "alternatenames":alternatenames, "latitude":latitude, \
               "longitude":longitude, "feature_class":feature_class, "feature_code":feature_code, "country_code":country_code, "cc2":cc2, "admin1_code":admin1_code, "admin2_code":admin2_code, \
                "admin3_code":admin3_code, "admin4_code":admin4_code, "population":population, "elevation":elevation, "dem":dem, "timezone":timezone, "modification_date":modification_date}
        
        status_code, resp = user_add_page(data)
        if status_code != 201:
            api_error = True
            msg = resp['message']
            flash(msg)
            return render_template('ajouter.html', api_error=api_error, msg=msg)
        else:
            msg = resp['message']
            api_success = True
            flash(msg)
            return render_template('ajouter.html', api_success = api_success, msg=msg)
            
@place_bp.route('/<geonameid>', methods=['GET', 'POST'])
def one_location_page(geonameid):
    if request.method == 'GET':
        status_code, results = user_info_page(geonameid)
        if status_code == 404 :
            api_error = True
            msg = results['message']
            flash(msg)
            return render_template('location.html',api_error=api_error, msg=msg)
        else:
            return render_template('location.html', results = results)
    
    elif request.method == 'POST':
        choice = request.form.get('choice')
        
        if choice == "Supprimer":
            status_code, results = user_info_page_delete(geonameid)
            if status_code == 404 :
                api_error = True
                msg = results['message']
                flash(msg)
                return render_template('location.html', results = results, api_error = api_error, msg=msg)
            elif status_code == 200:
                api_success = True
                msg = results['message']
                flash(msg)
                return render_template('location.html', results = results, api_success = api_success, msg=msg)

        elif choice == "Modifier":
            status_code, results = user_info_page_change(geonameid)
            resultat = user_info_page(geonameid)[1]
            if status_code == 404 :
                api_error = True
                msg = results['message']
                flash(msg)
                return render_template('location.html', results = resultat, api_error = api_error, msg=msg)
            elif status_code == 200:
                api_success = True
                msg = results['message']
                flash(msg)
                return render_template('location.html', results = resultat, api_success = api_success, msg=msg)

