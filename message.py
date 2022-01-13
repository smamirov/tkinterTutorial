from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")

def popup():
    # Message box options
    # showinfo, showwarning, showerror, askquestion, askcancel, askyesno
    response = messagebox.askyesno("Wait", "Are you sure?")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text='Yes').pack()
    else:
        Label(root, text='No').pack()



Button(root, text="Popup", command=popup).pack()




root.mainloop()