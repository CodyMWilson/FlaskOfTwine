# A class to hold the twine card information
import json, utils
from bs4 import BeautifulSoup


class Card():
    def __init__(self, html, index):
        self._bareHtml = html
        self._index = index
        self._indexNext = index + 1

        self._name = None
        self._body = None

        self._branchNum = None

        self._tags= None
        self._tagsWav = None
        self._tagsFuz = None
        
        # Set based on other options
        self._lineColor = None


    def init(self):
        soup = BeautifulSoup(self._bareHtml, 'html5lib')
        #print(soup)


