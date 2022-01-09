from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I Clicked a Button!!!")
    myLabel.pack()

# Creating a button
myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()


'''
myButton = Button(root, text="Click Me!", state=DISABLED)       -> button will be greyed out
myButton = Button(root, text="Click Me!", padx=50, pady=50)     -> resize a button
'''