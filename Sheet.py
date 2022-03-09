# A class to hold the twine card information
import json, utils
from bs4 import BeautifulSoup
import re
from tableDefines import columnTemplate 

class Sheet():
    def __init__(self, id):
        self._name = None
        self._id = id
        
    def init(self, index):
        placeholder = 'placeholder'

    def getId(self):
        return self._id

    def debugPrint(self):
        print(str(self._id))