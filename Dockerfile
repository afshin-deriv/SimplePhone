FROM python:3.11-rc-slim

WORKDIR /app
COPY source_code/ /app
RUN pip install -r requirements.txt
USER app
ENTRYPOINT ["python", "server.py"]
