from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdowns")
root.geometry('400x400')

def show(var):
    picked = Label(root, text=clicked.get()).pack()
    
    
options= [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=show)
drop.pack()

root.mainloop()