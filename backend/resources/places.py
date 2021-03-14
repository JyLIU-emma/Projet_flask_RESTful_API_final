from flask import Flask, request, jsonify, redirect, url_for
from flask_restful import Resource, Api
from flask_login import login_required
import json
from .lib.utils import *

__all__ =['AddPlace', 'SearchPlaces', 'PlaceInfoPage']


# lister tous les infos à recueillir
info_list = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', \
            'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 'dem', 'timezone', 'modification_date']

class AddPlace(Resource):
    # @login_required
    @auth.login_required
    def get(self):
        """
        @api {get} https://home/geonames/add /geonames/add : Méthode GET
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription obtenir une liste d'inforamtions à remplir pour une location.

        @apiParam {int} geonameid      
        @apiParam {String} name   
        @apiParam {String} asciiname    
        @apiParam {String} alternatenames     
        @apiParam {Float} latitude   
        @apiParam {Float} longitude    
        @apiParam {String} feature_class      
        @apiParam {String} feature_code    
        @apiParam {String} country_code    
        @apiParam {String} cc2      
        @apiParam {int} admin1_code    
        @apiParam {int} admin2_code    
        @apiParam {int} admin3_code    
        @apiParam {int} admin4_code      
        @apiParam {int} population    
        @apiParam {String} elevation  
        @apiParam {String} dem    
        @apiParam {String} timezone  
        @apiParam {String} modification_date    

        @apiParamExample {json} Success-Response:
        {
            "infolist": [
                "geonameid",
                "name",
                "asciiname",
                "alternatenames",
                "latitude",
                "longitude",
                "feature_class",
                "feature_code",
                "country_code",
                "cc2",
                "admin1_code",
                "admin2_code",
                "admin3_code",
                "admin4_code",
                "population",
                "elevation",
                "dem",
                "timezone",
                "modification_date"
            ]
        }
        """
        return {'infolist':info_list}

    # @login_required
    @auth.login_required
    def post(self):
        """

        @api {post} https://home/geonames/add /geonames/add : Méthode POST
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription ajouter les informations pour une location.

        @apiParam {int} geonameid      
        @apiParam {String} name    
        @apiParam {String} asciiname    
        @apiParam {String} alternatenames     
        @apiParam {Float} latitude   
        @apiParam {Float} longitude    
        @apiParam {String} feature_class      
        @apiParam {String} feature_code    
        @apiParam {String} country_code    
        @apiParam {String} cc2      
        @apiParam {int} admin1_code    
        @apiParam {int} admin2_code    
        @apiParam {int} admin3_code    
        @apiParam {int} admin4_code      
        @apiParam {int} population    
        @apiParam {String} elevation  
        @apiParam {String} dem    
        @apiParam {String} timezone  
        @apiParam {String} modification_date    
        
        @apiParamExample {json} Request-Example:
        {
            "Geoname ID": "2968815",
            "Name": "Paris",
            "Ascii Name": "Paris",
            "Alternate Names": "Departement de Paris,Département de Paris,Parigi,Paris,Paris Department",
            "Latitude": "48.8534",
            "Longitude": "2.3486",
            "Feature class": "A",
            "Feature code": "ADM2",
            "Country code": "FR",
            "CC2": "FR",
            "Admin1 code": "11",
            "Admin2 code": "75",
            "Admin3 code": "13",
            "Admin4 code": "14",
            "Population": "2257981",
            "Elevation": "33443",
            "Dem": "35",
            "Timezone": "Europe/Paris",
            "Modification date": "2019-06-17"
        }

        @apiSuccess {int} geonameid      
        @apiSuccess {String} name    
        @apiSuccess {String} asciiname    
        @apiSuccess {String} alternatenames     
        @apiSuccess {Float} latitude   
        @apiSuccess {Float} longitude    
        @apiSuccess {String} feature_class      
        @apiSuccess {String} feature_code    
        @apiSuccess {String} country_code    
        @apiSuccess {String} cc2      
        @apiSuccess {int} admin1_code    
        @apiSuccess {int} admin2_code    
        @apiSuccess {int} admin3_code    
        @apiSuccess {int} admin4_code      
        @apiSuccess {int} population    
        @apiSuccess {String} elevation  
        @apiSuccess {String} dem    
        @apiSuccess {String} timezone  
        @apiSuccess {String} modification_date    

        @apiSuccessExample {json} Success-Response:  
        {
            "message": "Beijing(112233) est bien ajoutée dans la base de données."
        }

        @apiError info S'il y existes des champs incomplets, il renvoie un message d'erreur pour compléter tous les champs.

        @apiErrorExample {json} Error-Response:
        {
            "error": "Veuillez remplir tous les champs. "
        }
        """
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

        info = [geonameid, name, asciiname, alternatenames, latitude, \
            longitude, feature_class, feature_code, country_code, cc2, admin1_code, admin2_code, \
                admin3_code, admin4_code, population, elevation, dem, timezone, modification_date]
            
        if not all(info):
            msg = "****Veuillez remplir tous les champs. ****"
            return {"message":msg}
        else :
            location = fr(*info)
            db.session.add(location)
            db.session.commit()
            msg = '****{}({}) est bien ajoutée dans la base de données.****'.format(name, geonameid)
            return {"message":msg}, 201
        

