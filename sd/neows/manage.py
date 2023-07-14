#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import multiprocessing as mp
import requests as req
import pymongo
from datetime import date, timedelta, datetime
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import dumps, loads
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


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neows.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def dataHoy(params=None):
    fecha = date.today()
    fecha = fecha.strftime("%Y-%m-%d")
    docs = asteroides.find()
    print(fecha)
    flag = 0  # Nos indica si ya se ingresaron los datos de asteroides del dia de hoy (0: no, 1: si)
    for documento in docs:
        if documento['fecha'] == fecha:
            flag = 1

    if flag == 0:
        api_url = "https://www.neowsapp.com/rest/v1/feed/today?detailed=false&api_key=5640"
        response = req.get(api_url, params)
        data = response.json()
        near_objects = data.get('near_earth_objects').get(fecha)
        cont = 0
        for elemento in near_objects:
            if cont % 3 == 1:
                print(type(elemento))
                producer.send(topic_name1, value=elemento)
            elif cont % 3 == 2:
                print(type(elemento))
                producer.send(topic_name2, value=elemento)
            else:
                print(type(elemento))
                producer.send(topic_name3, value=elemento)
            cont += 1
        crearProcesos()
    else:
        print("Los datos de hoy ya han sido ingresados")


def filtrarData(consumer):
    fecha = date.today()
    fecha = fecha.strftime("%Y-%m-%d")
    for message in consumer:
        if isinstance(message.value, dict):
            aux = {"fecha": fecha,
                   "id": message.value['id'],
                   "name": message.value['name'],
                   "estimated_diameter": {
                       "estimated_diameter_min": message.value['estimated_diameter']['meters']['estimated_diameter_min'],
                       "estimated_diameter_max": message.value['estimated_diameter']['meters']['estimated_diameter_max']},  # Solo metros
                   "is_potentially_hazardous_asteroid": message.value['is_potentially_hazardous_asteroid'],
                   "close_approach_data": {
                       "close_approach_date": message.value['close_approach_data'][0]['close_approach_date'],
                       "miss_distance": float(message.value['close_approach_data'][0]['miss_distance']['kilometers'])}}  # Solo kilometros

            asteroides.insert_one(aux)
            print(aux)
        else:
            print("El valor del mensaje no es un diccionario")


def pasarData(flag):
    print('pid: ' + str(os.getpid()))
    if flag == 0:
        consumer = KafkaConsumer(topic_name1, group_id='id1', bootstrap_servers=['localhost:9092'],
                                 consumer_timeout_ms=1000, value_deserializer=lambda m: loads(m.decode('utf-8')))
        filtrarData(consumer)
        print('pasando a 0')
        consumer.close()

    if flag == 1:
        consumer = KafkaConsumer(topic_name2, group_id='id2', bootstrap_servers=['localhost:9092'],
                                 consumer_timeout_ms=1000, value_deserializer=lambda m: loads(m.decode('utf-8')))
        filtrarData(consumer)
        print('pasando a 1')
        consumer.close()

    if flag == 2:
        consumer = KafkaConsumer(topic_name3, group_id='id3', bootstrap_servers=['localhost:9092'],
                                 consumer_timeout_ms=1000, value_deserializer=lambda m: loads(m.decode('utf-8')))
        filtrarData(consumer)
        print('pasando a 2')
        consumer.close()


def crearProcesos():
    procesos = list()
    for i in range(3):
        print('creando hilos: ' + str(i))
        p = Process(target=pasarData, args=(i,))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()


if __name__ == '__main__':
    mp.set_start_method('spawn')
    dataHoy()
    main()
