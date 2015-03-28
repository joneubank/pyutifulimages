import math
import time

import boxdraw
import palettes
import imgutil
import random

SIZES_2560 = [320, 160, 80, 64, 40, 32, ]

def makeGridpalette(palette, pixelSize, variance=15, width=2560, height=1600, path="/", name=(str(time.strftime("%Y%m%d%H%M%S"))+".png")):
    im = boxdraw.makeSquareGridpalette(int(math.ceil(width*1.0/pixelSize)),int(math.ceil(height/pixelSize)),pixelSize, palette=palette, variance=variance)
    imgutil.save(im, path, name)

def main():
    # Next line gets a random palette from color lovers
    # palette = colourlovers.getpalette(random.randint(1,3687000))

    #Next line gets a specific palette from color lovers
    colourloverid = 1283145
    palette = palettes.getFromColourLovers(colourloverid)

    # 2560 / Standard
    # makeGridpalette(palette,80, path="created/wallpaper/")

    # 1920x1080
    # makeGridpalette(palette,120, path="created/wallpaper/", width=1920, height=1080)

    makeGridpalette(palette,320, path="created/wallpaper/", width=2560, height=1920, variance=15, name=(str(time.strftime("%Y%m%d%H%M%S"))+"_"+str(colourloverid)+".png"))

if __name__ == '__main__':
    main()