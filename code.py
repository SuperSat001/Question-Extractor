from PIL import Image as img
import matplotlib.pyplot as plt
from functions import work

sample = img.open(f"sample.png", "r")
w, h = sample.size

print(w, h)

pix = sample.load()

k = work(sample)
print(k)

plt.imshow(k[0])
plt.show()

plt.imshow(k[1])
plt.show()




