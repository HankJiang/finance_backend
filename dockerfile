FROM python:3.7-alpine

MAINTAINER gsxxm jianghan.ah@foxmail.com

COPY ./requirements.txt /www/requirements.txt

WORKDIR /www

ENV FLASK_ENV=production

RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python-dev libffi-dev openssl-dev make

RUN pip install --isolated -r requirements.txt

COPY . /www

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8888", "app:app"]