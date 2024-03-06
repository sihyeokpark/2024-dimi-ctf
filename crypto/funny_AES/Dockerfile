FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip
RUN pip install pycryptodome

RUN adduser Aw

ADD . /home/Aw

WORKDIR /home/Aw

USER Aw

EXPOSE 7770
CMD socat TCP-LISTEN:7770,reuseaddr,fork EXEC:"python3 server.py",pty,raw,echo=0