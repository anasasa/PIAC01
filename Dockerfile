FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY templates/ ./templates/
COPY static/ ./static/
COPY run.py ./

CMD PYTHONPATH=$PYTHONPATH:./run.py \
FLASK_APP=run flask run --host=0.0.0.0
