import pymongo
from datetime import date

user = "mongo"
password = "mongo"
host = "mongodb"
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


def peligroS():
    filtro = {"is_potentially_hazardous_asteroid": True}
    data = asteroides.find(filtro)
    return data


def cercanoS():
    fecha = date.today()
    fecha = fecha.strftime("%Y-%m-%d")
    filtro = {"fecha": {"$eq": fecha}}
    data = asteroides.find_one(filtro, sort=[("close_approach_data.miss_distance", pymongo.ASCENDING)])
    return data


def lejanoS():
    fecha = date.today()
    fecha = fecha.strftime("%Y-%m-%d")
    filtro = {"fecha": {"$eq": fecha}}
    data = asteroides.find_one(filtro, sort=[("close_approach_data.miss_distance", pymongo.DESCENDING)])
    return data


def mediaAsteroides():
    fechas = asteroides.distinct('fecha')
    cont = 0
    for fecha in fechas:
        filtro = {'fecha': fecha}
        cont = cont + asteroides.count_documents(filtro)

    largo = len(fechas)
    promedio = int(cont / largo)
    return promedio


def mediaAsteroidesDist():
    filtro = {}
    cont = asteroides.count_documents(filtro)  # Total de documentos

    filtro = {"close_approach_data.miss_distance": {"$lt": 30000000}}
    cercanos = asteroides.count_documents(filtro)
    promedio = int(cont / cercanos)
    return promedio


def mediaAsteroidesPelig():
    filtro = {}
    cont = asteroides.count_documents(filtro)  # Total de documentos

    filtro = {"is_potentially_hazardous_asteroid": True}
    peligrosos = asteroides.count_documents(filtro)
    promedio = int(cont / peligrosos)
    return promedio
