FROM python:3.9-slim as base

ENV PYTHONPYCACHEPREFIX=/tmp

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN set -ex \
  && BUILD_DEPS="curl build-essential python3-dev" \
  && apt-get update && apt-get -y install $BUILD_DEPS \
  && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
  && . $HOME/.poetry/env \
  && poetry config virtualenvs.create false \ 
  && poetry install $(test "$BUILD_ENV" = production && echo "--no-dev") --no-root --no-interaction --no-ansi

COPY src /app/src