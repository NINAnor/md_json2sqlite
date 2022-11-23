FROM python:3.8

RUN pip3 install poetry 

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . ./

ENV PYTHONPATH "${PYTHONPATH}:/app"
