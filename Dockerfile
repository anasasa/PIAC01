FROM python:3

ARG APP_DIR=/usr/src/PIAC01

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD templates/ $APP_DIR/hello_world/
ADD static/ $APP_DIR/hello_world/
ADD run.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/PIAC01 \
	FLASK_APP=PIAC01 flask run --host=0.0.0.0
