from flask import Flask, request
from os import urandom
import subprocess


app = Flask(__name__)
app.secret_key = urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = 'DH{This_is_flag}'


@app.route("/", methods=["GET"])
def index():
    url = request.args.get("url", "")
    if len(url) == 0:
        return 'Please enter url. Ex) ?url=http://exon.kr'
    
    if url[0:14] != 'http://exon.kr':
        return 'Nono.. you need to go to exon.kr'
    else:
        try:
            response = subprocess.run(
                ["curl", f"{url}"], capture_output=True, text=True, timeout=1, shell=False
            )
            print(response.stdout)
            return 'Success!!! Reponse: ' + response.stdout
        except subprocess.TimeoutExpired:
            return 'Timeout !!!'


@app.route("/flag", methods=["GET"])
def flag():
    ip_address = request.remote_addr
    if ip_address == "127.0.0.1":
        return FLAG
    else:
        return "Only local access allowed", 403


app.run(host="0.0.0.0", port=3000)
