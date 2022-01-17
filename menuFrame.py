from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Menu")
root.geometry('400x400')

myMenu = Menu(root)
root.config(menu=myMenu)

def fileNew():
    hideAllFrames()
    fileNewFrame.pack(fill="both", expand=True)

def editCut():
    hideAllFrames()
    editCutFrame.pack(fill="both", expand=True)

# Hide all frames function
def hideAllFrames():
    fileNewFrame.pack_forget()
    editCutFrame.pack_forget()

# Create a menu item

fileMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=fileNew)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# Create and edit menu item
editMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=editCut)
editMenu.add_command(label="Copy")

# Create some frames
fileNewFrame = Frame(root, width=400, height=400, bg="red")
editCutFrame = Frame(root, width=400, height=400, bg="blue")


root.mainloop()