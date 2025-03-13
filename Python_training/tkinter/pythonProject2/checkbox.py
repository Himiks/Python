from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("checkBox")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box, l dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

my_btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()