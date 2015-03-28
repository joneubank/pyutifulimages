import random


class Color:
    # Optional:
    # a=255 - specify opacity if transparency is desired
    def __init__(self, r, g, b, a=255):
        self.r = clamp(r)
        self.g = clamp(g)
        self.b = clamp(b)
        self.a = clamp(a)

    def rgb(self):
        return (self.r, self.g, self.b)

    def rgbrange(self,variance):
        output = (
            clamp(self.r-variance),
            clamp(self.r+variance),
            clamp(self.g-variance),
            clamp(self.g+variance),
            clamp(self.b-variance),
            clamp(self.b+variance),
            )
        return output

    def rgba(self):
        return (self.r, self.g, self.b, self.a)

    def invert(self):
        return Color(255-self.r, 255-self.g, 255-self.b, self.a)

    def __unicode__(self):
        return self.rgba()


def fromNum(num):
    r = num & 255
    g = (num & (255*256)) >> 8
    b = (num & (255*256*256)) >> 16

    # Apply clamps
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)

    return Color(r, g, b)


def randcolorrange(colorrange=(0, 255, 0, 255, 0, 255), opacity=255):
    r = clamp(random.randint(int(colorrange[0]), int(colorrange[1])))
    g = clamp(random.randint(int(colorrange[2]), int(colorrange[3])))
    b = clamp(random.randint(int(colorrange[4]), int(colorrange[5])))

    if(opacity >= 0 and opacity <= 255):
        a = opacity
    else:
        a = random.randint(min, max)

    return Color(r, g, b, a)


# Optional:
# min=0 - Specify minimum generated value - applies to R, G, B, and A values
# max=255 - Specify maximum generated value - applies to R, G, B, and A values
# opacity=255 - specify opacity or set to -1 for random
def randcolor(min=0, max=255, opacity=255):
    return randcolorrange((min, max, min, max, min, max), opacity)


# Returns input limited to rang 0-255
# if higher returns 255, if lower returns 0
def clamp(n):
    if n < 0:
        return 0
    elif n > 256:
        return 256
    else:
        return n

std = {
    'BLACK': Color(0, 0, 0),
    'WHITE': Color(255, 255, 255),
    'RED': Color(255, 0, 0),
    'GREEN': Color(0, 255, 0),
    'BLUE': Color(0, 0, 255)
    }


def main():
    # print colorFromNum(300000).rgb()
    pass


if __name__ == '__main__':
    main()
