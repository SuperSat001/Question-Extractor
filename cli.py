from PIL import Image as img
import matplotlib.pyplot as plt
from functions import work

def imgMerge(images):
	widths, heights = zip(*(i.size for i in images))

	total_height = sum(heights)
	max_width = max(widths)

	new_im = img.new('RGB', (max_width, total_height))

	y_offset = 0
	for im in images:
		new_im.paste(im, (0, y_offset))
		y_offset += im.size[1]

	return new_im

def cli(qns, x=1):
	i = x
	merge = False
	to_merge = []
	for qn in qns:
		plt.imshow(qn)
		plt.waitforbuttonpress(0)
		plt.close()

		if merge:
			print("merging", len(to_merge))
		t = int(input("Command: "))
		if t == 0:
			if merge:
				new = imgMerge(to_merge)
				new.save(f"cut/{i}.png", "PNG")
				to_merge = []
				merge = False
				i += 1
		elif t == 1:
			if not merge:
				qn.save(f"cut/{i}.png", "PNG")
			else:
				new = imgMerge(to_merge)
				new.save(f"cut/{i}.png", "PNG")
				to_merge = []
				merge = False
			i += 1
		elif t == 2:
			if not merge:
				merge = True
				print(f"Merge started at q{i}")
			to_merge.append(qn)



# sample = img.open(f"sample.png", "r")
# sample2 = img.open(f"sample2.png", "r")

# qn2 = work(sample2)

# cli(qn2)