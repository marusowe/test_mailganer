FROM python:2.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python2-dev musl-dev zlib-dev jpeg-dev

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for

COPY . .

RUN chmod 777 entrypoint.sh
