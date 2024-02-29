FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat -y

RUN adduser wane

ADD . /home/wane

WORKDIR /home/wane

RUN chmod 644 ./flag
RUN chmod 755 ./unreliable_user

USER wane

EXPOSE 13370
CMD socat TCP-LISTEN:13370,reuseaddr,fork EXEC:./unreliable_user,pty,raw,echo=0
