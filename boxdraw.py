# import random
import imgutil
import colorz
# from color import Color

import time

from PIL import Image
# from PIL import ImageColor
from PIL import ImageDraw


def makeBlank(width, height, color=colorz.std['BLACK']):
    return Image.new("RGBA", (width, height), color.rgb())


# tilesWide is number of tiles horizontaly
# tilesHigh is number of tiles veritcally
# tileSize is pixels per tile, both horizontal and vertical
def makeSquareGrid(tilesWide, tilesHigh, tileSize):
    width = tilesWide*tileSize
    height = tilesHigh*tileSize

    im = makeBlank(width, height)
    draw = ImageDraw.Draw(im, "RGBA")

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            r = [x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize]
            draw.rectangle(r, fill=colorz.randcolor(min=20, max=235).rgba())

    return im


def main():

    im = makeSquareGrid(12, 12, 85)
    imgutil.save(
        im,
        "created/grid/",
        str(time.strftime("%Y%m%d%H%M%S")) + ".png"
        )

    pass

if __name__ == '__main__':
    main()
