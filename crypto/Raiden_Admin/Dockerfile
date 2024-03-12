FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

RUN chmod 644 ./flag
RUN chmod 644 ./pull_raiden.py

USER wane

EXPOSE 6666
CMD socat TCP-LISTEN:6666,reuseaddr,fork EXEC:"python3 pull_raiden.py",pty,raw,echo=0
