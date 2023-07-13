from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import pymongo
from .services import objetosHoy, distanciaM, cercanoS, lejanoS
from datetime import date

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


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def hoy(request):
    fecha = date.today().strftime("%Y-%m-%d")
    data = objetosHoy(fecha)
    context = {
        'data': data,
    }
    return render(request, 'hoy.html', context=context)


def distancia(request):
    data = distanciaM()
    context = {
        'data': data,
    }
    return render(request, 'distancia.html', context=context)


def acercandose(request):
    # data = objetosHoy()
    context = {}
    return render(request, 'acercandose.html', context=context)


def cercano(request):
    data = cercanoS()
    context = {
        'data': data,
    }
    return render(request, 'cercano.html', context=context)


def lejano(request):
    data = lejanoS()
    context = {
        'data': data,
    }
    return render(request, 'lejano.html', context=context)