class SearchPlaces(Resource):

    # @login_required
    @auth.login_required
    def get(self):
        """
        @api {get} https://home/geonames /geonames : Méthode GET
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription obtenir les informations principales d'une ou des location(s) en donnant un nom à rechercher.

        @apiParam {String} name nom de la location.   
        @apiParamExample {json} Request-Example:
        {
            "name": "Annecy"
        }

        @apiSuccess {int} geonameid      
        @apiSuccess {String} name      
        @apiSuccess {Float} latitude   
        @apiSuccess {Float} longitude  

        @apiSuccessExample {json} Success-Response:  
        {
            "3037540": {
                "geonameid": "3037540",
                "name": "Annecy-le-Vieux",
                "latitude": "45.91971",
                "longitude": "6.14393"
            },
            "3037541": {
                "geonameid": "3037541",
                "name": "Lac d'Annecy",
                "latitude": "45.85164",
                "longitude": "6.1767"
            },
            "3037542": {
                "geonameid": "3037542",
                "name": "Arrondissement d'Annecy",
                "latitude": "45.8907",
                "longitude": "6.17903"
            }
        }

        """

        city = request.args.get('name')
        geonameid = request.args.get('geoid')
        if geonameid != None:
            return redirect(url_for('placeinfo_ep', geonameid=geonameid))
            
        elif geonameid == None:
            if city is None:
                results = fr.query.all()
            else:
                results = fr.query.filter(fr.name.like("%" + city + "%") if city is not None else "").all()
            results_dico = {}
            for location in results:
                results_dico[location.geonameid] = {
                    'geonameid' : location.geonameid,
                    'name' : location.name,
                    'latitude' : location.latitude,
                    'longitude' : location.longitude
                }
            return jsonify(results_dico)


