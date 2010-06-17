#!/usr/bin/env python
# coding: utf-8

from BeautifulSoup import BeautifulSoup #HTML Parser
from urllib2 import urlopen
from datetime import date
import re

class VimScript(object):
    def __init__(self, name = '', version=1.0, date=date.today(),
            vimVersion=7.2, author = '', description = ''):
        self.name = name
        self.version = version
        self.date = date
        self.vimVersion = vimVersion
        self.author = author
        self.description = description

if __name__ == "__main__":
    page = urlopen('http://www.vim.org/scripts/script.php?script_id=273')
    soup = BeautifulSoup(page)
    downloadSpan = soup.findAll(name='span', attrs={'class' : 'txth2'})
    downloadLink = soup.find(href=re.compile('download_script'))
    print downloadLink.parent
