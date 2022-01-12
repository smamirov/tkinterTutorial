from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frame Tutorial')

frame = LabelFrame(root, text="Frame", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b= Button(frame, text="Button")
b2 = Button(frame, text="Button2")

# You can use grid within a packed frame
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()