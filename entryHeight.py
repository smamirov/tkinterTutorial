from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Entry Height")
root.geometry('400x400')

def myclick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, END)
    myLabel.pack(pady=10)

e = Entry(root, width=50, font=('Ariel', 30))
e.pack(padx=10, pady=10)

myBtn = Button(root, text="Button", command=myclick)
myBtn.pack(pady=10)

root.mainloop()