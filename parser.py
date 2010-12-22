#!/usr/bin/env python
# coding: utf-8

import vim
import BeautifulSoup
import re

def parseScriptPage(script):
    """Parses the page for a passed-in script.
    """
    resultScript = VimScript(script.name, script.url)
    from urllib2 import urlopen
    from datetime import date
    soup = BeautifulSoup.BeautifulSoup(urlopen(script.url))
    downloadLink = soup.find(href=re.compile('download_script'))
    # Version
    versionEntry = downloadLink.parent.nextSibling.nextSibling
    resultScript.version = float(versionEntry.contents[0].string)
    # Date
    dateEntry = versionEntry.nextSibling.nextSibling
    dateString = dateEntry.contents[0].string
    dateList = dateString.split('-')
    dateList = [int(x) for x in dateList]
    resultScript.uploadDate = date(*dateList)
    # Vim Version
    vimEntry = dateEntry.nextSibling.nextSibling
    resultScript.vimVersion = float(vimEntry.string)
    # Author
    authorEntry = vimEntry.nextSibling.nextSibling
    resultScript.author = authorEntry.contents[0].contents[0].string
    # Short Description
    descriptionEntry = authorEntry.nextSibling.nextSibling
    description = [string.strip() for string in descriptionEntry.contents if
            isinstance(string, BeautifulSoup.NavigableString)]
    resultScript.description = u' '.join(description)
    return resultScript

def parseScriptPage(url):
    """Parses the script whose page is at a passed-in url.
    """
    from urllib2 import urlopen
    from datetime import date
    soup = BeautifulSoup.BeautifulSoup(urlopen(url))
    name = soup.title.string.partition(' - ')
    return parseScriptPage(VimScript(name, url))

def parseSearchPage(resultsPage):
    """Parses a search and returns a list of SearchResult's.
    """
    from search import SearchResult
    results = []
    soup = BeautifulSoup.BeautifulSoup(resultsPage,
            convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
    header = soup.find(text='Search Results')
    resultsTable = header.parent.nextSibling.nextSibling
    # Removes line break entries
    scriptsTable = withoutNavigableStrings(resultsTable.contents)
    # Remove header and footer entries
    scriptsTable = scriptsTable[2:-1]
    for scriptEntry in scriptsTable:
        scriptEntry = withoutNavigableStrings(scriptEntry)
        urlEntry = scriptEntry[0]
        name = urlEntry.contents[0].string
        url = '/'.join(['http://www.vim.org/scripts',
            urlEntry.contents[0]['href']])
        category = scriptEntry[1].string
        rating = int(scriptEntry[2].string)
        downloads = int(scriptEntry[3].string)
        description = scriptEntry[4].contents[0].string
        results.append(SearchResult(name, url, category, rating, downloads,
            description))
    return results

def withoutNavigableStrings(coll):
    return [entry for entry in coll if not isinstance(entry,
        BeautifulSoup.NavigableString)]
    

if __name__ == "__main__":
    parseScriptPage('http://www.vim.org/scripts/script.php?script_id=273')
