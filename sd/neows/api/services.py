import requests as req
import pymongo
from datetime import date, timedelta
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import dumps
from multiprocessing import Process
import os

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

# Topicos de kafka
topic_name1 = 'Topic1'
topic_name2 = 'Topic2'
topic_name3 = 'Topic3'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

pids = list()

def objetosHoy(params=None):
    if params is None:
        params = {}
    api_url = "https://www.neowsapp.com/rest/v1/feed/today?api_key=5640"
    response = req.get(api_url, params)
    data = response.json()
    return data


def asteroidesDistancia(params=None):
    fecha = date.today() - timedelta(days=7)
    fecha = fecha.strftime("%Y-%m-%d")
    api_url = "https://www.neowsapp.com/rest/v1/feed?start_date=" + str(fecha) + "&detailed=false"
    response = req.get(api_url, params)
    data = response.json()
    largo = len(data)
    cont = 0
    for elemento in data:
        if cont % 3 == 1:
            producer.send(topic_name1, value=elemento)
        elif cont % 3 == 2:
            producer.send(topic_name2, value=elemento)
        else:
            producer.send(topic_name3, value=elemento)
        cont += 1
    crearProcesos()

def impactoDeRiesgo(tamanio, params=None):
    if params is None:
        params = {}
    api_url = "https://www.neowsapp.com/rest/v1/neo/sentry?is_active=true&size=" + str(tamanio) + "&api_key=5640"
    response = req.get(api_url, params)
    data = response.json()
    return data

def pasarData():
    print('pid: ' + str(os.getpid()))
    if os.getpid() == pids[0]:
        consumer = KafkaConsumer(topic_name1, group_id='id1', bootstrap_servers=['localhost:9092'])
        print('Hilo 1')
        for element in consumer:
            print(element)

    if os.getpid() == pids[1]:
        consumer = KafkaConsumer(topic_name2, group_id='id2', bootstrap_servers=['localhost:9092'])
        print('Hilo 2')
        for element in consumer:
            print(element)

    if os.getpid() == pids[2]:
        consumer = KafkaConsumer(topic_name3, group_id='id3', bootstrap_servers=['localhost:9092'])
        print('Hilo 3')
        for element in consumer:
            print(element)


def crearProcesos():
    procesos = list()
    for i in range(3):
        print('creando hilos: ' + str(i))
        p = Process(target=pasarData, args=())
        p.start()
        procesos.append(p)
        pids.append(p.pid)

    print('pids: ' + str(pids))

    for p in procesos:
        p.join()
