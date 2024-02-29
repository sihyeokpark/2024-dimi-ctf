FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

USER wane

EXPOSE 13373
CMD socat TCP-LISTEN:13373,reuseaddr,fork EXEC:"python3 cipher.py",pty,raw,echo=0
