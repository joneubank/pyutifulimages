from bs4 import BeautifulSoup
import urllib2

from colorz import Color
import colorz

def letThemGo():
    return [
        Color(41, 33, 82),
        Color(20, 86, 99),
        Color(220, 42, 94),
        Color(249, 146, 79),
        Color(245, 243, 202)
    ]


def ulquiorra():
    return [
        Color(238, 241, 232),
        Color(167, 193, 170),
        Color(78, 131, 85),
        Color(57, 88, 82),
        Color(34, 51, 59)
    ]


def vivacious():
    [
        Color(204, 12, 57),
        Color(230, 120, 30),
        Color(200, 207, 2),
        Color(248, 252, 193),
        Color(22, 147, 167),
    ]


def randpallette(num):
    output = []
    for i in range(0, num):
        output.append(colorz.randcolor())
    return output

# ############################################
# This section contains code for getting 
# pallettes from the site www.colourlovers.com
# --------------------------------------------

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


def getFromColourLovers(num):
    url = BASEURL_PALLETTE + str(num)
    html = httpGetUrl(url)
    pallette = parsePalletteColors(html)
    return pallette



def main():
    print randpallette(7)

if __name__ == '__main__':
    main()
