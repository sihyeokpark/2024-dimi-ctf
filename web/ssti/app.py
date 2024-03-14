from flask import *

app = Flask(__name__)
app.config['FLAG'] = 'DIMI{ssT1_is_n0t_Super_Super_Terrible_1nj3ction}'

users = {
    'exon': 'exonisgod',
    'guest': 'guest'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            form_id = request.form['id']
            form_pw = request.form['pw']
            
            if len(form_id) > 10 or len(form_pw) > 10:
                return render_template_string('Too long')
            if form_id in users.keys():
                if users[form_id] == form_pw:
                    return render_template_string('welcome ' + form_id + '!')
                return render_template_string('{form_pw} is incorrect password.'.format(form_pw=form_pw))
            else:
                return render_template_string('It is not registered id.')
    except:
        return render_template_string('Error')
    
app.run(host='0.0.0.0', port=13000, threaded=False)