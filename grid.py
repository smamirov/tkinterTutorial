from tkinter import *

root = Tk()

# Creating a label widget
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Said Mamirov")

# Using grid to place the labels
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()