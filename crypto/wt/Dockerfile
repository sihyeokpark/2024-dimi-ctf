FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat python3-pip -y
RUN pip install --upgrade pip

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

USER wane

EXPOSE 13374
CMD socat TCP-LISTEN:13374,reuseaddr,fork EXEC:"python3 Weird_Translator.py",pty,raw,echo=0
