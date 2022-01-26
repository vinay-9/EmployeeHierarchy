FROM ubuntu:20.04

RUN apt-get update \
  && apt-get install -y python3-pip libmysqlclient-dev python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip3 install pymysql


WORKDIR /app
ENTRYPOINT pip3 install -r requirements.txt && python3 app.py