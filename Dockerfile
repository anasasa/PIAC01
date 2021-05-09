FROM python:3.8

WORKDIR /usr/src/run
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./run.py"]
