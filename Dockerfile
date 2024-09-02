# compile stage #
FROM python:3.12.5-slim-bookworm

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN pip install poetry==1.8.3

WORKDIR /opt/app

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt -o requirements.txt --without-hashes

# build stage #
FROM python:3.12.5-slim-bookworm

WORKDIR /opt/app

RUN apt update && apt install -y build-essential curl git g++ && rm -rf /var/lib/apt/lists/*

COPY --from=0 /opt/app/requirements.txt ./
RUN pip install --no-input -r requirements.txt

COPY . .

ENV PORT=8000
EXPOSE $PORT

CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT}
