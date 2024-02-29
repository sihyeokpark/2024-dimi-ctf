FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip
RUN pip install pycryptodome

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

RUN chmod 644 ./flag

USER wane

EXPOSE 13375
CMD socat TCP-LISTEN:13375,reuseaddr,fork EXEC:"python3 Exp2loit.py",pty,raw,echo=0
