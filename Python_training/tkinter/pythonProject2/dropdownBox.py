from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("checkBox")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()



root.mainloop()