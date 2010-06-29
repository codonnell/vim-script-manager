#!/usr/bin/env python
# coding: utf-8

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

        import BeautifulSoup
        import re
        soup = BeautifulSoup.BeautifulSoup(resultsPage,
                convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
        header = soup.find(text='Search Results')
        resultsTable = header.parent.nextSibling.nextSibling
        # Removes line break entries
        scriptsTable = [entry for entry in resultsTable.contents if not
                isinstance(entry, BeautifulSoup.NavigableString)]
        scriptsTable = scriptsTable[2:-1]
        for scriptEntry in scriptsTable:
            scriptEntry = [entry for entry in scriptEntry if not
                    isinstance(entry, BeautifulSoup.NavigableString)]
            urlEntry = scriptEntry[0]
            name = urlEntry.contents[0].string
            print name
            url = '/'.join(['http://www.vim.org/scripts',
                urlEntry.contents[0]['href']])
            category = scriptEntry[1].string
            rating = int(scriptEntry[2].string)
            downloads = int(scriptEntry[3].string)
            description = scriptEntry[4].contents[0].string
            self.results.append(SearchResult(name, url, category, rating,
                downloads, description))

        for result in self.results:
            print unicode(result)

if __name__ == "__main__":
    search = Search('taglist')
