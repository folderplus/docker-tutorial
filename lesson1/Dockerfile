FROM harbor.mobagel.com/core-tech-ci/python:3.8-slim as base
RUN apt-get update && pip3 install --upgrade pip & pip install poetry
WORKDIR /app
COPY ./poetry.lock poetry.lock
COPY ./pyproject.toml pyproject.toml
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-dev

CMD uvicorn app:app --host 0.0.0.0 --reload