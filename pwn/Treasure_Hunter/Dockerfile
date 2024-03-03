FROM ubuntu:22.04@sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f

ENV user island
ENV chall_port 26146

RUN apt-get update
RUN apt-get -y install socat

RUN adduser $user

ADD ./flaf /home/$user/flaf
ADD ./.flag /home/$user/.flag
ADD ./prob /home/$user/prob

RUN chown -R root:$user /home/$user/flaf
RUN chown -R root:$user /home/$user/.flag
RUN chown -R root:$user /home/$user/prob

RUN chmod 755 /home/$user/prob
RUN chmod 755 -R /home/$user/.flag
RUN chmod 755 -R /home/$user/flaf

WORKDIR /home/$user
USER $user
EXPOSE $chall_port
CMD socat -T 60 TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/prob
