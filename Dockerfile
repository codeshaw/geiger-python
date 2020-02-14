FROM python:3.6-alpine

RUN adduser -D geiger

WORKDIR /home/geiger

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY geiger geiger
COPY app.py start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP app.py

RUN chown -R geiger:geiger ./
USER geiger

EXPOSE 8080
ENTRYPOINT ["./start.sh"]
