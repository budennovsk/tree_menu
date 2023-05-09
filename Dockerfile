FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 

RUN mkdir code
WORKDIR /code
ADD . /code/
ADD .env.docker /code/.env

RUN mkdir /code/static && mkdir /code/media

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD gunicorn menu.wsgi:application -b 0.0.0.0:8000

