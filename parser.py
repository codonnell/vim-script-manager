#!/usr/bin/env python
# coding: utf-8

from BeautifulSoup import BeautifulSoup #HTML Parser
from urllib2 import urlopen
from datetime import date
import re

class VimScript(object):
    def __init__(self, name='', url='', version=1.0, uploadDate=date.today(),
            vimVersion=7.2, author = '', description = ''):
        self.name = name
        self.url = url
        self.version = version
        self.uploadDate = date
        self.vimVersion = vimVersion
        self.author = author
        self.description = description

    def _download(self):
        """Downloads the vim script using its url attr.
        """
        print self.url
        soup = BeautifulSoup(urlopen(self.url))
        downloadElt = soup.find(href=re.compile('download_script'))
        downloadLink = '/'.join(['http://www.vim.org/scripts', downloadElt['href']])
        filepath = '/'.join(['/home/chris/Downloads', downloadElt.string])
        from urllib import urlretrieve
        urlretrieve(downloadLink, filepath)
        return filepath

    def _unpack(self, filepath):
        """Determines the vim script's extension and unpacks it.
        """
        import os.path
        root, ext = os.path.splitext(filepath)
        if ext == u'.zip':
            from zipfile import ZipFile
            archive = ZipFile(filepath, 'r')
            archive.extractall(root)
        elif ext == u'.tar':
            import tarfile
            archive = tarfile.open(filepath)
            archive.extractall(root)
        elif ext == u'.gz' and os.path.splitext(root)[1] == u'.tar':
            import tarfile
            archive = tarfile.open(filepath)
            archive.extractall(os.path.splitext(root)[0])

    def install(self):
        """Download and unpack the script into the vim runtime directory.
        """
        filepath = self._download()
        self._unpack(filepath)
        #self._unpack(u'/home/chris/Downloads/taglist_45.zip')
        

# TODO: Finish this parsing.
# def parseScriptPage(url):
#     soup = BeautifulSoup(urlopen(url))
#     downloadLink = soup.find(href=re.compile('download_script'))
#     versionEntry = downloadLink.parent.nextSibling.nextSibling
#     version = float(versionEntry.contents[0].string)
#     dateEntry = versionEntry.nextSibling.nextSibling
#     dateString = dateEntry.contents[0].string
#     dateList = dateString.split('-')
#     dateList = [int(x) for x in dateList]
#     uploadDate = date(*dateList)
#     return VimScript('script', url, version, uploadDate)

if __name__ == "__main__":
    taglist = VimScript(name='project',
            url='http://www.vim.org/scripts/script.php?script_id=69')
    # soup = BeautifulSoup(urlopen(taglist.url))
    # downloadSpan = soup.findAll(name='span', attrs={'class' : 'txth2'})
    # downloadLink = soup.find(href=re.compile('download_script'))
    # versionEntry = downloadLink.parent.nextSibling.nextSibling
    # taglist.version = versionEntry.contents[0].string
    # dateEntry = versionEntry.nextSibling.nextSibling
    # dateString = dateEntry.contents[0].string
    # dateList = dateString.split('-')
    # dateList = [int(x) for x in dateList]
    # taglist.date = date(*dateList)
    # print dateList
    # print taglist.date
    taglist.install()
