from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
import pymongo

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


def distancia(request):
    #data = objetosHoy()
    context = {}
    return render(request, 'distancia.html', context=context)


class NeoWSViewTest(APIView):
    def get(self, request):
        return Response({'message': 'hello world'}, status=status.HTTP_200_OK)


class NeoWSView(APIView):
    def post(self, request):
        data = request.data
        try:
            init_date = data['init_date']
            end_date = data['end_date']
            key = data['key']
        except Exception as key_error:
            return Response({'message': 'invalid request 1', 'error': str(key_error)},
                            status=status.HTTP_400_BAD_REQUEST)
        print(init_date, end_date, key)
        try:
            url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={init_date}&end_date={end_date}&api_key={key}'
            print(url)
            request_neows = requests.get(url)
            print(request_neows)
            response_neows = request_neows.content.decode('utf-8')
            print(response_neows)
        except Exception as e:
            return Response({'message': 'invalid request 2', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'success', 'data': response_neows}, status=status.HTTP_201_CREATED)
