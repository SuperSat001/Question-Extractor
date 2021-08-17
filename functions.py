from PIL import Image as img
from numpy import array

white = (255, 255, 255)
sens_x, sens_y = 1250, 30

def checkWhite(i, j, pix):
	for y in range(j, j+sens_y):
		for x in range(i, i+sens_x):
			if pix[x, y] != white:
				return 0
	return 1

def notAllWhite(image):
	w, h = image.size
	pix = image.load()
	for i in range(w):
		for j in range(h):
			if pix[i, j] != white:
				return 1
	return 0

def checkLine(image):
	w, h = image.size
	pix = image.load()
	for i in range(h):
		j = 0
		cont = 0
		while j < w:
			if pix[j, i] != white:
				cont += 1
			else:
				if cont >= 0.6*w:
					return 1
				cont = 0
			j += 1
	return 0

def work(im):
	pix = im.load()
	width, height = im.size

	marks = [0]

	y = 0
	while y < height-sens_y:
		if checkWhite(50, y, pix):
			marks.append(y + 5)
			y += sens_y
		y += 1

	marks.append(height)
	
	qns = []

	i = 0
	for l in range(len(marks)-1):
		c = im.crop((0, marks[l], width, marks[l+1]))
		if notAllWhite(c):
			qns.append(c)
			#c.save(f"{i}.png", "PNG")
			i += 1

	return qns



