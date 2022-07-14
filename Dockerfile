FROM debian:latest
MAINTAINER Egor Gasay 'https://github.com/egorgasay'
RUN apt-get update 
RUN apt-get install -y python3 python3-pip
COPY . /todoapp-with-restfull-api
WORKDIR /todoapp-with-restfull-api
RUN pip install -r requirements.txt
RUN apt-get install python3-tk -y
RUN python3 manage.py migrate
