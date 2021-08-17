from PIL import Image as img
import matplotlib.pyplot as plt
from functions import work
from cli import cli
from pdf2image import convert_from_path

pages = convert_from_path("file.pdf", 200)
sample = pages[0]

# sample = img.open(f"sample.png", "r")

k = work(pages[0]) + work(pages[1]) + work(pages[2]) 

cli(k)





