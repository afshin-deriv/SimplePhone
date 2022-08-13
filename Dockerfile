FROM python:3.11-rc-slim

WORKDIR /app
COPY source_code/ /app
RUN pip install --root-user-action=ignore -r requirements.txt
ENTRYPOINT ["python", "server.py"]
