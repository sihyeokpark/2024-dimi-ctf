from flask import Flask, request, render_template_string, redirect, url_for, session
import os
import binascii

app = Flask(__name__)

app.secret_key = binascii.hexlify(os.urandom(24)).decode()

@app.route('/')
def home():
    return '''
        <style>
            body {
                background-color: #000;
                color: #fff;
                font-family: 'Arial', sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            h2, p {
                color: gold;
            }
            input[type="text"] {
                border: 2px solid gold;
                border-radius: 5px;
                padding: 10px;
                background-color: #222;
                color: gold;
            }
            input[type="submit"] {
                border: 2px solid gold;
                border-radius: 5px;
                padding: 10px 20px;
                background-color: gold;
                color: #000;
                cursor: pointer;
                font-weight: bold;
            }
            input[type="submit"]:hover {
                background-color: #ffd700;
            }
            form {
                margin-top: 20px;
            }
        </style>
        <h2>Welcome to the Ako's Casino!</h2>
        <p>Enter your name:</p>
        <form action="/welcome" method="POST">
            <input type="text" name="name" placeholder="Enter your name"/>
            <input type="submit" value="Submit"/>
        </form>
    '''

@app.route('/welcome', methods=['POST'])
def name_p():
    name = request.form.get('name', 'Guest')
    session['name'] = name
    if(len(name)>10):
        return "Too long "
    else:
        template = f'<p>Hello {name}!, u wanna play game??</p>'
        return render_template_string(template)

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    if request.method == 'POST':
        user_secret_key = request.form.get('secret_key')
        if user_secret_key == app.secret_key:
            return '''
                <p>Welcome VIP! Now you can read a flag:</p>
                <form action="/read_file" method="POST">
                    <input type="text" name="filename" placeholder="Enter file path"/>
                    <input type="submit" value="Read File"/>
                </form>
            '''
        else:
            return '<p>Incorrect secret key! <a href="/secret">Try again</a></p>'
    else:
        return '''
            <h2>Secret Key Required</h2>
            <form action="/secret" method="POST">
                <input type="text" name="secret_key" placeholder="Enter secret key"/>
                <input type="submit" value="Submit"/>
            </form>
        '''

@app.route('/read_file', methods=['POST'])
def read_file():
    filename = request.form.get('filename')
    file_path = os.path.join('fake', filename)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return f'<pre>{content}</pre>'
    except Exception as e:
        return f'Error reading file: {e}'

if __name__ == '__main__':
    app.run(debug=True)