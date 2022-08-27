# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /code
ENV FLASK_APP=src/main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /code
CMD ["flask", "run"]