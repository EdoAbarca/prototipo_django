# Prueba de concepto

Segunda entrega del laboratorio de sistemas distribuidos de la Universidad de Santiago de Chile
- Prof: Marcela Rivera
- Integrantes: Aldo Castillo y Eduardo Abarca

## Tecnologias
- Django
- Python
- Docker
- Apache Kafka
- Html + CSS

## Manual de uso

Para poder usar esta aplicacion es necesario seguir ciertos pasos que se detallaran a continuación:

### Kafka
Para ejecutar esta aplicacion es necesario tener docker y docker-compose instalado, al instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/) deberian instalarse por defecto.

Una vez instalado abrir una consola de comandos en la carpeta "kafka-stack-docker-compose-master", ejecutar el comando:
```
docker-compose -f ./zk-single-kafka-single.yml up
```

#### Aplicacion
Abrir una consola en la carpeta "sd" del proyecto y ejectuar el comando
```
docker-compose up
```
