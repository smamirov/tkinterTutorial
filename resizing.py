import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.button = tk.Button(self.frame, text='Open New Window', command=self.openNew)
        self.button.grid(row=0, column=0, sticky='nsew')
    
    def openNew(self):
        self.secondWin = tk.Toplevel()
        self.myLbl = tk.Label(self.secondWin, text="You opened new window.")
        self.myLbl.grid()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()