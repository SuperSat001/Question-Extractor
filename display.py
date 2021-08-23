from tkinter import *
from tkinter.ttk import *

def fn(x, master, var):	
	def f():
		var.set(x)
		#print("Button",x)
		#l = Label(master, text=f"Last {x}")
		#l.grid(row = 15, column = 0, pady = 5)
	return f

def buttons(master, var, qn, merge, qmerge, qcurr, qnext=None):

	temp = IntVar()
	temp.set(qn)
	Label(master, text=f"No. {qn}").grid(row = 3, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	def qinc():
		temp.set(temp.get()+1)
		Label(master, text=f"No. {temp.get()}").grid(row = 3, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	Button(master, text=f"Q Inc", command=qinc).grid(row = 3, column = 1,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	def qdec():
		temp.set(temp.get()-1)
		Label(master, text=f"No. {temp.get()}").grid(row = 3, column = 0,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)

	Button(master, text=f"Q Dec", command=qdec).grid(row = 3, column = 2,
       columnspan = 1, rowspan = 1, padx = 5, pady = 5)



	nextLabel, nextPic, mergeLabel, mergePic, b3, b4 = None, None, None, None, None, None
	if not merge:

		b0 = Button(master, text="Skip\n", command=fn(0, master, var))
		b0.grid(row = 0, column = 0, pady=5, padx=5, rowspan=2)

		b1 = Button(master, text = "Save\n", command=fn(1, master, var))
		b1.grid(row = 0, column = 1, pady=5, padx=5, rowspan=2)

		b2 = Button(master, text="Start Merge", command=fn(2, master, var))
		b2.grid(row = 2, column = 0, pady=5, padx=5)

	else:
		b0 = Button(master, text="Skip\nWhile Merging", command=fn(0, master, var))
		b0.grid(row = 0, column = 0, pady=5, padx=5, rowspan=2)

		b1 = Button(master, text = "Save\nEnd Merge", command=fn(1, master, var))
		b1.grid(row = 0, column = 1, pady=5, padx=5, rowspan=2)

		b2 = Button(master, text="Merge Same", command=fn(2, master, var))
		b2.grid(row = 2, column = 0, pady=5, padx=5)

		b3 = Button(master, text="Merge Next", command=fn(3, master, var))
		b3.grid(row = 2, column = 1, pady=5, padx=5)

		b4 = Button(master, text="Skip and End Merge", command=fn(4, master, var))
		b4.grid(row = 2, column = 2, pady=5, padx=5, columnspan=1)

	b5 = Button(master, text="Back", command=fn(5, master, var))
	b5.grid(row = 0, column = 2, pady=5, padx=5, columnspan=1)

	Label(master, text="Current Question").grid(row = 4, column = 0,
       columnspan = 4, rowspan = 1, padx = 5, pady = 5)

	Label(master, image = qcurr).grid(row = 5, column = 0,
       columnspan = 4, rowspan = 2, padx = 5, pady = 5)

	if not (qnext == None): 
	       nextLabel = Label(master, text="Next Question")
	       nextLabel.grid(row = 7, column = 0, columnspan = 4, rowspan = 1, padx = 5, pady = 5)

	       nextPic = Label(master, image = qnext)
	       nextPic.grid(row = 8, column = 0, columnspan = 4, rowspan = 2, padx = 5, pady = 5)

	if merge:
		mergeLabel = Label(master, text="Current Merge")
		mergeLabel.grid(row = 10, column = 0, columnspan = 4, rowspan = 1, padx = 5, pady = 5)

		mergePic = Label(master, image = qmerge)
		mergePic.grid(row = 11, column = 0, columnspan = 4, rowspan = 2, padx = 5, pady = 5)


	b0.wait_variable(var)
	#print(var.get())
	b0["state"] = "disabled"
	b1["state"] = "disabled"
	b2["state"] = "disabled"
	try:
		b3["state"] = "disabled"
	except:
		pass
	try:
		b4["state"] = "disabled"
	except:
		pass


	to_delete = [nextLabel, nextPic, mergeLabel, mergePic, b3, b4]
	for delete_item in to_delete:
		try:
			delete_item.destroy()
		except:
			pass
	
	return temp.get()



