FROM python:3

ARG APP_DIR=/usr/src/PIAC01

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD templates/ $APP_DIR/templates/
ADD static/ $APP_DIR/static/
ADD run.py $APP_DIR
