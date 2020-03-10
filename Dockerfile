FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN python3.8 -m pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /requirements.txt
# RUN apt add --update --no-cache postgresql-client
# RUN apt add --update --no-cache --virtual .temp-buil-deps \
#     gcc libc-dev linux-header postgresql-dev
RUN pip install -r /requirements.txt
# RUN apt del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN useradd -ms /bin/bash fahad
USER fahad