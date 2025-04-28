import time
import random
import numpy as np
import requests
from pymongo import MongoClient

# Conexión a MongoDB (en Docker)
client = MongoClient("mongodb://mongodb:27017/")
db = client["waze_db"]
coleccion = db["eventos"]

# Parámetros
MODO = "normal"  # Cambiado a "normal" o "poisson"
LAMBDA = 5       # Solo se usa si vuelves a modo poisson
MEDIA_NORMAL = 1.0  # Media de segundos entre eventos para Normal
STD_DEV_NORMAL = 0.2  # Desviación estándar para Normal (pequeña variabilidad)
MONITOR_URL = "http://monitor:5000/evento"  # URL del monitor Flask

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
        print(f"[GENERADOR] Evento enviado: {evento['_id']} | Tipo: {evento.get('type', 'unknown')}")
        try:
            requests.post(MONITOR_URL, timeout=0.5)
        except Exception as e:
            print(f"[GENERADOR] Error al enviar al monitor: {e}")

def generador_poisson():
    """Genera eventos usando distribución de Poisson."""
    while True:
        n_eventos = np.random.poisson(LAMBDA)
        if n_eventos > 0:
            eventos = buscar_eventos_random(n_eventos)
            enviar_eventos(eventos)
        time.sleep(1)

def generador_normal():
    """Genera eventos usando distribución Normal."""
    while True:
        delay = np.random.normal(MEDIA_NORMAL, STD_DEV_NORMAL)
        delay = max(0.01, delay)  # Evitar delays negativos o muy chicos hola
        eventos = buscar_eventos_random(1)
        enviar_eventos(eventos)
        time.sleep(delay)

def main():
    print(f"[GENERADOR] Iniciando en modo: {MODO}")
    if MODO == "poisson":
        generador_poisson()
    elif MODO == "normal":
        generador_normal()
    else:
        print("[GENERADOR] Error: modo inválido. Usa 'poisson' o 'normal'.")

if __name__ == "__main__":
    main()
