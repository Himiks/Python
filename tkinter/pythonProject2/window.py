from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Window")


def open():
    global img
    top = Toplevel()
    top.title("Second Window")
    img = ImageTk.PhotoImage(Image.open("name5.jpg"))
    lbl = Label(top, image=img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()


root.mainloop()
