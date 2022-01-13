from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Dialog")

def open():
    global myimg
    root.filename = filedialog.askopenfilename(initialdir='E:/VSCode/tkintertutorial', title="Select a File", filetypes=(("all files", "*.*"), ("png files", "*.png")))
    myLabel = Label(root, text=root.filename).pack()
    myimg = ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel = Label(image=myimg).pack()

mybtn = Button(root, text="Select an Image", command=open).pack()


root.mainloop()