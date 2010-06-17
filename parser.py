#!/usr/bin/env python
# coding: utf-8

from BeautifulSoup import BeautifulSoup #HTML Parser
from urllib2 import urlopen
import re

#class vimHTMLParser(HTMLParser):
#    def __init__(self, url):
#        HTMLParser.__init__(self)
#        req = urlopen(url)
#        self.feed(req.read())
#
#    def handle_starttag(self, tag, attrs):
#        print "Encountered the beginning of a %s tag" % tag
#
#    def handle_endtag(self, tag):
#        print "Encountered the end of a %s tag" % tag
#
#    def handle_comment(self, data):
#        print "Encountered a comment: %s" % data

if __name__ == "__main__":
    page = urlopen('http://www.vim.org/scripts/script.php?script_id=273')
    soup = BeautifulSoup(page)
    downloadSpan = soup.findAll(name='span', attrs={'class' : 'txth2'})
    downloadLinks = soup.findAll(attrs={'href' : re.compile('download')})
    print downloadLinks
#    vimHTMLParser('file:/home/chris/coding/vim-script-manager/real_test.html')
