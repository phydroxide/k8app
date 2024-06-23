# syntax=docker/dockerfile:1 
# 
# Adapted from:
# https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
FROM python:3.8-slim-buster
WORKDIR /python-docker
RUN apt-get update && apt-get install netcat sqlite3 vim -y && apt clean 
COPY ../City.mmdb City.mmdb 

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r ./requirements.txt
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "5555"]
#CMD [ "python3", "./app.py" ] 
 
