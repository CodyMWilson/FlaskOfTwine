# A class to hold the twine card information
import json, utils
from bs4 import BeautifulSoup
import re

class Card():
    def __init__(self, bsTag):
        self._bsTag = bsTag
        self._name = None
        self._body = None

        self._branchNum = 0
        self._branches = []

        self._tags= None
        self._tagsWav = None
        self._tagsFuz = None
        self._tagsList = []

        # Set based on other options
        self._lineColor = None

        self._index = None
        self._indexNext = None

    def init(self, index):
        self._index = index
        self._indexNext = index + 1

        soup = self._bsTag
        self._body = soup.string
        self._name = soup['name']
        self._tags = soup['tags']
        
        # Returns a list of strings that were separated by space
        # Loop over these to find special cases
        for word in self._tags.split(' '):
            # TODO would be nice to not be case-sensitive 
            if (word.find('.wav') != -1):
                self._tagsWav = word
                break
            if (word.find('.fuz') != -1):
                self._tagsFuz = word
                break
            self._tagsList.append(word)
        
        # Find branches using the text string
        branches = re.findall('\[\[.*?\]\]', self._body)
        for branch in branches:
            # Strip the characters '[' and ']' and record how many branches there are
            branch = re.sub('[\[\]]','',branch)
            self._branches.append(branch)
            self._branchNum += 1

        self.debugPrint() 


    def debugPrint(self):
        
        # This will print out the tag definitions that we know will come from Twine for convenience
        soup = self._bsTag 
        print(soup)
        print('body is -' + str(soup.string))
        print('index is -' + str(self._index))
        print('name is -' + str(soup['name']))
        print('tags are -' + str(soup['tags']))
        print('this is card -' + str(self._index) + ' with these ' +str(self._branchNum) + ' branches ' + str(self._branches)) 
