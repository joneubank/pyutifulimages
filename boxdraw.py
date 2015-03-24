import random
import imgutil
import colorz
from colorz import Color
import pallettes

import time
import math

from PIL import Image
# from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFilter


def makeBlank(width, height, color=colorz.std['BLACK']):
    return Image.new("RGBA", (width, height), color.rgba())


# tilesWide is number of tiles horizontaly
# tilesHigh is number of tiles veritcally
# tileSize is pixels per tile, both horizontal and vertical
def makeSquareGrid(
    tilesWide, tilesHigh, tileSize, colorrange=(0, 255, 0, 255, 0, 255)
):
    width = tilesWide*tileSize
    height = tilesHigh*tileSize

    im = makeBlank(width, height)
    draw = ImageDraw.Draw(im, "RGBA")

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            r = [x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize]
            draw.rectangle(r, fill=colorz.randcolorrange(colorrange=colorrange).rgba())

    return im

# makeSquareGrid usage Example:
# colorrange = (200, 255, 0, 100, 50, 150)
# im = makeSquareGrid(10, 10, 100, colorrange=colorrange)
# filename = str(time.strftime("%Y%m%d%H%M%S")) + str(colorrange) + ".png"
# imgutil.save(im, "created/grid/", filename)


def makeSquareGridGradientSides(
    tilesWide, tilesHigh, tileSize,
    top=(0, 255, 0, 255, 0, 255),
    bottom=(0, 255, 0, 255, 0, 255),
    left=(0, 255, 0, 255, 0, 255),
    right=(0, 255, 0, 255, 0, 255)
):
    width = tilesWide*tileSize
    height = tilesHigh*tileSize

    im = makeBlank(width, height)
    draw = ImageDraw.Draw(im, "RGBA")

    xDelta = (
        (left[0]-right[0])/tilesWide,
        (left[1]-right[1])/tilesWide,
        (left[2]-right[2])/tilesWide,
        (left[3]-right[3])/tilesWide,
        (left[4]-right[4])/tilesWide,
        (left[5]-right[5])/tilesWide
        )

    print xDelta

    yDelta = (
        (top[0]-bottom[0])/tilesHigh,
        (top[1]-bottom[1])/tilesHigh,
        (top[2]-bottom[2])/tilesHigh,
        (top[3]-bottom[3])/tilesHigh,
        (top[4]-bottom[4])/tilesHigh,
        (top[5]-bottom[5])/tilesHigh
        )

    print yDelta

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            useRange = (
                (top[0] + left[0] - xDelta[0]*(x+1) - yDelta[0]*(y+1))/2,
                (top[1] + left[1] - xDelta[1]*(x+1) - yDelta[1]*(y+1))/2,
                (top[2] + left[2] - xDelta[2]*(x+1) - yDelta[2]*(y+1))/2,
                (top[3] + left[3] - xDelta[3]*(x+1) - yDelta[3]*(y+1))/2,
                (top[4] + left[4] - xDelta[4]*(x+1) - yDelta[4]*(y+1))/2,
                (top[5] + left[5] - xDelta[5]*(x+1) - yDelta[5]*(y+1))/2,
                )
            r = [x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize]
            draw.rectangle(r, fill=colorz.randcolorrange(colorrange=useRange).rgba())

    return im



