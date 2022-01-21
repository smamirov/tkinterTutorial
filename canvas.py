from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Canvas")
root.geometry('500x500')

myCanvas = Canvas(root, width=300, height=200, bg="white")
myCanvas.pack(pady=10)

# Create a rectangle
# myCanvas.create_rectangle(x1, y1, x2, y2, fill="color")
myCanvas.create_rectangle(50, 150, 250, 50, fill="pink")

# Create an ellipse
# myCanvas.create_oval(x1, y1, x2, y2, fill="color")
myCanvas.create_oval(50, 150, 250, 50, fill="cyan")

# Create a line
# myCanvas.create_line(x1, y1, x2, y2, fill="color")
myCanvas.create_line(0, 100, 300, 100, fill="red")
myCanvas.create_line(150, 0, 150, 200, fill="red")


root.mainloop()