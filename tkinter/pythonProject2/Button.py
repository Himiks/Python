from tkinter import *
root = Tk()

e = Entry(root, width=50, fg="yellow", bg="blue", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    myLabel = Label(root, text="Hello" + " " + e.get())
    myLabel.pack()

myButton = Button(root, text="Confirm", padx=50, pady=50, command=myClick, fg="blue", bg="yellow")

myButton.pack()

root.mainloop()