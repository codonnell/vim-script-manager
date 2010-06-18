#!/usr/bin/env python
# coding: utf-8

from BeautifulSoup import BeautifulSoup #HTML Parser
from urllib2 import urlopen
from datetime import date
import re

class VimScript(object):
    def __init__(self, name='', url='', version=1.0, uploadDate=date.today(),
            vimVersion=7.2, author = '', description = '', files=[]):
        self.name = name
        self.url = url
        self.version = version
        self.uploadDate = date
        self.vimVersion = vimVersion
        self.author = author
        self.description = description
        self.files = files

    def _download(self):
        """Downloads the vim script using its url attr.
        """
        import os.path
        from urllib import urlretrieve
        print self.url
        soup = BeautifulSoup(urlopen(self.url))
        downloadElt = soup.find(href=re.compile('download_script'))
        downloadLink = os.path.join('http://www.vim.org/scripts', downloadElt['href'])
        print downloadLink
        filepath = '/'.join(['/home/chris/Downloads', downloadElt.string])
        urlretrieve(downloadLink, filepath)
        return filepath

    #TODO: Extract vimballs and extract to the correct directory.
    #TODO: Correctly determine to which directory .vim files should be moved.
    def _unpack(self, filepath):
        """Determines the vim script's extension and unpacks it. Also sets the
        files variable.
        """
        import os.path
        root, ext = os.path.splitext(filepath)
        if ext == u'.zip':
            from zipfile import ZipFile
            archive = ZipFile(filepath, 'r')
            self.files = [member.filename for member in archive.infolist()]
            archive.extractall(root)
        elif ext == u'.tar' or ext == u'.tgz' or ext == u'.bz2':
            import tarfile
            archive = tarfile.open(filepath)
            self.files = [member.name for member in archive.getmembers() if
                    member.isfile()]
            archive.extractall(root)
        elif (ext == u'.gz' or ext == u'.bz2') and os.path.splitext(root)[1] == u'.tar':
            import tarfile
            archive = tarfile.open(filepath)
            self.files = [member.name for member in archive.getmembers() if
                    member.isfile()]
            archive.extractall(os.path.splitext(root)[0])
        elif ext == u'.vba':
            import subprocess
            import tempfile
            import os
            scriptFile = tempfile.NamedTemporaryFile(mode='w', delete=False)
            scriptFile.write(':so %\n:q\n')
            scriptFile.close()
            vim = subprocess.Popen('vim' + ' -s {0} {1}'.format(scriptFile.name, filepath), shell=True)
            print vim.wait()
            os.unlink(scriptFile.name)
            

    def install(self):
        """Download and unpack the script into the vim runtime directory.
        """
        filepath = self._download()
        self._unpack(filepath)
        #self._unpack(u'/home/chris/Downloads/taglist_45.tar')
        

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
            url='http://www.vim.org/scripts/script.php?script_id=1318')
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
    # import subprocess
    # vim = subprocess.Popen(['vim', '-S #FILENAMEHERE'])# :q<cr>'])
    # vim.communicate(':e test.txt')
    # vim.communicate(':w')
    # vim.terminate()
