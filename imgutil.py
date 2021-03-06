import os
import sys
# import random
from PIL import Image

import colorz


def makeBlank(width, height, color=colorz.std['BLACK'], mode="RGBA"):
    return Image.new(mode, (width, height), color.rgba())


# Save a PIL Image at the given path. Ensure that the filetype is specified.
def save(image, path, name):

    # first ensure the path exists, and create if it doesn't
    if not os.path.exists(path):
        os.makedirs(path)

    # Now save image, catching any errors which occur
    try:
        filename = path + name
        image.save(filename)
    except:
        # temporary except block. handle specific errors as they occur
        print "An error occured, details follow, consider correcting for this:"
        print str(sys.exc_info()[0])
        raise


def genTimeName(description, filetype, timestamp=True):
    output = ""
    if timestamp:
        output = output + str(time.strftime("%Y%m%d%H%M%S")) + "_"
    output = output + description + "." + filetype
    return output

def main():
    print "Not really any reason to run this, but thanks for playing!"


if __name__ == '__main__':
    main()
