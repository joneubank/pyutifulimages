import os
import sys
# import random
# from PIL import Image


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


def main():
    print "Not really any reason to run this, but thanks for playing!"


if __name__ == '__main__':
    main()
