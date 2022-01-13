from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Windows")

def open():
    global img
    top = Toplevel()
    top.title("Second Window")
    img = ImageTk.PhotoImage(Image.open('zorosnip.PNG'))
    lbl = Label(top, image=img).pack()
    closeBtn = Button(top, text='Close', command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()
