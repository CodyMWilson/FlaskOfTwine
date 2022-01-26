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

from Card import Card

debug = True

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
               
                #now that we have the data, we have some processing to do... 
                # 1 - the html option "tags" is ALL part of the alias box
               # 2 - anything in a 'tags' with .fuz or .wav extension is ignored
               # 3 - the html "name" is the card title and goes into the context box
               # 4 - body of html is the line of dialogue
               # 5 - each distinct character should have their own sheet generated (so each can have their own structure)
               # 6 - Each sheet needs to be created based on a template
               # 7 - Each sheet needs a quest name 
               # 8 - Each scene has a delineater between them, and scenes are cards that branch to four other cards
               # # Note that a branch means that a text option in the body of the option delineated by [[ .. ]] will be the name for another html tag (card
               # 9 - Cards with a single link can be put at the bottom in close to their original order.
               # 10 - Player choice sections need to be ordered
               # 11 - Character lines that flow un-interrupted are designated by having the same character have multiple linear branches and can all be boxed together
               # 12 - Lines are color coded and can be assigned during runtime

               # This means that as we process we need to keep track of the following for each of x characters:
               # 1 Individual lines w/
               # # Character speaking
               # # Branches
               # # Context
               # # 
               # 2 How many branches each line has
               # 3  

               # Implementation - 
               #  Each html (voice line/card) can be an object with number of links, line data, what the links are, color of the table, 

                # init required for variable scope outside of loop                
                cardList = []
                index = 0
                # Find every occurance of a twine 'card' as designated by the tw-passagedata attribute
                for row in soup.findAll('tw-passagedata'):
                    index += 1
                    # Create a structure with every card found from imported twine sheet
                    newCard = Card(row)
                    newCard.init(index)
                    cardList.append(newCard)
                print(cardList)
               
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
