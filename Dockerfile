# pull official base image
FROM python:3.9-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y build-essential pkg-config libcairo2-dev libgirepository1.0-dev

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install --only-binary :all: psutil reportlab

# copy requirements.txt
COPY requirements.txt /app/

# install project dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /app/
EXPOSE 8000

# run django server
CMD python manage.py runserver 0.0.0.0:8000
