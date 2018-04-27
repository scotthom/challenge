import tkinter as tk

# By default frames will stack ontop of each other vertically
class HaarCascade(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(fill="none", expand = True)

        self.frames = {}

        #frame = Window1(container, self)

        #self.frames[Window1] = frame

        #frame.grid(row=0, column=0, sticky="nsew")

        for F in (Window1, Window2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Window1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Window1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame1 = tk.Frame(self,highlightbackground="green", 
                highlightcolor="green", highlightthickness=1, width=150,
                height=150)
        frame1.pack()
        # pack_propagate: stops Tkinter automatically resizing frame. 
        # Planning use mostly.
        frame1.pack_propagate(False)

        name = tk.Label(frame1, text="Window 1")
        name.pack()

        label1 = tk.Label(frame1, text="Frame 1")
        label1.pack()

        frame2 = tk.Frame(self,highlightbackground="green", 
                highlightcolor="green", highlightthickness=1, width=150,
                height=150)
        frame2.pack()
        frame2.pack_propagate(False)

        label2 = tk.Label(frame2, text="Frame 2")
        label2.pack()

class Window2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame1 = tk.Frame(self,highlightbackground="green", 
                highlightcolor="green", highlightthickness=1, width=150,
                height=150)
        frame1.pack()
        # pack_propagate: stops Tkinter automatically resizing frame. 
        # Planning use mostly.
        frame1.pack_propagate(False)

        name = tk.Label(frame1, text="Window 2")
        name.pack()

        label1 = tk.Label(frame1, text="Frame 1")
        label1.pack()

        frame2 = tk.Frame(self,highlightbackground="green", 
                highlightcolor="green", highlightthickness=1, width=150,
                height=150)
        frame2.pack()
        frame2.pack_propagate(False)

        label2 = tk.Label(frame2, text="Frame 2")
        label2.pack()



app = HaarCascade()
app.mainloop()