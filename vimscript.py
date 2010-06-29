#!/usr/bin/env python
# coding: utf-8

from datetime import date

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
        import tempfile
        import os.path
        import re
        from urllib import urlretrieve
        from urllib2 import urlopen
        from BeautifulSoup import BeautifulSoup #HTML Parser
        soup = BeautifulSoup(urlopen(self.url))
        downloadElt = soup.find(href=re.compile('download_script'))
        downloadLink = os.path.join('http://www.vim.org/scripts', downloadElt['href'])
        print "Downloading {0}...".format(downloadElt.string)
        tempdir = tempfile.mkdtemp()
        filepath = '/'.join([tempdir, downloadElt.string])
        urlretrieve(downloadLink, filepath)
        return filepath

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
            self.files = [member.filename for member in archive.infolist() if
                    not member.filename[-1] == '/']
            archive.extractall('/home/chris/.vim')
        elif ext == u'.tar' or ext == u'.tgz' or ext == u'.bz2':
            import tarfile
            archive = tarfile.open(filepath)
            self.files = [member.name for member in archive.getmembers() if
                    member.isfile()]
            archive.extractall('/home/chris/.vim')
        elif (ext == u'.gz' or ext == u'.bz2') and (os.path.splitext(root)[1] ==
                u'.tar'):
            import tarfile
            archive = tarfile.open(filepath)
            self.files = [member.name for member in archive.getmembers() if
                    member.isfile()]
            archive.extractall('/home/chris/.vim')
        elif ext == u'.vba':
            vimExecute(':so %\n:q\n')
            self.files=[filepath]
        # Cleanup
        print "Deleting {0} and {1}".format(filepath, os.path.dirname(filepath))
        os.unlink(filepath)
        os.rmdir(os.path.dirname(filepath))

    def install(self):
        """Download and unpack the script into the vim runtime directory.
        """
        filepath = self._download()
        self._unpack(filepath)
        vimExecute(':helptags /home/chris/.vim/doc\n:q\n')
        #self._unpack(u'/home/chris/Downloads/taglist_45.tar')

    def uninstall(self):
        import os
        import os.path
        if os.path.splitext(self.files[0])[1] == '.vba':
            vimExecute(':RmVimball {0}\n:q\n'.format(self.files[0]))
        else:
            print "Deleting {0}".format([os.path.join('/home/chris/.vim',
                filename) for filename in self.files])
            for filename in self.files:
                filepath = os.path.join('/home/chris/.vim', filename)
                os.unlink(filepath)
        vimExecute(':helptags /home/chris/.vim/doc\n:q\n')

def vimExecute(command):
    from subprocess import Popen
    from tempfile import NamedTemporaryFile
    import os
    # Create a temporary file with a vim script which sources the
    # vimball then quits vim. Open the vimball with vim and run the
    # script.
    scriptFile = NamedTemporaryFile(mode='w', delete=False)
    scriptFile.write(command)
    scriptFile.close()
    vim = Popen('vim' + ' -s {0}'.format(scriptFile.name),
            shell=True)
    vim.wait()
    os.unlink(scriptFile.name)


if __name__ == "__main__":
    script = VimScript('slimv',
            'http://www.vim.org/scripts/script.php?script_id=2531')
    script.install()
    script.uninstall()

