from PIL import Image,ImageDraw
import numpy

def cortar():
	im = Image.open(r"D:\PUJ\AAAA\ACN\Proyecto---Analisis-Numerico\prueba.png")

	width,height = im.size

	#im.show()

	# COnvert to numpy
	imArray = numpy.asarray(im)

	#Create mask

	#En el polygon, se agregan las coordenada xy del punto
	polygon = [(40,20),(45,25),(50,30),(55,35),(60,40),(65,45),(70,50),(85,55),(90,60),(95,65)]
<<<<<<< Updated upstream
=======
	
# create new image ("1-bit pixels, black and white", (width, height), "default color")
>>>>>>> Stashed changes
	maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
	ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
	mask = numpy.array(maskIm)

	# assemble new image (uint8: 0-255)
	newImArray = numpy.empty(imArray.shape,dtype='uint8')

	# copy color values (RGB)
	newImArray[:,:,:3] = imArray[:,:,:3]

	# filtering image by mask
	newImArray[:,:,0] = newImArray[:,:,0] * mask
	newImArray[:,:,1] = newImArray[:,:,1] * mask
	newImArray[:,:,2] = newImArray[:,:,2] * mask	# back to Image from numpy

	newIm = Image.fromarray(newImArray, "RGB")
	newIm.show()
	#newIm.save("out.png")

	# # Setting the points for cropped image 
	# left = 155
	# top = 65
	# right = 360
	# bottom = 270
	  
	# # Cropped image of above dimension 
	# # (It will not change orginal image) 
	# im1 = im.crop((left, top, right, bottom)) 
	  
	# # Shows the image in image viewer 
	# im1.show() 
cortar()

<<<<<<< Updated upstream
# import numpy
# from PIL import Image, ImageDraw

# # read image as RGB and add alpha (transparency)
# im = Image.open("crop.jpg").convert("RGBA")

# # convert to numpy (for convenience)
# imArray = numpy.asarray(im)

# # create mask
# polygon = [(444,203),(623,243),(691,177),(581,26),(482,42)]
# maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
# ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
# mask = numpy.array(maskIm)

# # assemble new image (uint8: 0-255)
# newImArray = numpy.empty(imArray.shape,dtype='uint8')

# # colors (three first columns, RGB)
# newImArray[:,:,:3] = imArray[:,:,:3]

# # transparency (4th column)
# newImArray[:,:,3] = mask*255

# # back to Image from numpy
# newIm = Image.fromarray(newImArray, "RGBA")
# newIm.save("out.png")
# shareimprove this answer
=======
#https://stackoverflow.com/questions/22588074/polygon-crop-clip-using-python-pil
>>>>>>> Stashed changes
