import tkinter as tk

class HaarCascade(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        # Import Tk class __init__ attributes/ methods
        tk.Tk.__init__(self, *args, **kwargs)

        frame = tk.Frame(self,highlightbackground="green", 
                highlightcolor="green", highlightthickness=1, width=150,
                height=150)
        frame.pack()
        # pack_propagate: stops Tkinter automatically resizing frame. 
        # Planning use mostly.
        frame.pack_propagate(False)

        label = tk.Label(frame, text="Frame")
        label.pack()

app = HaarCascade()
app.mainloop()