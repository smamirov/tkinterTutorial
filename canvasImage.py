from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images with Canvas")
root.geometry('500x500')

myCanvas = Canvas(root, width=600, height=400, bg="white")
myCanvas.pack(pady=20)

img = PhotoImage(file="rollercoaster.png")
myCanvas.create_image(0, 0, anchor='nw', image=img)

root.mainloop()