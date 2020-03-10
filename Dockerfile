FROM python:3.8

ENV PYTHONUNBUFFERED 1


RUN python3.8 -m pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN useradd -ms /bin/bash fahad
USER fahad