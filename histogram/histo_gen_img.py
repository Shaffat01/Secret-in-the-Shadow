import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import librosa


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path).convert("L")  
        histogram = np.histogram(image, bins=256, range=(0, 255))

        plt.figure(figsize=(8, 5))
        plt.bar(histogram[1][:-1], histogram[0], width=1)
        plt.title("Image Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.show()



root = tk.Tk()
root.title("Hystogram Generator")
root.geometry("600x600+400+100")
root.config(bg="#73738c")
img = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 900), Image.ANTIALIAS))
lbl = tk.Label(root, width=400, height=400, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, width=600, height=600, anchor='center')

title = tk.Label(root, text="Hystogram Generator", font=('arial', 20, 'bold'), width=50, height=3, bg="#417be8")
title.pack(padx=30, pady=50)

def on_enter(event):
    root.open_image.config(bg='#03fcca')

def on_leave(event):
    root.open_image.config(bg='#3f256e')

root.open_image = tk.Button(root, text="Image", command=open_image, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
root.open_image.pack(pady=10)
root.open_image.bind("<Enter>", on_enter)
root.open_image.bind("<Leave>", on_leave)

root.mainloop()
