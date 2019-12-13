FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y build-essential python3-pip python3-dev
RUN pip3 install --upgrade pip

RUN mkdir -p /opt/microservices
ADD . /opt/microservices
RUN pip3 install -r /opt/microservices/requirements.txt

WORKDIR /opt/microservices
EXPOSE 5000

CMD python server.py
