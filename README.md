# Tarea 1 - Sistema Distribuidos
En este repositorio se encuentran todos los códigos implementados para poder levantar cada uno de los sistemas solicitados en cada entrega 

  Integrantes:
  * Benjamín Escandar
  * Jorge Gallegos
  ## Stack de tecnologías usado

[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=flat)](https://www.docker.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white&style=flat)](https://www.mongodb.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white&style=flat)](https://redis.io/)

## Instrucciones de uso

En la terminal utilizar los siguientes comandos:
```bash
 git clone https://github.com/escandarr/ProyectoSD2025.git 
```

Desde la carpeta ´ProyectoSD2025´, levantar los contenedores con:
```bash
sudo docker compose up --build
```
Para ver la cantidad de registros desde la terminal del modulo de almacenamiento (MongoDB) se utiliza los siguientes comandos:
```bash
sudo docker exec -it mongodb mongosh
use waze_db
db.eventos.countDocuments()
```


Para poder ver la los graficos ir a de cache y trafico respectivamente:
```bash
http://localhost:7000/
http://localhost:5000/
```
