from tkinter import *
from tkinter.ttk import *
from PIL import Image as img
from PIL import ImageTk
from math import floor

def fn(x, master, var):	
	def f():
		var.set(x)
		#print("Button",x)
		l = Label(master, text=f"Last {x}")
		l.grid(row = 5, column = 0, pady = 5)
	return f


def buttons(master, var, qcurr, qnext=None):
	b0 = Button(master, text="0", command=fn(0, master, var))
	b0.grid(row = 0, column = 0, pady=5)

	b1 = Button(master, text = "1", command=fn(1, master, var))
	b1.grid(row = 1, column = 0, pady=5 )

	b2 = Button(master, text="2", command=fn(2, master, var))
	b2.grid(row = 2, column = 0, pady=5)

	b3 = Button(master, text="3", command=fn(3, master, var))
	b3.grid(row = 3, column = 0, pady=5)

	b4 = Button(master, text="4", command=fn(4, master, var))
	b4.grid(row = 4, column = 0, pady=5)

	Label(master, text="Current Question").grid(row = 0, column = 1,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	Label(master, image = qcurr).grid(row = 1, column = 1,
       columnspan = 1, rowspan = 2, padx = 5, pady = 5)

	if not (qnext == None): 
	       Label(master, text="Next Question").grid(row = 3, column = 1,
	       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	       Label(master, image = qnext).grid(row = 4, column = 1,
	       columnspan = 1, rowspan = 2, padx = 5, pady = 5)

	b0.wait_variable(var)
	#print(var.get())
	b0["state"] = "disabled"
	b1["state"] = "disabled"
	b2["state"] = "disabled"
	b3["state"] = "disabled"
	b4["state"] = "disabled"

	return



