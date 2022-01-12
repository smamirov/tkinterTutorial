from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

#r = IntVar()

MODES = [
    ("Pepperoni", "Pepperoni"),  # display - value
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
#pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()



def clicked(option):
    myLabel = Label(root, text=option)
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myButton = Button(root, text="Click Me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()