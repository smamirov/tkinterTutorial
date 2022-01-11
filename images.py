from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Fire!")
# Favicon
root.iconbitmap('fire.ico')

# Import an image 
myImage = ImageTk.PhotoImage(Image.open('zorosnip.PNG'))
myLabel = Label(image=myImage)  # Adding it to the label (can be added to anything, even buttons)
myLabel.pack()  # Pack like usual to ust get in on the screen


# Button to quit the program
buttonQuit = Button(root, text="Exit", command=root.quit)
buttonQuit.pack()


root.mainloop()