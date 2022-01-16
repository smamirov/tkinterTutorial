from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Forget Pack")
root.geometry('400x400')

def myclick():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, END)
    myLabel.pack(pady=10)
    myBtn['state'] = DISABLED

def mydelete():
    #myLabel.pack_forget()
    myLabel.destroy()
    myBtn['state'] = NORMAL
    print(myBtn.winfo_exists())

e = Entry(root, width=50, font=('Ariel', 30))
e.pack(padx=10, pady=10)

myBtn = Button(root, text="Enter Your Name", command=myclick)
myBtn.pack(pady=10)

deleteButton = Button(root, text="Delete Text", command=mydelete)
deleteButton.pack(pady=10)

root.mainloop()