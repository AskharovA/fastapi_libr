FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

CMD ["poetry", "run", "python", "src/main.py"]
