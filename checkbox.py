from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.geometry('400x400')

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off", command=show)
c.deselect()
c.pack()

#myBtn = Button(root, text="Show Selection", command=show).pack()


root.mainloop()