from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select image file", filetype = (("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All file", "how are you.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image = img)
    lbl.image = img

fun = Tk()

fram = Frame(fun)
fram.pack(side = BOTTOM, padx = 15, pady = 15)

lbl = Label(fun)
lbl.pack()

btn = Button(fram, text = "Select Image", command = showimage)
btn.pack(side = tk.LEFT)

btn2 = Button(fram, text = "Exit", command = lambda:exit())
btn2.pack(side = tk.LEFT, padx = 12)

fun.title("Talha's Image Viewer")
fun.geometry("400x500")
fun.mainloop()