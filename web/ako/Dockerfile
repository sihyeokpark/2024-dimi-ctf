FROM python:3.8

RUN apt update && apt install -y git
RUN apt-get update -y && apt-get install -y python3-pip build-essential curl

RUN pip install --upgrade pip

COPY ./deploy /deploy/
WORKDIR /deploy
RUN pip install -r requirements.txt

CMD ["python", "/deploy/main/app.py"]