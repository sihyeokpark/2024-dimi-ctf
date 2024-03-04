FROM ubuntu:22.04@sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f

ENV user wane
ENV chall_port 26146

RUN apt-get update
RUN apt-get -y install socat

RUN adduser $user

ADD ./THCJ_participate /home/$user/THCJ_participate
ADD ./WACCON_participate /home/$user/WACON_participate
ADD ./Connect_to_Wane /home/$user/Connect_to_Wane

RUN chown -R root:$user /home/$user/THCJ_participate
RUN chown -R root:$user /home/$user/WACON_participate
RUN chown root:$user /home/$user/Connect_to_Wane

RUN chmod -R 755 /home/$user/THCJ_participate
RUN chmod -R 755 /home/$user/WACON_participate
RUN chmod 755 /home/$user/Connect_to_Wane

WORKDIR /home/$user
USER $user
EXPOSE $chall_port
CMD socat -T 60 TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/Connect_to_Wane
