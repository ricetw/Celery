FROM python:3.6.8

WORKDIR /flask-Celery

#COPY ./requirements.txt /flask-Celery
#
#RUN pip install -r requirements.txt
#
#COPY . /flask-Celery

COPY . /flask-Celery

RUN pip install -r requirements.txt

EXPOSE 5000

CMD waitress-serve --listen=*:5000 app:app