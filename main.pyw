import random
import os
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("470x450")
root.title("Dice Simulator")
icon = PhotoImage(file = "defaultDice.png")
root.iconphoto(False, icon)

pics = os.listdir("pics")

def roll():
    c = random.choice(pics)
    root.img = ImageTk.PhotoImage(Image.open(os.path.join("pics",c)))
    l.config(image = root.img)

defaultImg = ImageTk.PhotoImage(Image.open("defaultDice.png"))
l = Label(root, image = defaultImg)
l.grid(row = 0, column = 0, padx = 80, pady = 40)

b = Button(root, text = "ROLL", bg = "gold", font = "comicsansms 12 bold", command = roll)
b.grid(row = 1, column = 0)
root.mainloop()
