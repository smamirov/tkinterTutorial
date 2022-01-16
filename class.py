from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.title("Classes")
root.geometry('400x400')

class TestClass:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.grid()

        # Two labels 
        self.fnamelabel = tk.Label(master, text="First Name:")
        self.fnamelabel.grid(row=0, column=0)
        self.lnamelabel = tk.Label(master, text="Last Name:") 
        self.lnamelabel.grid(row=1, column=0)

        # Two Entry's
        self.fname = tk.Entry(master)
        self.fname.grid(row=0, column=1)
        self.lname = tk.Entry(master)
        self.lname.grid(row=1, column=1)

        # Button to sumbit
        self.submit = tk.Button(master, text="Submit", command=self.submit)
        self.submit.grid(row=2, column=0, sticky=W)

    def submit(self):
        firstName = self.fname.get()
        lastName = self.lname.get()

        self.myLabel = tk.Label(text=firstName + lastName)
        self.myLabel.grid(row=4, column=0)

instance = TestClass(root)


root.mainloop()