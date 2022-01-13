from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.geometry('400x400')

def resize():
    hlabel = Label(root, text=horizontal.get()).pack()
    root.geometry(f'{horizontal.get()}x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL) #command=resize
horizontal.pack()



hlabel = Label(root, text=horizontal.get()).pack()
resize = Button(root, text="Resize Window", command=resize).pack()

root.mainloop()