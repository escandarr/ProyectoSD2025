from pymongo import MongoClient
import csv
import os
from datetime import datetime

client = MongoClient("mongodb://mongodb:27017/")
db = client["waze_db"]
coleccion = db["eventos"]

def evento_valido(evento):
    campos = ["uuid", "city", "pubMillis", "type"]
    return all(campo in evento for campo in campos)

def normalizar_texto(texto):
    if not isinstance(texto, str):
        return ""
    return texto.strip().lower().replace("á", "a").replace("é", "e")\
        .replace("í", "i").replace("ó", "o").replace("ú", "u")

def procesar_eventos():
    eventos = coleccion.find()
    eventos_limpios = []

    for evento in eventos:
        if not evento_valido(evento):
            continue

        uuid = evento["uuid"]
        tipo = normalizar_texto(evento.get("type", "desconocido"))
        ciudad = normalizar_texto(evento.get("city", ""))
        calle = normalizar_texto(evento.get("street", ""))
        fecha = datetime.fromtimestamp(int(evento["pubMillis"]) / 1000).strftime("%Y-%m-%d %H:%M:%S")
        severidad = evento.get("severity", "")

        eventos_limpios.append({
            "uuid": uuid,
            "type": tipo,
            "city": ciudad,
            "street": calle,
            "date": fecha,
            "severity": severidad,
        })

    if not eventos_limpios:
        print("⚠ No se encontraron eventos válidos.")
        return

    os.makedirs("salida", exist_ok=True)
    with open("salida/eventos_filtrados.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=eventos_limpios[0].keys())
        writer.writeheader()
        writer.writerows(eventos_limpios)

    print(f"✔ Procesamiento completo. Eventos exportados: {len(eventos_limpios)}")

if __name__ == "__main__":
    procesar_eventos()
