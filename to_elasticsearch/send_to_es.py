# send_to_es.py

import requests
import csv
import time

# Dirección de Elasticsearch (ajústala si corres esto desde dentro de un contenedor)
ELASTICSEARCH_URL = "http://localhost:9200/eventos/_doc"

def enviar_a_elasticsearch(eventos):
    for evento in eventos:
        doc = {
            "uuid": evento[0],
            "tipo": evento[1],
            "comuna": evento[2],
            "calle": evento[3],
            "fecha": evento[4],
            "gravedad": int(evento[5])
        }

        try:
            res = requests.post(ELASTICSEARCH_URL, json=doc)
            print(f"[INFO] Enviado: {res.status_code} - {res.json().get('_id', '')}")
        except Exception as e:
            print(f"[ERROR] Fallo al enviar evento: {evento} - {e}")
        time.sleep(0.05)  # Para evitar saturar ES

def leer_csv(ruta_archivo):
    eventos = []
    with open(ruta_archivo, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for fila in reader:
            if len(fila) == 6:
                eventos.append(fila)
    return eventos

if __name__ == "__main__":
    ruta_archivo = "salida/eventos_filtrados/part-m-00000"
    eventos = leer_csv(ruta_archivo)
    print(f"[INFO] Total eventos leídos: {len(eventos)}")
    enviar_a_elasticsearch(eventos)
