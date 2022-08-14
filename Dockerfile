FROM python:3.11-rc-slim

EXPOSE 80
WORKDIR /app
COPY source_code/ /app
RUN pip install --root-user-action=ignore -r requirements.txt
USER nobody
ENTRYPOINT ["python", "server.py"]
