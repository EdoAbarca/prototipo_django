from django.shortcuts import render
from .services import *
from datetime import date, timedelta

# Create your views here.

# Datos de conexión
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

fecha = (date.today()).strftime("%Y-%m-%d")


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def hoy(request):
    data = objetosHoy(fecha)
    media = mediaAsteroides()
    context = {
        'data': data,
        'media': media,
    }
    return render(request, 'hoy.html', context=context)


def distancia(request):
    data = distanciaM()
    media = mediaAsteroidesDist()
    context = {
        'data': data,
        'media': media
    }
    return render(request, 'distancia.html', context=context)


def peligro(request):
    data = peligroS()
    media = mediaAsteroidesPelig()
    context = {
        'data': data,
        'media': media,
    }
    return render(request, 'peligroso.html', context=context)


def cercano(request):
    data = cercanoS(fecha)
    context = {
        'data': data,
    }
    return render(request, 'cercano.html', context=context)


def lejano(request):
    data = lejanoS(fecha)
    context = {
        'data': data,
    }
    return render(request, 'lejano.html', context=context)
