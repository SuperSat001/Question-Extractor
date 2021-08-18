from PIL import Image as img
from PIL import ImageTk
import matplotlib.pyplot as plt
from functions import work
from cli import cli
from pdf2image import convert_from_path
from tkinter import *
from tkinter.ttk import *
from math import floor


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

#r = pics("sample2.png")
r = pdfs("file.pdf")

cli(r, 1, master, var)





