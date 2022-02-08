FROM python:3.10.2-alpine AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN apk update \
    && apk add --no-cache --update --virtual .build-deps gcc postgresql-dev python3-dev musl-dev \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir pipenv \
    && pipenv install --system \
    && apk del --no-cache .build-deps

COPY . ./

FROM build AS development
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
