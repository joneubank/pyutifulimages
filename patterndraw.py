import random
import imgutil
import colorz
from colorz import Color
import pallettes
import time

from PIL import Image
# from PIL import ImageColor
from PIL import ImageDraw

# Like the github random avatars
def makeSymmetryBlocks(
    tilesWide, tilesHigh, tileSize,
     foreground, background, border=0
):
    im = imgutil.makeBlank(tilesWide*tileSize+border*2, tilesHigh*tileSize+border*2, color=background)
    draw = ImageDraw.Draw(im, "RGBA")

    odd = tilesWide%2 == 1
    half = tilesWide/2
    
    uniqueColumns = half
    if odd:
        uniqueColumns += 1

    grid = []
    for x in range(0, uniqueColumns):
        column = []
        for y in range(0, tilesHigh):
            column.append(bool(random.getrandbits(1)))
        grid.append(column)


    print grid
    for i in reversed(range(half)):
        grid.append(grid[i])    

    print grid

    for x in range(0, tilesWide):
        for y in range(0, tilesHigh):
            if(grid[x][y]):
                r = [x*tileSize+border, y*tileSize+border, (x+1)*tileSize+border, (y+1)*tileSize+border]
                draw.rectangle(r, fill=foreground.rgba())

    return im


def main():
    color = colorz.randcolor()
    im = makeSymmetryBlocks(3, 3, 50, color, color.invert(), border=20)

    filename = str(time.strftime("%Y%m%d%H%M%S")) +  "_3x3.png"
    imgutil.save(im, "created/pattern/sym/", filename)


if __name__ == '__main__':
    main()