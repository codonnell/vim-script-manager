#!/usr/bin/env python
# coding: utf-8

import vim

def parseScriptPage(script):
    import BeautifulSoup
    import re
    from urllib2 import urlopen
    from datetime import date
    soup = BeautifulSoup.BeautifulSoup(urlopen(url))
    downloadLink = soup.find(href=re.compile('download_script'))
    # Version
    versionEntry = downloadLink.parent.nextSibling.nextSibling
    script.version = float(versionEntry.contents[0].string)
    # Date
    dateEntry = versionEntry.nextSibling.nextSibling
    dateString = dateEntry.contents[0].string
    dateList = dateString.split('-')
    dateList = [int(x) for x in dateList]
    script.uploadDate = date(*dateList)
    # Vim Version
    vimEntry = dateEntry.nextSibling.nextSibling
    script.vimVersion = float(vimEntry.string)
    # Author
    authorEntry = vimEntry.nextSibling.nextSibling
    script.author = authorEntry.contents[0].contents[0].string
    # Short Description
    descriptionEntry = authorEntry.nextSibling.nextSibling
    description = [string.strip() for string in descriptionEntry.contents if
            isinstance(string, BeautifulSoup.NavigableString)]
    script.description = u' '.join(description)
    return script

def parseScriptPage(url):
    import BeautifulSoup
    import re
    from urllib2 import urlopen
    from datetime import date
    soup = BeautifulSoup.BeautifulSoup(urlopen(url))
    downloadLink = soup.find(href=re.compile('download_script'))
    # Version
    versionEntry = downloadLink.parent.nextSibling.nextSibling
    version = float(versionEntry.contents[0].string)
    # Date
    dateEntry = versionEntry.nextSibling.nextSibling
    dateString = dateEntry.contents[0].string
    dateList = dateString.split('-')
    dateList = [int(x) for x in dateList]
    uploadDate = date(*dateList)
    # Vim Version
    vimEntry = dateEntry.nextSibling.nextSibling
    vimVersion = float(vimEntry.string)
    # Author
    authorEntry = vimEntry.nextSibling.nextSibling
    author = authorEntry.contents[0].contents[0].string
    # Short Description
    descriptionEntry = authorEntry.nextSibling.nextSibling
    description = [string.strip() for string in descriptionEntry.contents if
            isinstance(string, BeautifulSoup.NavigableString)]
    descriptionString = u' '.join(description)
    return VimScript('script', url, version, uploadDate, vimVersion, author,
            descriptionString)

if __name__ == "__main__":
    parseScriptPage('http://www.vim.org/scripts/script.php?script_id=273')
