FROM python:3.7-slim

MAINTAINER gsxxm jianghan.ah@foxmail.com

COPY ./requirements.txt /www/requirements.txt

WORKDIR /www

ENV FLASK_ENV=production

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --isolated -r requirements.txt

COPY . /www

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:9001", "app:app"]