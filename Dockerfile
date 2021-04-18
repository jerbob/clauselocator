FROM python:3.9-slim as base

ENV PYTHONPYCACHEPREFIX=/tmp

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN set -ex \
  && apt-get update && apt-get -y install curl netcat \
  && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
  && . $HOME/.poetry/env \
  && poetry config virtualenvs.create false \ 
  && poetry install $(test "$BUILD_ENV" != "dev"  && echo "--no-dev") --no-root --no-interaction --no-ansi

COPY src /app/src

ENTRYPOINT [ "/app/src/entrypoint.sh" ]

CMD [ "gunicorn", "-w", "12", "-b", "0.0.0.0:80", "--chdir", "src", "core.wsgi:application" ]
