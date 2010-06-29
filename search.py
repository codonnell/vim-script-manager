#!/usr/bin/env python
# coding: utf-8

class Search(object):
    def __init__(self, term):
        self.term = term

    def getResults(self):
        from urllib2 import urlopen
        from ClientForm import ParseResponse
        response = urlopen('http://www.vim.org/search.php')
        searchForm = ParseResponse(response, backwards_compat=False)[3]
        searchForm['keywords'] = self.term
        results = urlopen(searchForm.click())

        from BeautifulSoup import BeautifulSoup
        import re
        soup = BeautifulSoup(results)
        header = soup.find(text='Search Results')
