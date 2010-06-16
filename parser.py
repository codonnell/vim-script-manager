#!/usr/bin/env python
# coding: utf-8

from HTMLParser import HTMLParser

class vimHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag, attrs):
        print "Encountered the end of a %s tag" % tag
