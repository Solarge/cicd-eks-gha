# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 show Flask && pip3 uninstall -y Flask || echo "Flask is not installed"
RUN pip3 install Flask

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
