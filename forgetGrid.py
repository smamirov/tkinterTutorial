from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Forget Grid")
root.geometry('400x400')

myLabel = Label(root)

def myclick():
    global myLabel
    myLabel.destroy()

    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, END)
    myLabel.grid(row=3, column=0, pady=10)
    #myBtn['state'] = DISABLED

'''
def mydelete():
    myLabel.grid_forget()
    #myLabel.destroy()
    myBtn['state'] = NORMAL
    #print(myBtn.winfo_exists())
'''

e = Entry(root, width=17, font=('Ariel', 30))
e.grid(row=0, column=0,padx=10, pady=10)

myBtn = Button(root, text="Enter Your Name", command=myclick)
myBtn.grid(row=1, column=0,pady=10)

'''
deleteButton = Button(root, text="Delete Text", command=mydelete)
deleteButton.grid(row=2, column=0,pady=10)
'''

root.mainloop()