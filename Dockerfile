FROM python:3.6-alpine

RUN adduser -D geiger

WORKDIR /home/geiger

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY geiger geiger
COPY app.py start.sh ./
RUN chmod +x start.sh

RUN chown -R geiger:geiger ./
USER geiger

EXPOSE 8080
ENTRYPOINT ["./start.sh"]
RUN source venv/bin/activate
CMD ["waitress-serve", "--port=8080", "geiger:geiger"]
