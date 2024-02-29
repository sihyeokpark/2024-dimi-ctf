from flask import Flask, request
from hashlib import md5
from os import urandom
import subprocess

app = Flask(__name__)
app.secret_key = urandom(32)

FLAG = 'DIMI{doY0uKnowFilePr0toco1?}'

secret = open('./secret.txt', 'r').read()

@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url', '').strip()
    if len(url) == 0:
        return 'Please enter url. Ex) ?url=http://exon.kr'
    print(url)
    try:
        response = subprocess.run(
            ['curl', f'{url}'], capture_output=True, text=True, timeout=1, shell=False
        )
        print(response.stdout)
        return 'Success!!! Response: ' + response.stdout
    except subprocess.TimeoutExpired:
        return 'Timeout !!!'
    
@app.route('/admin', methods=['GET'])
def admin():
    key = request.args.get('key', '').strip()
    print(md5(key.encode()).hexdigest(), secret)
    if str(md5(key.encode()).hexdigest()) == secret:
        return FLAG
    else:
        return 'Wrong key'


app.run(host='0.0.0.0', port=8000)
