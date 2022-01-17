from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("")
root.geometry('500x500')

myNotebook = ttk.Notebook(root)
myNotebook.pack(pady=15)

def hide():
    myNotebook.hide(1)

def show():
    myNotebook.add(myFrame2, text="Red Tab")

def select():
    myNotebook.select(1)

myFrame1 = Frame(myNotebook, width=400, height=400, bg="blue")
myFrame2 = Frame(myNotebook, width=400, height=400, bg="red")

myFrame1.pack(fill="both", expand=True)
myFrame2.pack(fill="both", expand=True)

myNotebook.add(myFrame1, text="Blue Tab")
myNotebook.add(myFrame2, text="Red Tab")

myBtn = Button(myFrame1, text="Hide tab 2", command=hide).pack(pady=10)
myBtn2 = Button(myFrame1, text="Show tab 2", command=show).pack(pady=10)
myBtn3 = Button(myFrame1, text="Navigate to tab 2", command=select).pack(pady=10)

root.mainloop()