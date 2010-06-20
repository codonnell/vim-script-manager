#!/usr/bin/env python
# coding: utf-8

from vimscript import VimScript

class Vim(object):
    def __init__(self, scripts=None):
        if scripts is None:
            scripts = []
        self.scripts = scripts

    #TODO: Add a force install option at command line
    def addScript(self, script):
        if not script.name in [script.name for script in self.scripts]:
            if script.url:
                script.install()
                self.scripts.append(script)
            else:
                print "At the moment, we need a url to install scripts."
        else:
            print "This script is already installed."

    def removeScript(self, script):
        if script.name in [script.name for script in self.scripts]:
            script.uninstall()
            self.scripts = [installedScript for installedScript in self.scripts if
                    installedScript.name != script.name]
        else:
            print "This script is not installed"

if __name__ == "__main__":
    taglist = VimScript('taglist',
            'http://www.vim.org/scripts/script.php?script_id=273')
    vim = Vim()
    vim.addScript(taglist)
    #vim.removeScript(taglist)
