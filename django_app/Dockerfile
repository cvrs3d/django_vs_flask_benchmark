FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY reqs.txt /usr/src/app

RUN pip install -r reqs.txt

COPY . /usr/src/app