from functions import work
from cli import cli
from pdf2image import convert_from_path
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from PIL import Image as img
import os
import shutil
import sys
from tkinter.filedialog import askopenfilename

# dir_path = os.path.dirname(os.path.realpath(__file__))
# path = os.path.join(dir_path, "cut")
# try: 
#     os.mkdir(path)
# except FileExistsError:
#     print("Cut Deleted")
#     shutil.rmtree(path)
#     os.mkdir(path)

def pdfs(name):
	pages = convert_from_path(name, 200)
	k = []
	for _p in pages:
		k += work(_p)
	return k

def pics(name):
	im = img.open(name)
	return work(im)


print("Code by Delta0001#1968")
print("Hosted on GitHub @ SuperSat001/Question-Extractor")


master = Tk()
master.title("Question Extractor")
Label(master, text="Loading").grid(row=0, column=0, padx=10, pady=10)
# master.withdraw()

save_loc = filedialog.askdirectory()
print("Saving location:", save_loc)

filename = askopenfilename(filetypes=[("Accepted", "*.pdf"), ("Accepted", "*.png")])
print("Selected file:", filename)
# master.deiconify()

var = IntVar()

if filename.endswith(".png"):
	r = pics(filename)
else:
	r = pdfs(filename)

cli(r, 1, master, var, save_loc)





