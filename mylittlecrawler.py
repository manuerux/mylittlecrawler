# -*- coding: UTF-8 -*-
USER_AGENT = "5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gec\
ko) Ubuntu/10.10 Chromium/11.0.696.0 Chrome/11.0.696.0 Safari/534.24"

from BeautifulSoup import BeautifulSoup as Soup
import argparse
import urllib2
import os

_opener = urllib2.build_opener()
_opener.addheaders = [('user-agent',USER_AGENT)]

parser = argparse.ArgumentParser(description = "Living on a crawler!!!!!")

parser.add_argument("url", nargs=1, help = "target URL")

parser.add_argument("-n", "--number-of-levels", type = int, default = 1,
 help="You have to specify the levels you want")

args = parser.parse_args()

target_url = args.url.pop()

deep = args.number_of_levels

target_aux = "http://www.calcifer.org/documentos/librognome/gtktextview\
.html#gtktextview-text-management"

def deeper(target_url, deep):
    """Search in all link recursively from a web page.
    
    Keyword arguments:
    target_url -- the url of the page to analyse
    deep -- Number of links from the links of start page
    
    """
    try:
       raw_code = _opener.open(target_url).read()
       
    except urllib2.URLError:
        print "there was a mistake in the process of looking up  " + target_url
        return False
        
    soup_code = Soup(raw_code)
    
    #esto imprimiria divs.
    #divs = [div for div in soup_code.findAll('div') if div.get('class') == "sect1"]
    
    links = [link['href'] for link in soup_code.findAll('a') if link.has_key('href')]
    for link in links:
        if '#' not in link and "mailto" not in link:
            if deep > 1:
                if not "http" in link:
                    next = target_url.rfind("/")+1
                    link = target_url[0:next]+link
                    #print link
                    print "+-"+link +" profundidad: " + str(deep)
                    
                deeper(link,deep-1)
            else:
                print link +" profundidad: " + str(deep)

deeper(target_url,deep)
