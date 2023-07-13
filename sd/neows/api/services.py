import requests as req
import pymongo

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

# Colección
asteroides = db.get_collection("asteroides")


#########################################################
# Funciones con llamadas a MongoDB

# Cambiar consulta a la APi por Consulta a la DB
def objetosHoy(fecha):
    filtro = {"fecha": {"$eq": fecha}}
    data = asteroides.find(filtro)
    return data


def distanciaM():
    filtro = {"close_approach_data.miss_distance": {"$lt": 30000000}}
    data = asteroides.find(filtro)
    return data


def cercanoS():
    filtro = {}
    data = asteroides.find_one(filtro, sort=[("close_approach_data.miss_distance", pymongo.ASCENDING)])
    return data


def lejanoS():
    filtro = {}
    data = asteroides.find_one(filtro, sort=[("close_approach_data.miss_distance", pymongo.DESCENDING)])
    return data
