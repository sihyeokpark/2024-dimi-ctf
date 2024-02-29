FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install socat -y

RUN mkdir problem

ADD . ./problem
WORKDIR ./problem

RUN chmod 755 ./.flag
RUN chmod 755 ./program
RUN rm -rf ./Dockerfile

RUN adduser wane
USER wane

EXPOSE 13372
CMD socat TCP-LISTEN:13372,reuseaddr,fork EXEC:./program,pty,raw,echo=0
