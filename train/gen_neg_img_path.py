import os
import tkinter
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()
root.update()

root.filename = filedialog.askdirectory(initialdir=".", title="Select Image", mustexist=False)

dir_path = os.path.join(root.filename)
 
for img in os.listdir(dir_path):
    line = dir_path+'/'+img+'\n'
    with open('neg_img_path.txt','a') as f:
        f.write(line)

root.destroy()
