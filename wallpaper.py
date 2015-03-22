import math
import time

import boxdraw
import pallettes
import imgutil
import colourlovers
import random

# Divisors of 2560
# {1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 64, 80, 128, 160, 256, 320, 512, 640, 1280, 2560}
# Divisors of 1600
# {1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 160, 200, 320, 400, 800, 1600}
#
# Common Divisors:
# [1, 2, 4, 5, 8, 16, 20, 25, 32, 40, 64, 80, 160, 320]
#
# Grid Box Combination Options:
# (8,5,320),
# (16,10,160), 
# (32,20,80),
# (102,,64),
# 
# (128,80,20),
# (160,100,16),
# (320,200,8),
# (512,320,5),
# (640,400,4),
# (1280,800,2)

SIZES_2560 = [320, 160, 80, 64, 40, 32, ]

def makeGridPallette(pallette, pixelSize, variance=15, width=2560, height=1600, path="/", name=(str(time.strftime("%Y%m%d%H%M%S"))+".png")):
    im = boxdraw.makeSquareGridPallette(int(math.ceil(width*1.0/pixelSize)),int(math.ceil(height/pixelSize)),pixelSize, pallette=pallette, variance=variance)
    imgutil.save(im, path, name)

def main():
    # Next line gets a random pallette from color lovers
    # pallette = colourlovers.getPallette(random.randint(1,3687000))

    #Next line gets a specific pallette from color lovers
    colourloverid = 125448
    pallette = colourlovers.getPallette(colourloverid)

    # 2560 / Standard
    # makeGridPallette(pallette,80, path="created/wallpaper/")

    # 1920x1080
    # makeGridPallette(pallette,120, path="created/wallpaper/", width=1920, height=1080)

    makeGridPallette(pallette,160, path="created/wallpaper/", width=2560, height=2560, variance=20, name=(str(time.strftime("%Y%m%d%H%M%S"))+"_"+str(colourloverid)+".png"))

if __name__ == '__main__':
    main()