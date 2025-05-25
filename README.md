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





* Para clonar repositorio:


```bash


 git clone https://github.com/escandarr/ProyectoSD2025.git 


```





* Desde la carpeta `ProyectoSD2025`, levantar los contenedores con:


```bash


sudo docker compose up --build


```


* Para ver la cantidad de registros desde la terminal del modulo de almacenamiento (MongoDB) se utiliza los siguientes comandos:


```bash


sudo docker exec -it mongodb mongosh


use waze_db


db.eventos.countDocuments()


```


* Para poder ver la los graficos ir a de cache y trafico respectivamente:


```bash


http://localhost:7000/


```


```bash


http://localhost:5000/


```


## Parámetros de configuración





* Generador de tráfico (modificables en generador/generador.py):


```python


MODO = "poisson"          # Opciones: "poisson" o "normal"


LAMBDA = 5                # Parámetro para distribución Poisson


MEDIA_NORMAL = 1.0        # Media de la distribución Normal


STD_DEV_NORMAL = 0.2      # Desviación estándar de la distribución Normal


MONITOR_URL = "http://monitor:5000/evento"


```





* Redis (configurado en docker-compose.yml):


```yaml


redis:


  image: redis:7.2


  container_name: redis


  ports:


    - "6379:6379"


  command: >


    redis-server


    --maxmemory 100mb


    --maxmemory-policy allkeys-lru


  restart: always


```





- Política de cache: `allkeys-lru` `allkeys-lfu`


- Tamaño máximo: `100MB` `50MB`