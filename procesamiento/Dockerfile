# procesamiento/Dockerfile

FROM python:3.12-slim

WORKDIR /app

COPY procesamiento/filtrar_eventos.py .

RUN pip install pymongo

CMD ["python", "filtrar_eventos.py"]
