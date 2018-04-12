import os
import os.path
import os
import cv2
import imutils
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class Resize(Frame):
    def resize_alg(self, pos_size, neg_size):
        #self.progress["value"] = 0
        #self.maxbytes = len
        #self.progress["maximum"] = len
        # load the image to a smaller factor so that the shapes can be 
        #   approximated better

        pos_resize_width = int(pos_size.get())
        neg_resize_width = int(neg_size.get())

        raw_neg_dir = "./raw/neg/"
    
        for img_name in os.listdir(raw_neg_dir):
            img = cv2.imread(raw_neg_dir + img_name)
            resized = imutils.resize(img, width=neg_resize_width)
            cv2.imwrite("clean_neg/"+img_name, resized)

        raw_pos_dir = "./raw/pos/"
    
        for img_name in os.listdir(raw_pos_dir):
            img = cv2.imread(raw_pos_dir + img_name)    
            resized = imutils.resize(img, width=pos_resize_width)
            cv2.imwrite("clean_pos/"+img_name, resized)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        frame = Frame(self)
        frame.pack(fill="none", expand=True)
        self.master.wm_geometry("500x600")

        # add title and image to applicaiton
        title = Label(frame, text="Resize Image")
        title.config(font=("Courier, 24"))
        title.grid(row=0)

        # Add photo
        path = "./images/resize_image.jpg"
        photo = ImageTk.PhotoImage(Image.open(path))
        label_photo = Label(frame, image=photo)
        label_photo.image = photo
        label_photo.grid(row=1)

        # label = Label(root1, text="sum ")
        label_pos_resize_width = Label(frame, text="Positive Image Resize Width")
        label_neg_resize_width = Label(frame, text="Negative Image Resize Width")


        # user input box
        input_pos_resize_width = Entry(frame)
        input_neg_resize_width = Entry(frame)

        #blank space
        blank_row = Label(frame, text="")

        # Format Objects

        label_pos_resize_width.config(font=("Courier, 14"))
        label_neg_resize_width.config(font=("Courier, 14"))
        input_pos_resize_width.config(font=("Courier, 14"))
        input_neg_resize_width.config(font=("Courier, 14"))

        blank_row.grid(row=2)
        label_pos_resize_width.grid(row=3)
        label_neg_resize_width.grid(row=5)
        input_pos_resize_width.grid(row=4)
        input_neg_resize_width.grid(row=6)
 
        b = Button(frame, text="resize", width=10, command=lambda: self.resize_alg(input_pos_resize_width, input_neg_resize_width))
        b.config(font=("Courier, 10"))
        b.grid(row=7)
        
        #self.progress = ttk.Progressbar(self, orient="horizontal",
        #                                length=200, mode="determinate")
        #self.progress.pack()

        #self.bytes = 0
        #self.maxbytes = 0

        
        ## Make progress bar
        #num_pos_images = len([name for name in os.listdir('./train/raw/pos') if os.path.isfile(name)])
        #num_neg_images = len([name for name in os.listdir('./train/raw/pos') if os.path.isfile(name)])
        #num_total_image = num_pos_images + num_neg_images
        #self.start(num_total_image)

    #def read_bytes(self):
    #    self.bytes += 1
    #    self.progress["value"] = self.bytes

#def resizeWidth():


app = Resize()
#app.geometry("500x600")
#app.title("Haar Cascade")
app.mainloop()

#main.pack(side="top", fill="both", expand=True)
#root.geometry("500x600")
#root.mainloop


