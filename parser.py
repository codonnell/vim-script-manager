#!/usr/bin/env python
# coding: utf-8

import vim

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
