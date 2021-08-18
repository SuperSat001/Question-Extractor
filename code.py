from PIL import Image as img
from PIL import ImageTk
import matplotlib.pyplot as plt
from functions import work
from cli import cli
from pdf2image import convert_from_path
from tkinter import *
from tkinter.ttk import *
from math import floor

# pages = convert_from_path("file.pdf", 200)
# #sample = pages[0]

# # sample = img.open(f"sample.png", "r")

# k = []
# for _p in pages:
# 	k += work(_p)

# im = img.open("sample2.png")
# # r = work(im)

# cli(k, 10)

master = Tk()
var = IntVar()

l = Label(master, text="Test")
l.grid(row=5, column=0)

from display import gen

sample = img.open("0-3.png")
sample = sample.resize((floor(sample.size[0]/2), floor(sample.size[1]/2)))
simg1 = ImageTk.PhotoImage(sample)

sample = img.open("0-4.png")
sample = sample.resize((floor(sample.size[0]/2), floor(sample.size[1]/2)))
simg2 = ImageTk.PhotoImage(sample)


gen(master, var, simg1, simg2)

mainloop()





