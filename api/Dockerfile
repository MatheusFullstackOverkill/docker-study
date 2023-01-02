FROM python:3

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app