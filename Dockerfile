# pull official base image
FROM python:3.9-alpine3.14

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy project
COPY . /app/
EXPOSE 8000

# run django server
CMD python manage.py runserver 0.0.0.0:8000