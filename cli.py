from PIL import Image as img
from PIL import ImageTk
from display import buttons
from math import floor

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

def cli(qns, x, master, var, save_loc):
	i = x
	merge = False
	to_merge = []
	for _q in range(len(qns)):
		t = -1

		qcurr = qns[_q]
		qn = qns[_q]
		qcurr = qcurr.resize((floor(qcurr.size[0]/2), floor(qcurr.size[1]/2)))
		qcurr = ImageTk.PhotoImage(qcurr)

		qnext = None
		if _q < len(qns)-1:
			qnext = qns[_q+1]
			qnext = qnext.resize((floor(qnext.size[0]/2), floor(qnext.size[1]/2)))
			qnext = ImageTk.PhotoImage(qnext)

		qmerge = None
		if merge:
			qmerge = imgMerge(to_merge)
			qmerge = qmerge.resize((floor(qmerge.size[0]/2), floor(qmerge.size[1]/2)))
			qmerge = ImageTk.PhotoImage(qmerge)
			#print("merging", len(to_merge))


		# tkinter window
		i = buttons(master, var, i, merge, qmerge, qcurr, qnext)
		#print(i)
		# if any button pressed, stop window and move to next part of code

		t = var.get()
		#print("t", t)

		if t == 0:
			pass

		elif t == 1:
			if not merge:
				qn.save(f"{save_loc}/{i}.png", "PNG")
			else:
				new = imgMerge(to_merge)
				new.save(f"{save_loc}/{i}.png", "PNG")
				to_merge = []
				merge = False
			i += 1

		elif t == 2:
			if not merge:
				merge = True
				#print(f"Merge started at q{i}")
			to_merge.append(qn)

		elif t == 3:
			para = True
			if not merge:
				merge = True
				#print(f"Para merging")
			to_merge.append(qn)
			i += 1

		elif t == 4:
			if merge:
				new = imgMerge(to_merge)
				new.save(f"{save_loc}/{i}.png", "PNG")
				to_merge = []
				merge = False
				i += 1

	if merge:
		new = imgMerge(to_merge)
		new.save(f"{save_loc}/{i}.png", "PNG")
	master.destroy()


