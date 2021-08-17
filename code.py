from PIL import Image as img
from numpy import array
from functions import *

sample = img.open(f"sample.png", "r")
w, h = sample.size

print(w, h)

pix = sample.load()

print(notAllWhite(sample))
print(checkWhite(100,100,pix))
print(checkLine(sample))

k = work(sample)
print(k)

k[0].save("ceh.png", "PNG")





