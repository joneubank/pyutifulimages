import math
import time

import boxdraw
import pallettes
import imgutil
import random

SIZES_2560 = [320, 160, 80, 64, 40, 32, ]

def makeGridPallette(pallette, pixelSize, variance=15, width=2560, height=1600, path="/", name=(str(time.strftime("%Y%m%d%H%M%S"))+".png")):
    im = boxdraw.makeSquareGridPallette(int(math.ceil(width*1.0/pixelSize)),int(math.ceil(height/pixelSize)),pixelSize, pallette=pallette, variance=variance)
    imgutil.save(im, path, name)

def main():
    # Next line gets a random pallette from color lovers
    # pallette = colourlovers.getPallette(random.randint(1,3687000))

    #Next line gets a specific pallette from color lovers
    colourloverid = 1283145
    pallette = pallettes.getFromColourLovers(colourloverid)

    # 2560 / Standard
    # makeGridPallette(pallette,80, path="created/wallpaper/")

    # 1920x1080
    # makeGridPallette(pallette,120, path="created/wallpaper/", width=1920, height=1080)

    makeGridPallette(pallette,320, path="created/wallpaper/", width=2560, height=1920, variance=15, name=(str(time.strftime("%Y%m%d%H%M%S"))+"_"+str(colourloverid)+".png"))

if __name__ == '__main__':
    main()