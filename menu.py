from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Menu")
root.geometry('400x400')

myMenu = Menu(root)
root.config(menu=myMenu)

def ourCommand():
    pass

# Create a menu item

fileMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=ourCommand)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# Create and edit menu item
editMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=ourCommand)
editMenu.add_command(label="Copy", command=ourCommand)

root.mainloop()