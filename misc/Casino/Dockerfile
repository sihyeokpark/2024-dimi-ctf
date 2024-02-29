FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip
RUN pip install pycryptodome

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

USER wane

EXPOSE 13371
CMD socat TCP-LISTEN:13371,reuseaddr,fork EXEC:"python3 casino.py",pty,raw,echo=0
