from __future__ import print_function

import os.path


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import gspread
from google.oauth2.credentials import Credentials
import pandas as pd

# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = "" 
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    client = gspread.authorize(creds)

    try:
        #service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
    
        #newSheet = client.create("testSheet")

        #newSheet.add_worksheet(title="Sheet2", rows="10", cols="10", index=0)
       import glob
       import json, utils
       from bs4 import BeautifulSoup

       for file in glob.glob("*.html"):
           with open(file, 'r') as html_file: 

               soup = BeautifulSoup(html_file, 'html5lib') 

               table = soup.find('script')#, attrs = {'id':'script'})
               print(table)
               
               for row in soup.findAll('tw-passagedata'):
                   print(row.text.strip())
               #html = html_file.read()
               #jsonData = xmltojson.parse(html)
               print(file)

       import pprint
       pp = pprint.PrettyPrinter(width=41, compact=True)
       #print(jsonData) 
       #pp.pprint(jsonData)

    except Exception as e:
        print('Failed to create sheet due to ' + str(e))

if __name__ == '__main__':
    main()
