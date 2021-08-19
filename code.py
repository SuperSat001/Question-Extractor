from module.functions import work
from module.cli import cli
from pdf2image import convert_from_path
from tkinter import *
from tkinter.ttk import *
import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "cut")
try: 
    os.mkdir(path)
except FileExistsError:
    print("Cut Deleted")
    shutil.rmtree(path)
    os.mkdir(path)

def pdfs(name):
	pages = convert_from_path(name, 200)
	k = []
	for _p in pages:
		k += work(_p)
	return k

def pics(name):
	im = img.open(name)
	return work(im)


master = Tk()
master.title("Question Extractor")

var = IntVar()

#r = pics("testdata/sample2.png")
r = pdfs("testdata/file2.pdf")

cli(r, 1, master, var)





