import pymongo
import requests as req

user = "mongo"
password = "mongo"
host = "localhost"
port = "27017"
main_database = "admin"
database = "neows"

# Conexion a mongoDB
client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/{main_database}")

# Base de datos a usar
db = client.get_database(database)


def objetosHoy(params=None):
    if params is None:
        params = {}
    api_url = "https://www.neowsapp.com/rest/v1/feed/today?api_key=5640"
    response = req.get(api_url, params)
    data = response.json()
    return data


def impactoDeRiesgo(tamanio, params=None):
    if params is None:
        params = {}
    api_url = "https://www.neowsapp.com/rest/v1/neo/sentry?is_active=true&size=" + str(tamanio) + "&api_key=5640"
    response = req.get(api_url, params)
    data = response.json()
    return data


def subirJson(data):

    print(db)
    db.insert_many(data)
