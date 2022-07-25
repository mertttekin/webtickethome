FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
#requşred alpine packages to install uWSGI
RUN pip install -r/requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./webticket /webticket