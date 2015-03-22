from bs4 import BeautifulSoup
import urllib2
from colorz import Color

BASEURL_PALLETTE = "http://www.colourlovers.com/palette/"


def httpGetUrl(url):
    attempts = 0
    while attempts < 10:
        try:
            print "pyutifulimages.colourlovers.py - Attempting to get url: " + url

            response = urllib2.urlopen(url)
            html = response.read()
            print("httpGetUrl success")
            return html
        except urllib2.HTTPError as e:
            print("HTTPError occured: " + str(e.code))
            raise
        except urllib2.URLError as e:
            print("URL Error occured: " + str(e.reason))
            raise

# returns pallette with colors from html
def parsePalletteColors(html):
    output = []
    
    dom = BeautifulSoup(html)
    
    colorWrappers = dom('div',{'class':'col-80'})
    for cw in colorWrappers:
        colorInfoString = str(cw('h4')[0])
        colorInfo = colorInfoString.partition('>')[2].partition('<')[0].split(',')
        c = Color(int(colorInfo[0]), int(colorInfo[1]), int(colorInfo[2]))
        output.append(c)

    return output


def getPallette(num):
    url = BASEURL_PALLETTE + str(num)
    html = httpGetUrl(url)
    pallette = parsePalletteColors(html)
    return pallette


def main():
    html = httpGetUrl("http://www.colourlovers.com/palette/557560")
    parsePalletteColors(html)

if __name__ == '__main__':
    main()