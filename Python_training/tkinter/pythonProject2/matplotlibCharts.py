from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("checkBox")
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


my_button = Button(root, text="Graph It!", command=graph).pack()


root.mainloop()