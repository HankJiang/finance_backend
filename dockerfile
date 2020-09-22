FROM python:3.7-slim

MAINTAINER gsxxm jianghan.ah@foxmail.com

COPY ./requirements.txt /www/requirements.txt
COPY ./manage.py /www/manage.py

WORKDIR /www

ENV FLASK_ENV=production

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . /www
