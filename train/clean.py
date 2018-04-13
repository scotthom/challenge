import os
import os.path
import os
import cv2
import imutils
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image


class Resize(Frame):
    def resize_alg(self, pos_size, neg_size):

        pos_resize_width = int(pos_size.get())
        neg_resize_width = int(neg_size.get())

        raw_pos_dir = self.pos_img_dir_path
    
        for img_name in os.listdir(raw_pos_dir):
            img = cv2.imread(raw_pos_dir + "/" + img_name)    
            resized = imutils.resize(img, width=pos_resize_width)
            cv2.imwrite("clean_pos/"+img_name, resized)

        raw_neg_dir = self.neg_img_dir_path
    
        for img_name in os.listdir(raw_neg_dir):
            img = cv2.imread(raw_neg_dir + "/" + img_name)
            resized = imutils.resize(img, width=neg_resize_width)
            cv2.imwrite("clean_neg/"+img_name, resized)

    def positiveImagePath(self, label):
        pos_img_dir = filedialog.askdirectory(initialdir=".",
        title="Select Positive Image", mustexist=False)
        self.pos_img_dir_path = os.path.join(pos_img_dir)
        label.config(text="Okay", fg="green2")

    def negativeImagePath(self, label):
        neg_img_dir = filedialog.askdirectory(initialdir=".",
        title="Select Negative Image", mustexist=False)
        self.neg_img_dir_path = os.path.join(neg_img_dir)
        label.config(text="Okay", fg="green2")


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        frame = Frame(self)
        frame.pack(fill="none", expand=True)
        self.master.wm_geometry("500x600")

        # add title and image to applicaiton
        title = Label(frame, text="Resize Images")
        title.config(font=("Courier, 24"))
        title.grid(row=0)

        # Add photo
        path = "./images/resize_image.jpg"
        photo = ImageTk.PhotoImage(Image.open(path))
        label_photo = Label(frame, image=photo)
        label_photo.image = photo
        label_photo.grid(row=1)

        #blank space
        blank_row_1 = Label(frame, text="")
        blank_row_1.grid(row=2)

        # initialize variables to be updated with path
        self.pos_img_dir_path = ""
        self.neg_img_dir_path = ""

        pos_img_dir_label = Label(frame, text="Positive Folder: ")
        pos_img_dir_label.config(font=("Courier, 14"))
        pos_img_dir_label.grid(row=3, column=0)

        pos_img_dir_state_label = Label(frame, text="")
        pos_img_dir_state_label.config(font=("Courier, 14"))
        pos_img_dir_state_label.grid(row=3, column=1)

        frame.grid_columnconfigure(3, weight=0)

        pos_img_dir_button = Button(frame, text="set folder location",
        width=20, command=lambda: self.positiveImagePath(pos_img_dir_state_label))
        pos_img_dir_button.config(font=("Courier, 10"))
        pos_img_dir_button.grid(row=4)


        neg_img_dir_label = Label(frame, text="Negative Folder: ")
        neg_img_dir_label.config(font=("Courier, 14"))
        neg_img_dir_label.grid(row=5)

        neg_img_dir_state_label = Label(frame, text="")
        neg_img_dir_state_label.config(font=("Courier, 14"))
        neg_img_dir_state_label.grid(row=5, column=1)

        neg_img_dir_button = Button(frame, text="set folder location",
        width="20", command=lambda: self.negativeImagePath(neg_img_dir_state_label))
        neg_img_dir_button.config(font=("Courier, 10"))
        neg_img_dir_button.grid(row=6)

        # label = Label(root1, text="sum ")
        label_pos_resize_width = Label(frame, text="Positive Resize Width")
        label_neg_resize_width = Label(frame, text="Negative Resize Width")


        # user input box
        input_pos_resize_width = Entry(frame)
        input_neg_resize_width = Entry(frame)

        # Format Objects

        label_pos_resize_width.config(font=("Courier, 14"))
        label_neg_resize_width.config(font=("Courier, 14"))
        input_pos_resize_width.config(font=("Courier, 14"))
        input_neg_resize_width.config(font=("Courier, 14"))

        blank_row_2 = Label(frame, text="")
        blank_row_2.grid(row=7)

        label_pos_resize_width.grid(row=8)
        label_neg_resize_width.grid(row=10)
        input_pos_resize_width.grid(row=9)
        input_neg_resize_width.grid(row=11)
 
        b = Button(frame, text="resize", width=10, command=
        lambda: self.resize_alg(input_pos_resize_width, input_neg_resize_width))
        b.config(font=("Courier, 10"))
        b.grid(row=12)
        
app = Resize()
app.mainloop()