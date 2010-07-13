#!/usr/bin/env python
# coding: utf-8

from parser import parseSearchPage

class SearchResult(object):
    def __init__(self, name, url, category, rating, downloads, description):
        self.name = name
        self.url = url
        self.category = category
        self.rating = rating
        self.downloads = downloads
        self.description = description

    def __str__(self):
        return u'{0}/{1} {2}: {3}'.format(self.rating, self.downloads, self.name,
                self.description)

class Search(object):
    def __init__(self, term):
        self.term = term
        self.results = []

        from urllib2 import urlopen
        from ClientForm import ParseResponse
        response = urlopen('http://www.vim.org/search.php')
        searchForm = ParseResponse(response, backwards_compat=False)[3]
        searchForm['keywords'] = self.term
        resultsPage = urlopen(searchForm.click())
        self.results = parseSearchPage(resultsPage)

        for result in self.results:
            print unicode(result)

if __name__ == "__main__":
    search = Search('taglist')
