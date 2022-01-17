from tkinter import *

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        #self.resizable(False, False)

    def label(self):
        self.myLabel = Label(self, text="Hello World!")
        self.myLabel.pack()

if __name__=="__main__":
    root = Login()
    root.label()
    root.mainloop()