class PlaceInfoPage(Resource):
    # @login_required
    @auth.login_required
    def get(self, geonameid):
        """
        @api {get} https://home/geonames/<geonameid> /geonames/<geonameid> : Méthode GET
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription obtenir les informations détaillées d'une location en donnant l'identifiant(geonameid).

        @apiSuccess {int} geonameid      
        @apiSuccess {String} name    
        @apiSuccess {String} asciiname    
        @apiSuccess {String} alternatenames     
        @apiSuccess {Float} latitude   
        @apiSuccess {Float} longitude    
        @apiSuccess {String} feature_class      
        @apiSuccess {String} feature_code    
        @apiSuccess {String} country_code    
        @apiSuccess {String} cc2      
        @apiSuccess {int} admin1_code    
        @apiSuccess {int} admin2_code    
        @apiSuccess {int} admin3_code    
        @apiSuccess {int} admin4_code      
        @apiSuccess {int} population    
        @apiSuccess {String} elevation  
        @apiSuccess {String} dem    
        @apiSuccess {String} timezone  
        @apiSuccess {String} modification_date   

        @apiSuccessExample {json} Success-Response:  
        {
            "3037540": {
                "Geoname ID": "3037540",
                "Name": "Annecy-le-Vieux",
                "Ascii Name": "Annecy-le-Vieux",
                "Alternate Names": "Anesi le Vje,Annecium Vetus,Annecy-le-Vieux,Annesi-le-V'e,Annesi-le-Ve,Анеси ле Вје,Аннеси-ле-Вье,Аннесі-ле-Вє",
                "Latitude": "45.91971",
                "Longitude": "6.14393",
                "Feature class": "P",
                "Feature code": "PPL",
                "Country code": "FR",
                "CC2": "",
                "Admin1 code": "84",
                "Admin2 code": "74",
                "Admin3 code": "741",
                "Admin4 code": "74010",
                "Population": "21521",
                "Elevation": "",
                "Dem": "498",
                "Timezone": "Europe/Paris",
                "Modification date": "2017-05-29"
            }
        }

        @apiError location S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.

        @apiErrorExample {json} Error-Response:
        {
            "error": "La base de données n'a pas d'infos de cette location (961022)"
        }
        """

        geonameid = str(geonameid)
        location = fr.query.filter(fr.geonameid == geonameid).first()
        if not location:
            msg = f"La base de données n'a pas l'info de cette location ({geonameid})"
            return {"message":msg}, 404
        cityinfo = {
            "Geoname ID" : location.geonameid,
            "Name" : location.name,
            "Ascii Name" : location.asciiname,
            "Alternate Names" : location.alternatenames,
            "Latitude" : location.latitude,
            "Longitude" : location.longitude,
            "Feature class" : location.feature_class,
            "Feature code" : location.feature_code,
            "Country code" : location.country_code,
            "CC2" : location.cc2,
            "Admin1 code" : location.admin1_code,
            "Admin2 code" : location.admin2_code,
            "Admin3 code" : location.admin3_code,
            "Admin4 code" : location.admin4_code,
            "Population" : location.population,
            "Elevation" : location.elevation,
            "Dem" : location.dem,
            "Timezone" : location.timezone,
            "Modification date" : location.modification_date,
        }
        return { geonameid : cityinfo }

    # @login_required
    @auth.login_required
    def put(self, geonameid):
        """
        @api {put} https://home/geonames/<geonameid> /geonames/<geonameid> : Méthode PUT
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription modifier les informations d'une location en donnant l'identifiant(geonameid).

        @apiParam {int} geonameid      
        @apiParam {String} name    
        @apiParam {String} asciiname    
        @apiParam {String} alternatenames     
        @apiParam {Float} latitude   
        @apiParam {Float} longitude    
        @apiParam {String} feature_class      
        @apiParam {String} feature_code    
        @apiParam {String} country_code    
        @apiParam {String} cc2      
        @apiParam {int} admin1_code    
        @apiParam {int} admin2_code    
        @apiParam {int} admin3_code    
        @apiParam {int} admin4_code      
        @apiParam {int} population
        @apiParam {String} elevation  
        @apiParam {String} dem    
        @apiParam {String} timezone  
        @apiParam {String} modification_date   

        @apiParamExample {json} Request-Example:
        {
            "Geoname ID": "2968815",
            "Name": "Paris Store",
            "Ascii Name": "Paris Store",
            "Modification date": "2020-09-30"
        }
 
        @apiSuccessExample {json} Success-Response:  
        {
            "message":"Les informations de Paris Store (2968815) est bien modifiées."
        }

        @apiError result S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.

        @apiErrorExample {json} Error-Response:
        {
            "error": "La base de données n'a pas l'info de cette location (961022)"
        }

        @apiError user_info[0] Si l'utilisateur change l'identifiant d'un geoname, il renvoie un message d'erreur.

        @apiErrorExample {json} Error-Response:
        {
            "error": "Désolé, le geonameid ne peut pas être changé."
        }

        """
        user_info = []
        db_info = []
        
        # les informations après changement de l'user
        for item in info_list:
            user_info.append(request.form.get(item))

        # les informations originales de db
        geonameid = str(geonameid)
        result = fr.query.filter(fr.geonameid == geonameid).first()
        if not result:
            msg = "La base de données n'a pas l'info de cette location ({})".format(geonameid)
            return {"message":msg}, 404

        for i in info_list:
            field_info = eval(f'result.{i}')
            db_info.append(field_info)

        for i in range(len(info_list)):
            if i == 0:
                if user_info[i] != db_info[i]:
                    msg = u"Désolé, le geonameid ne peut pas être changé."
                    return jsonify({"message":msg})
            else:
                if user_info[i] != db_info[i]:
                    db_info[i] = user_info[i]
        
        location_new_version = fr(*db_info)

        db.session.delete(result)
        db.session.add(location_new_version)
        db.session.commit()
        
        msg = '****Les informations de {}({}) est bien modifiées.****'.format(user_info[1], geonameid)
        return {"message":msg}

    # @login_required
    @auth.login_required
    def delete(self, geonameid):
        """
        @api {delete} https://home/geonames/<geonameid> /geonames/<geonameid> : Méthode DELETE
        @apiVersion 1.0.0
        @apiGroup ClassData
        @apiDescription supprimer une location et toutes ces informations en donnant son identifiant.

        @apiSuccessExample {json} Success-Response:  
        {
            "message": "Paris(2968815) est supprimée."
        }

        @apiError result S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.
        @apiErrorExample {json} Error-Response:
        {
            "error": "La base de données n'a pas l'info de cette location (961022)."
        }
        """
        geonameid = str(geonameid)
        result = fr.query.filter(fr.geonameid == geonameid).first()
        if not result:
            msg = "La base de données n'a pas l'info de cette location ({})".format(geonameid)
            return {"message":msg}, 404
        cityname = result.name
        db.session.delete(result)
        db.session.commit()
        msg = '****{}({}) est supprimée.****'.format(cityname, geonameid)
        return {"message":msg}
        
        