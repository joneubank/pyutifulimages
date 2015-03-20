# pyutifulimages
Programatic image generation in python. Sandbox project, no objective or application.

##imgutil.py
###save(image, path, dir)
Usage Example:
```
from PIL import Image

im = Image.open("test.jpg")
imgutil.save(out,"temp/","test.png")
```


##colorz.py
Convenient methods and data structure for representing RGBA colors. All RGBA values are restricted to be between the rang 0-255.

###class Color(r,g,b,a=255)
Convenient data model for passing/generating color data. Includes two methods to output a tuple representing the color values:
* rgb() for (r,g,b)
* rgba() for (r,g,b,a)

###def randcolor(min=0, max=255, opacity=255)
Returns a Color object with random RGB values in the range min-max. Opacity can be specified or set to -1 to generate randomly.

###def fromNum(num)
Returns a Color object with RGB values based on the value of the number passed in.



##Requirements
The following python packages are dependencies for this package to run:
* [pillow](https://pypi.python.org/pypi/Pillow/2.0.0) - Maintained fork of PIL (Python Image Library)
