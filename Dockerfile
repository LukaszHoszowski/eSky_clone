FROM python:3.10.2-alpine AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_CODE=/usr/src/app

WORKDIR $APP_CODE

COPY Pipfile Pipfile.lock ./

RUN apk update \
    && apk upgrade \
    && apk add --no-cache --update --virtual .build-deps gcc postgresql-dev python3-dev musl-dev bash \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir pipenv \
    && pipenv install --system \
    && pipenv install flake8 \
    && apk del --no-cache .build-deps

COPY . ./

FROM build AS development
CMD flake8 -v --ignore=E501 --count --output-file=./docs/Flake8/flake8.log
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

EXPOSE 8000