def makeSquareGridGradientCorners(
    tilesWide, tilesHigh, tileSize,
    topLeft=(0, 255, 0, 255, 0, 255),
    bottomLeft=(0, 255, 0, 255, 0, 255),
    topRight=(0, 255, 0, 255, 0, 255),
    bottomRight=(0, 255, 0, 255, 0, 255)
):
    width = tilesWide*tileSize
    height = tilesHigh*tileSize

    im = makeBlank(width, height)
    draw = ImageDraw.Draw(im, "RGBA")

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            
            maxd = (tilesHigh+tilesWide)/2

            xn = tilesWide-1-x
            yn = tilesWide-1-y

            tld = maxd-math.sqrt(x*x+y*y)
            trd = maxd-math.sqrt(xn*xn+y*y)
            bld = maxd-math.sqrt(x*x+yn*yn)
            brd = maxd-math.sqrt(xn*xn+yn*yn)

            # maxd = tilesWide*tilesWide+tilesHigh*tilesHigh
            # tld = maxd-(x*x+y*y)
            # trd = maxd-(xn*xn+y*y)
            # bld = maxd-(x*x+yn*yn)
            # brd = maxd-(xn*xn+yn*yn)

            if tld < 0: tld = 0
            if trd < 0: trd = 0
            if bld < 0: bld = 0
            if brd < 0: brd = 0

            totald = tld+trd+bld+brd

            tlr = tld/totald
            trr = trd/totald
            blr = bld/totald
            brr = brd/totald

            # print x, xratio

            useRange = (
                (topLeft[0]*tlr + topRight[0]*trr + bottomLeft[0]*blr + bottomRight[0]*brr),
                (topLeft[1]*tlr + topRight[1]*trr + bottomLeft[1]*blr + bottomRight[1]*brr),
                (topLeft[2]*tlr + topRight[2]*trr + bottomLeft[2]*blr + bottomRight[2]*brr),
                (topLeft[3]*tlr + topRight[3]*trr + bottomLeft[3]*blr + bottomRight[3]*brr),
                (topLeft[4]*tlr + topRight[4]*trr + bottomLeft[4]*blr + bottomRight[4]*brr),
                (topLeft[5]*tlr + topRight[5]*trr + bottomLeft[5]*blr + bottomRight[5]*brr),
                )

            # print x, y, tld, trd, bld, brd, totald, tlr, trr, blr, brr, useRange

            r = [x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize]
            draw.rectangle(r, fill=colorz.randcolorrange(colorrange=useRange).rgba())

    return im

    #Corner Gradient Usage Example:

    # rangeRed = (220, 255, 0, 25, 0, 25)
    # rangeBlue = (0, 25, 0, 25, 220, 255)
    # rangeGreen = (0, 25, 220, 255, 0, 25)
    # rangeOrange = (220, 255, 125, 175, 0, 25)
    # rangeYellow = (220, 255, 220, 255, 0, 25)
    # rangeHigh = (100, 255, 100, 255, 100, 255)
    # rangeLow = (0, 25, 0, 25, 0, 25)
    # rangeNoBlue = (0, 255, 0, 255, 0, 0)
    # rangeWhite = (220, 255, 220, 255, 220, 255)
    # rangePureWhite = (255, 255, 255, 255, 255, 255)
    # rangeBlack = (0, 25, 0, 25, 0, 25)
    # rangePureBlack = (0, 0, 0, 0, 0, 0)

    # im = makeSquareGridGradientCorners(100,100, 10, topLeft=Color(41,33,82).rgbrange(20), bottomRight=Color(30,86,99).rgbrange(20), topRight=Color(220,42,94).rgbrange(20), bottomLeft=Color(246,146,79).rgbrange(20))


def makeSquareGridPallette(
    tilesWide, tilesHigh, tileSize,
    pallette=[Color(0,0,0)], variance=255
):
    width = tilesWide*tileSize
    height = tilesHigh*tileSize

    im = makeBlank(width, height)
    draw = ImageDraw.Draw(im, "RGBA")

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):

            useColor = random.randint(0,len(pallette)-1)
            useRange = pallette[useColor].rgbrange(variance)

            r = [x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize]
            draw.rectangle(r, fill=colorz.randcolorrange(colorrange=useRange).rgba())

    return im


def addGridShadows(
    image,
    tilesWide, tilesHigh, tileSize,
    color=colorz.std['BLACK'], thickness=5, blurIters=0
):
    overlay = makeBlank(tilesWide*tileSize, tilesHigh*tileSize, color=Color(255, 255, 255,a=0))
    draw = ImageDraw.Draw(overlay, image.mode)
    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            if(x != 0):
                width = thickness*random.choice([1, -1])
                vertrect = [x*tileSize, y*tileSize, x*tileSize+width, (y+1)*tileSize]
                draw.rectangle(vertrect, fill=color.rgba())

            if(y != 0):
                width = thickness*random.choice([1, -1])
                horzrect = [x*tileSize, y*tileSize, (x+1)*tileSize, y*tileSize+width]
                draw.rectangle(horzrect, fill=color.rgba())
    
    for i in range(blurIters):
        overlay = overlay.filter(ImageFilter.BLUR)

    image.paste(overlay, (0,0), overlay)
    return image


def drawGradient():
    pass

def main():

    # randomPallette = [Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))]
    # randomPallette4 = [
    # Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    # Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    # Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    # Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    # ]

    # for c in randomPallette4:
    #     print c.__unicode__()


    # im = makeSquareGridPallette(8,5,320, pallette=pallettes.getFromColourLovers(1283145), variance=15)

    colorrange = (100, 255, 0, 100, 0, 200)
    im = makeSquareGrid(10, 10, 100, colorrange=colorrange)
    im = addGridShadows(im, 10, 10, 100,color=Color(0,0,0,100),thickness=6)
    filename = str(time.strftime("%Y%m%d%H%M%S")) + str(colorrange) + ".png"
    imgutil.save(im, "created/grid/dropshadows/", filename)
    im.show()
    pass

if __name__ == '__main__':
    main()
