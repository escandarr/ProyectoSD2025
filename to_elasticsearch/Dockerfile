# to_elasticsearch/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY send_to_es.py .

RUN pip install requests

CMD ["python", "send_to_es.py"]
