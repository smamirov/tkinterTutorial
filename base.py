from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("")
root.geometry('400x400')



root.mainloop()


######################################################
# Method 1
from tkinter import *

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.resizable(False, False)

    def label(self):
        self.myLabel = Label(self, text="Hello World!")
        self.myLabel.pack()

if __name__=="__main__":
    root = Login()
    root.label()
    root.mainloop()

#######################################################
# Methid 2

import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()