import tkinter as tk
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12)

class HaarCascade(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(fill="none", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (home, resizeImage, positiveFile, train, identifyImage):

            #initialize each page in container
            frame = F(container, self)

            #Store frames in a dictionary
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        windowTitle = tk.Label(self, text="Home")
        windowTitle.grid(row=0)
        windowTitle.config(font=("Courier, 24"))

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=1)

        resize_image = Image.open("./images/resize.jpg")
        image_resize = ImageTk.PhotoImage(resize_image)
        label = tk.Label(image=image_resize)
        label.image = image_resize
        label.grid(blank_row=2)

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=3)

        resize_button = tk.Button(self, text="Resize Image", command=lambda:  controller.show_frame(resizeImage))
        resize_button.grid(row=4)

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=5)

        windowTitle = tk.Label(self, text="<Add cropped Miconia photo here>")
        windowTitle.grid(row=6)
        windowTitle.config(font=("Courier, 16"))

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=7)

        resize_button = tk.Button(self, text="Positive Image", command=lambda:  controller.show_frame(positiveFile))
        resize_button.grid(row=8)

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=9)

        windowTitle = tk.Label(self, text="<Add train Haar Cascade here>")
        windowTitle.grid(row=10)
        windowTitle.config(font=("Courier, 16"))

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=11)

        resize_button = tk.Button(self, text="Train", command=lambda:  controller.show_frame(train))
        resize_button.grid(row=12)

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=13)

        windowTitle = tk.Label(self, text="<Add identify Miconia here>")
        windowTitle.grid(row=14)
        windowTitle.config(font=("Courier, 16"))

        blank_row = tk.Label(self, text="")
        blank_row.grid(row=15)

        resize_button = tk.Button(self, text="Identify Image", command=lambda:  controller.show_frame(identifyImage))
        resize_button.grid(row=16)

class resizeImage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Resize Image", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(home))
        button1.pack()


class positiveFile(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Make Positive File", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(home))
        button1.pack()


class train(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Train", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(home))
        button1.pack()


class identifyImage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Identify Image", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(home))
        button1.pack()

        

app = HaarCascade()
app.wm_geometry("500x600")
app.title("Haar Cascade")
app.mainloop()
