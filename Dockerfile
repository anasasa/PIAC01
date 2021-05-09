FROM python:3.8

COPY app.py /app/
WORKDIR /app
RUN pip install flask
RUN export FLASK_APP=app.py

EXPOSE 5000
CMD ["/usr/local/bin/flask", "run", "--host", "0.0.0.0"]
