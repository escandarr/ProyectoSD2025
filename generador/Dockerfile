# generador/Dockerfile

FROM python:3.12-slim

WORKDIR /app

COPY generador/ .

RUN pip install --no-cache-dir pymongo numpy requests redis

CMD ["python", "generador.py"]
