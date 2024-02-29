FROM ubuntu

RUN apt update && apt install -y git
RUN apt-get update -y && apt-get install -y python3-pip build-essential curl

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]