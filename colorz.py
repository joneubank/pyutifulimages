import random

class Color:

	# Optional:
	# a=255 - provide (between 0-255) if you want there to set opacity as somthing other than 255
	def __init__(self, r, g, b, a=255):
		self.r = clamp(r)
		self.g = clamp(g)
		self.b = clamp(b)
		self.a = clamp(a)

	def rgb(self):
		return (self.r, self.g, self.b)

	def rgba(self):
		return (self.r, self.g, self.b, self.a)

def fromNum(num):
	r = num&255
	g = (num&(255*256)) >> 8
	b = (num&(255*256*256)) >> 16

	#Apply clamps
	r = clamp(r)
	g = clamp(g)
	b = clamp(b)

	return Color(r, g, b)



# Optional:
# min=0 - Specify minimum generated value - applies to R, G, B, and A values (A only if opacity set outside -1 to 255)
# max=255 - Specify maximum generated value - applies to R, G, B, and A values (A only if opacity set outside -1 to 255)
# opacity=255 - specify opacity or set to -1 for random
def randcolor(min=0, max=255, opacity=255):
	r = random.randint(min, max)
	g = random.randint(min, max)
	b = random.randint(min, max)

	if(opacity>=0 and opacity<=255):
		a = opacity
	else:
		a = random.randint(min,max)

	return Color(r,g,b,a)

#Returns input limited to rang 0-255, if higher returns 255, if lower returns 0
def clamp(n):
    if n < 0:
        return 0
    elif n > 256:
        return 256
    else:
        return n

std = {
	'BLACK'		:Color(  0,   0,   0),
	'WHITE'		:Color(255, 255, 255),
	'RED'		:Color(255,   0,   0),
	'GREEN'		:Color(  0, 255,   0),
	'BLUE'		:Color(  0,   0, 255)
	}

def main():
	# print colorFromNum(300000).rgb()
	pass

if __name__ == '__main__':
	main()