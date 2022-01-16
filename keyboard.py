from distutils import command
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Keyboard Events")
root.geometry('400x400')

def clicker(event):
    myLabel = Label(root, text="You Clicked" + event.keysym)
    myLabel.pack()

myBtn = Button(root, text="Button")
myBtn.bind("<Key>", clicker)
myBtn.pack(pady=20)

root.mainloop()