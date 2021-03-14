define({ "api": [
  {
    "type": "delete",
    "url": "https://home/geonames/<geonameid>",
    "title": "/geonames/<geonameid> : Méthode DELETE",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>supprimer une location et toutes ces informations en donnant son identifiant.</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message\": \"Paris(2968815) est supprimée.\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "result",
            "description": "<p>S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"error\": \"La base de données n'a pas l'info de cette location (961022).\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "DeleteHttpsHomeGeonamesGeonameid"
  },
  {
    "type": "get",
    "url": "https://home",
    "title": "home : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>Selon les données fournies, cette page va réorienter vers la page de login ou la page de création du compte.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "choice",
            "description": "<p>: 'login' ou 'create'</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message\": \"home page\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/home.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHome"
  },
  {
    "type": "get",
    "url": "https://home/admins/create",
    "title": "/admins/create : Méthode POST",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>cette méthode va créer une entrée de user dans le tableau &quot;users&quot; du db &quot;locations.db&quot;, elle: 1) reccueillit les infos remplies dans cette page; 2) teste toutes les infos 3) écrit dans le db 4) renvoie un message indiquant le résultat de l'opération</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message(201)\": \"Votre compte admin a bien été créé.\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"400\": \"Veuillez remplir tous les champs.\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "{\n    \"400\": \"Désolée, vous n'êtes pas notre collaborateur, vous ne pouvez pas créer un compte.\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "{\n    \"400\": \"Vous avez déjà un compte.\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "{\n    \"400\": \"Votre id ne conforme pas à votre nom. \"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "{\n    \"400\": \"Les deux mots de passe remplis doivent être identiques.\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/admins.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeAdminsCreate"
  },
  {
    "type": "get",
    "url": "https://home/admins/login",
    "title": "/admins/login : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>afficher la page de login.</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message\": \"login page\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/admins.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeAdminsLogin"
  },
  {
    "type": "get",
    "url": "https://home/admins/logout",
    "title": "/admins/logout : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>Cette méthode supprime l'info stocké dans session et réoriente vers la page d'accueil.</p>",
    "filename": "./resources/admins.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeAdminsLogout"
  },
  {
    "type": "get",
    "url": "https://home/geonames",
    "title": "/geonames : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>obtenir les informations principales d'une ou des location(s) en donnant un nom à rechercher.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>nom de la location.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"name\": \"Annecy\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"3037540\": {\n        \"geonameid\": \"3037540\",\n        \"name\": \"Annecy-le-Vieux\",\n        \"latitude\": \"45.91971\",\n        \"longitude\": \"6.14393\"\n    },\n    \"3037541\": {\n        \"geonameid\": \"3037541\",\n        \"name\": \"Lac d'Annecy\",\n        \"latitude\": \"45.85164\",\n        \"longitude\": \"6.1767\"\n    },\n    \"3037542\": {\n        \"geonameid\": \"3037542\",\n        \"name\": \"Arrondissement d'Annecy\",\n        \"latitude\": \"45.8907\",\n        \"longitude\": \"6.17903\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeGeonames"
  },
  {
    "type": "get",
    "url": "https://home/geonames/add",
    "title": "/geonames/add : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>obtenir une liste d'inforamtions à remplir pour une location.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "asciiname",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "alternatenames",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_class",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "country_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cc2",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin1_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin2_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin3_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin4_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "population",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "elevation",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "dem",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "timezone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "modification_date",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"infolist\": [\n        \"geonameid\",\n        \"name\",\n        \"asciiname\",\n        \"alternatenames\",\n        \"latitude\",\n        \"longitude\",\n        \"feature_class\",\n        \"feature_code\",\n        \"country_code\",\n        \"cc2\",\n        \"admin1_code\",\n        \"admin2_code\",\n        \"admin3_code\",\n        \"admin4_code\",\n        \"population\",\n        \"elevation\",\n        \"dem\",\n        \"timezone\",\n        \"modification_date\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeGeonamesAdd"
  },
  {
    "type": "get",
    "url": "https://home/geonames/<geonameid>",
    "title": "/geonames/<geonameid> : Méthode GET",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>obtenir les informations détaillées d'une location en donnant l'identifiant(geonameid).</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "asciiname",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "alternatenames",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "feature_class",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "feature_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "country_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "cc2",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin1_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin2_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin3_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin4_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "population",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "elevation",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "dem",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "timezone",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "modification_date",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"3037540\": {\n        \"Geoname ID\": \"3037540\",\n        \"Name\": \"Annecy-le-Vieux\",\n        \"Ascii Name\": \"Annecy-le-Vieux\",\n        \"Alternate Names\": \"Anesi le Vje,Annecium Vetus,Annecy-le-Vieux,Annesi-le-V'e,Annesi-le-Ve,Анеси ле Вје,Аннеси-ле-Вье,Аннесі-ле-Вє\",\n        \"Latitude\": \"45.91971\",\n        \"Longitude\": \"6.14393\",\n        \"Feature class\": \"P\",\n        \"Feature code\": \"PPL\",\n        \"Country code\": \"FR\",\n        \"CC2\": \"\",\n        \"Admin1 code\": \"84\",\n        \"Admin2 code\": \"74\",\n        \"Admin3 code\": \"741\",\n        \"Admin4 code\": \"74010\",\n        \"Population\": \"21521\",\n        \"Elevation\": \"\",\n        \"Dem\": \"498\",\n        \"Timezone\": \"Europe/Paris\",\n        \"Modification date\": \"2017-05-29\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "location",
            "description": "<p>S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"error\": \"La base de données n'a pas d'infos de cette location (961022)\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "GetHttpsHomeGeonamesGeonameid"
  },
  {
    "type": "post",
    "url": "https://home/geonames/add",
    "title": "/geonames/add : Méthode POST",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>ajouter les informations pour une location.</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "asciiname",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "alternatenames",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_class",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "country_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cc2",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin1_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin2_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin3_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin4_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "population",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "elevation",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "dem",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "timezone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "modification_date",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"Geoname ID\": \"2968815\",\n    \"Name\": \"Paris\",\n    \"Ascii Name\": \"Paris\",\n    \"Alternate Names\": \"Departement de Paris,Département de Paris,Parigi,Paris,Paris Department\",\n    \"Latitude\": \"48.8534\",\n    \"Longitude\": \"2.3486\",\n    \"Feature class\": \"A\",\n    \"Feature code\": \"ADM2\",\n    \"Country code\": \"FR\",\n    \"CC2\": \"FR\",\n    \"Admin1 code\": \"11\",\n    \"Admin2 code\": \"75\",\n    \"Admin3 code\": \"13\",\n    \"Admin4 code\": \"14\",\n    \"Population\": \"2257981\",\n    \"Elevation\": \"33443\",\n    \"Dem\": \"35\",\n    \"Timezone\": \"Europe/Paris\",\n    \"Modification date\": \"2019-06-17\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "asciiname",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "alternatenames",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "feature_class",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "feature_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "country_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "cc2",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin1_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin2_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin3_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "admin4_code",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "population",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "elevation",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "dem",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "timezone",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "modification_date",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message\": \"Beijing(112233) est bien ajoutée dans la base de données.\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "info",
            "description": "<p>S'il y existes des champs incomplets, il renvoie un message d'erreur pour compléter tous les champs.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"error\": \"Veuillez remplir tous les champs. \"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "PostHttpsHomeGeonamesAdd"
  },
  {
    "type": "put",
    "url": "https://home/geonames/<geonameid>",
    "title": "/geonames/<geonameid> : Méthode PUT",
    "version": "1.0.0",
    "group": "ClassData",
    "description": "<p>modifier les informations d'une location en donnant l'identifiant(geonameid).</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "geonameid",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "asciiname",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "alternatenames",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "latitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Float",
            "optional": false,
            "field": "longitude",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_class",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "feature_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "country_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "cc2",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin1_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin2_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin3_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "admin4_code",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "int",
            "optional": false,
            "field": "population",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "elevation",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "dem",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "timezone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "modification_date",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"Geoname ID\": \"2968815\",\n    \"Name\": \"Paris Store\",\n    \"Ascii Name\": \"Paris Store\",\n    \"Modification date\": \"2020-09-30\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:  ",
          "content": "{\n    \"message\":\"Les informations de Paris Store (2968815) est bien modifiées.\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "result",
            "description": "<p>S'il n'existe pas le geonameid demandé dans la base de données, il renvoie un message d'erreur.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "user_info[0]",
            "description": "<p>Si l'utilisateur change l'identifiant d'un geoname, il renvoie un message d'erreur.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"error\": \"La base de données n'a pas l'info de cette location (961022)\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "{\n    \"error\": \"Désolé, le geonameid ne peut pas être changé.\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./resources/places.py",
    "groupTitle": "ClassData",
    "name": "PutHttpsHomeGeonamesGeonameid"
  }
] });
