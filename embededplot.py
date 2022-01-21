from tkinter import *
from matplotlib import figure
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


root = Tk()
root.title("Embeded Matplotlib Plot")
root.geometry('800x700')

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(211)

a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

myCanvas = FigureCanvasTkAgg(f, root)
myCanvas.draw()
myCanvas.get_tk_widget().grid(row=0, column=0)

###################
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(211)

a.plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])

myCanvas2 = FigureCanvasTkAgg(f, root)
myCanvas2.draw()
myCanvas2.get_tk_widget().grid(row=0, column=1)



root.mainloop()