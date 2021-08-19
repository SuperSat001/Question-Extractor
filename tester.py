# from pdf2image import convert_from_path

# pages = convert_from_path("testdata/file2.pdf", 200)


# import sys
# print(sys.argv[0], len(sys.argv))

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print(filename)