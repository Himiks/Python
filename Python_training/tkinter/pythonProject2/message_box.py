from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Box")


def popup():
    responce = messagebox.askyesno("This is my popup!", "Hello World!")
    Label(root, text=responce).pack()
    # if responce == 1:
    #     Label(root, text="YES!").pack()
    # else:
    #     Label(root, text="NO!").pack()


Button(root, text="Popup", command=popup).pack()




root.mainloop()