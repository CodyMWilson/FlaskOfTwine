import os
from flask import Flask, render_template, request, redirect, url_for

import newsheet
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'html'}

print("hello from python!")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uploaded_file_path = None

@app.route('/', methods=['GET'])
def index():    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
        
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return redirect(url_for('index'))
    uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
    print("saved! to " + str(uploaded_file_path) + ' and dir after glob:')
    test()

    if request.form['Run Convertor'] == "Do Something":
        newsheet.convert()
    #files = request.files.getlist("file[]")

    return redirect(url_for('index'))

def test():
    newsheet.testGlob()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)