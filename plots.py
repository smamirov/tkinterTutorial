from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Plots")
root.geometry('400x200')

def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.hist(housePrices, 50)
    plt.show()

myBtn = Button(root, text="Graph", command=graph)
myBtn.pack()

root.mainloop()