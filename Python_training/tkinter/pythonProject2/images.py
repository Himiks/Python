from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icon")
root.iconbitmap("channel.jpg")

img = ImageTk.PhotoImage(Image.open("channel.jpg"))

my_label = Label(image=img)
my_label.pack()





button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()


root.mainloop()