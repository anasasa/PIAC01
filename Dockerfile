FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY templates/ ./templates/
COPY static/ ./static/
COPY run.py ./

CMD ["python", "./run.py"]
