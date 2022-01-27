import os
from flask import Flask, render_template, request, redirect, url_for

import newsheet

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

print("hello from python!")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uploaded_file = None

@app.route('/', methods=['GET'])
def index():    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print("saved!")
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))

    if request.form['Run Convertor'] == 'Do Something':
        test('test')   

    return redirect(url_for('index'))

def test(val):
    print(val)