import os
from flask import Flask, render_template, request, redirect, url_for
import flask

import newsheet
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)

# Testing google OAuth redirection
from google.auth.transport.requests import Request
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import gspread
from google.oauth2.credentials import Credentials
import flask, requests
import secrets

CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'html'}

print("hello from python!")

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uploaded_file_path = None

@app.route('/', methods=['GET'])
def index():    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    
    if request.form['Authorize'] == "Authorize":
        print("Authorize")
        return redirect(url_for('authorize'))

           
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

@app.route('/authorize')
def authorize():
  # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES)

  # The URI created here must exactly match one of the authorized redirect URIs
  # for the OAuth 2.0 client, which you configured in the API Console. If this
  # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
  # error.
  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  authorization_url, state = flow.authorization_url(
      # Enable offline access so that you can refresh an access token without
      # re-prompting the user for permission. Recommended for web server apps.
      access_type='offline',
      # Enable incremental authorization. Recommended as a best practice.
      include_granted_scopes='true')

  # Store the state so the callback can verify the auth server response.
  flask.session['state'] = state

  return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
  # Specify the state when creating the flow in the callback so that it can
  # verified in the authorization server response.
  state = flask.session['state']

  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  # Use the authorization server's response to fetch the OAuth 2.0 tokens.
  authorization_response = flask.request.url

  # For some reason request.url returns http: when we HAVE to use https: or Oauth2 will break.
  temp_var = authorization_response
  if "http:" in temp_var:
      temp_var = "https:" + temp_var[5:]
  authorization_response = temp_var

  flow.fetch_token(authorization_response=authorization_response)

  # Store credentials in the session.
  # ACTION ITEM: In a production app, you likely want to save these
  #              credentials in a persistent database instead.
  credentials = flow.credentials
  #flask.session['credentials'] = credentials_to_dict(credentials)

  return flask.redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)