# A class to hold the twine card information
import json, utils
from bs4 import BeautifulSoup


class Card():
    def __init__(self, html):
        self._bareHtml = html
        self._name = None
        self._body = None

        self._branchNum = None

        self._tags= None
        self._tagsWav = None
        self._tagsFuz = None
        
        # Set based on other options
        self._lineColor = None

        self._index = None
        self._indexNext = None


    def init(self, index):
        self._index = index
        self._indexNext = index + 1

        soup = BeautifulSoup(self._bareHtml, 'html5lib')
        
        print(soup)
        print('body is ' + str(soup.text.strip()))
        print('index is ' + str(self._index))
        print('name is ' + str(soup.find(attr = 'name')))
        print('tags are ' + str(soup.find('tags')))

        #print(soup)


