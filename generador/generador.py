import time
import random
import numpy as np
import requests
import redis
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client["waze_db"]
coleccion = db["eventos"]

# Conexión a Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Parámetros
MODO = "poisson"  # O "poisson" o "normal"
LAMBDA = 5
MEDIA_NORMAL = 1.0
STD_DEV_NORMAL = 0.2
MONITOR_URL = "http://monitor:5000/evento"

def buscar_eventos_random(cantidad):
    total = coleccion.count_documents({})
    if total == 0:
        return []
    skip_values = random.sample(range(total), min(cantidad, total))
    eventos = []
    for skip in skip_values:
        evento = coleccion.find().skip(skip).limit(1).next()
        eventos.append(evento)
    return eventos

def enviar_eventos(eventos):
    for evento in eventos:
        evento_id = str(evento["_id"])
        print(f"[GENERADOR] Evento enviado: {evento_id} | Tipo: {evento.get('type', 'unknown')}")
        try:
            # Monitor web
            requests.post(MONITOR_URL, timeout=0.5)
            
            # Cache Redis
            if r.exists(evento_id):
                r.incr("hits")
                print(f"[CACHE] HIT {evento_id}")
            else:
                r.incr("misses")
                r.set(evento_id, 1, ex=3600)  # 1 hora TTL
                print(f"[CACHE] MISS {evento_id}")

        except Exception as e:
            print(f"[GENERADOR] Error al enviar: {e}")

def generador_normal():
    while True:
        delay = np.random.normal(MEDIA_NORMAL, STD_DEV_NORMAL)
        delay = max(0.01, delay)
        eventos = buscar_eventos_random(1)
        enviar_eventos(eventos)
        time.sleep(delay)

def generador_poisson():
    while True:
        n_eventos = np.random.poisson(LAMBDA)
        if n_eventos > 0:
            eventos = buscar_eventos_random(n_eventos)
            enviar_eventos(eventos)
        time.sleep(1)

def main():
    print(f"[GENERADOR] Iniciando en modo: {MODO}")
    if MODO == "poisson":
        generador_poisson()
    elif MODO == "normal":
        generador_normal()
    else:
        print("[GENERADOR] Error: modo inválido.")

if __name__ == "__main__":
    main()