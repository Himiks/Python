from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state="disabled")

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<" , state="disabled")

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


img1 = ImageTk.PhotoImage(Image.open("name.jpg"))
img2 = ImageTk.PhotoImage(Image.open("name2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("name4.jpg"))
img4 = ImageTk.PhotoImage(Image.open("name5.jpg"))
img5 = ImageTk.PhotoImage(Image.open("channel.jpg"))

image_list = [img1, img2, img3, img4, img5]
status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)




my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<",command=back, state="disabled")
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1,column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()