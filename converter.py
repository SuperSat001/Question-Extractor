from pdf2image import convert_from_path
import os
import shutil
import sys
  
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "page")
save_path = os.path.join(dir_path, "Save/pics")

try:
    os.mkdir(save_path)
except:
    pass

try: 
    os.mkdir(path)
except FileExistsError:
    print("Conv Exists")
    shutil.rmtree(path)
    os.mkdir(path)

name = " ".join(sys.argv[1:])
pages = convert_from_path(name, 200)

k = 0

def proper(name):
    if name.startswith("AITS"):
        name = name[5:]
    if name.endswith(".pdf"):
        name = name[:-4]
    return name

f_path = os.path.join(save_path, proper(name))  
try:        
        os.mkdir(f_path)
except Exception as e:
        pass

for i in range(len(pages)):
    page = pages[i]
    page = page.crop((178,88,1537,2105))
    k += 1
    page.save(f'page/{i}.png', 'PNG')     

    page.save(f'{f_path}/{i}.png', 'PNG')

print(k)