import os
import sys
import random
from PIL import Image

# Save a PIL Image at the given path. Ensure that the filetype is specified.
def save(image, path, name):
	
	#first ensure the path exists, and create if it doesn't
	if not os.path.exists(path):
		os.makedirs(path)

	#Now save image, catching any errors which occur
	try:
		filename = path + name
		image.save(filename)
	except:
		#temporary except block. as real errors are discovered we can handle those issues specifically.
		print "An error occured, details follow, consider correcting for this:"
		print str(sys.exc_info()[0])
		raise


#Optional: opacity=255 - specify opacity or set to -1 for random
def randomColor(min=0,max=255,opacity=255):
	r = random.randint(min,max)
	g = random.randint(min,max)
	b = random.randint(min,max)

	if(opacity>=0 and opacity<=255):
		a = opacity
	else:
		a = random.randint(min,max)

	return (r,g,b,a)

def main():
	print "Not really any reason to run this, but thanks for playing!"


if __name__=='__main__':
	main()