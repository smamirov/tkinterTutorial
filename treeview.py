from operator import index
from tkinter import *
from tkinter import ttk
from unicodedata import name
from PIL import ImageTk, Image

root = Tk()
root.title("Treeview")
root.geometry('500x600')

myTree = ttk.Treeview(root)

# Define Columns
myTree['columns'] = ("Name", "ID", "Favorite Pizza")

# Format columns
myTree.column("#0", width=0, stretch=NO)
myTree.column("Name", anchor=W, width=140)
myTree.column("ID", anchor=CENTER, width=100)
myTree.column("Favorite Pizza", anchor=W, width=140)

# Create headings
myTree.heading("#0", text="Label", anchor=W)
myTree.heading("Name", text="Name", anchor=W)
myTree.heading("ID", text="ID", anchor=CENTER)
myTree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

data = [
    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Pepperoni"],
    ["Bob", 3, "Pepperoni"],
    ["Mary", 4, "Pepperoni"]
]

myTree.tag_configure('odd', background="white")
myTree.tag_configure('even', background="lightblue")

global count
count = 0
for record in data:
    if count % 2 == 0:
        myTree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('even'))
    else:
        myTree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('odd'))
    
    count += 1

'''# Add data
myTree.insert(parent='', index='end', iid=0, text="Parent", values=("John", 1, "Pepperoni"))
myTree.insert(parent='', index='end', iid=1, text="Parent", values=("Mary", 2, "Pepperoni"))
myTree.insert(parent='', index='end', iid=2, text="Parent", values=("Bob", 3, "Pepperoni"))
myTree.insert(parent='', index='end', iid=3, text="Parent", values=("Steve", 4, "Pepperoni"))
myTree.insert(parent='', index='end', iid=4, text="Parent", values=("Luke", 5, "Pepperoni"))'''

myTree.pack(pady=20)

addFrame = Frame(root)
addFrame.pack(pady=20)

# Labels
nl = Label(addFrame, text="Name")
nl.grid(row=0, column=0)

il = Label(addFrame, text="ID")
il.grid(row=0, column=1)

tl = Label(addFrame, text="Topping")
tl.grid(row=0, column=2)

nameBox = Entry(addFrame)
nameBox.grid(row=1, column=0)

idBox = Entry(addFrame)
idBox.grid(row=1, column=1)

toppingBox = Entry(addFrame)
toppingBox.grid(row=1, column=2)


def addRecord():
    global count
    if count % 2 == 0:
        myTree.insert(parent='', index='end', iid=count, text="Parent", values=(nameBox.get(), idBox.get(), toppingBox.get()), tags=('even'))
    else:
        myTree.insert(parent='', index='end', iid=count, text="Parent", values=(nameBox.get(), idBox.get(), toppingBox.get()), tags=('odd'))
    
    count += 1

    nameBox.delete(0, END)
    idBox.delete(0, END)
    toppingBox.delete(0, END)

def removeAll():
    for record in myTree.get_children():
        myTree.delete(record)

def removeOne():
    x = myTree.selection()[0]
    myTree.delete(x)

def removeMany():
    x = myTree.selection()
    for record in x:
        myTree.delete(record)

# Buttons
addRecord = Button(root, text="Add Record", command=addRecord)
addRecord.pack(pady=20)

removeAll = Button(root, text="Remove all records", command=removeAll)
removeAll.pack(pady=20)

removeOne = Button(root, text="Remove One", command=removeOne)
removeOne.pack(pady=10)

removeMany = Button(root, text="Remove Many Selected", command=removeMany)
removeMany.pack(pady=10)

root.mainloop()