import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def open_image():
    file_path = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 200))
        img_data.append(np.array(image))
        image_tk = ImageTk.PhotoImage(image)
        image_labels[len(img_data) - 1].config(image=image_tk)
        image_labels[len(img_data) - 1].image = image_tk


def combine_images():
    if len(img_data) < 2:
        messagebox.showinfo("Error", "Please select at least two images.")
        return

    if np.array_equal(img_data[0], img_data[1]):
        messagebox.showinfo("No Change", "No changes made to the images. Please select different images.")
        return

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    for i in range(2):
        axs[0, i].imshow(img_data[i], cmap='gray')
        axs[0, i].axis('off')
        axs[0, i].set_title(f"Histogram {i+1}")

    combined = np.abs(img_data[0] - img_data[1])
    im = axs[1, 0].imshow(combined, cmap='gray')
    axs[1, 0].axis('on')
    axs[1, 0].set_title("Combined Difference")
    plt.colorbar(im, ax=axs[1, 0])

    local_maxima = combined.max() - combined < 5
    coordinates = np.where(local_maxima)
    x_coords = coordinates[0]
    y_coords = coordinates[1]

    for x, y in zip(x_coords, y_coords):
        rect = patches.Rectangle((y-0.5, x-0.5), 1, 1, linewidth=1, edgecolor='red', facecolor='none')
        axs[1, 0].add_patch(rect)

    plt.tight_layout()
    plt.show()

    total_pixels = combined.size
    changed_pixels = np.count_nonzero(combined)
    percentage_change = (changed_pixels / total_pixels) * 100
    percentage_label.config(text=f"Percentage of Change: {percentage_change:.2f}%")


root = tk.Tk()
root.title("Histogram Comparison")
root.geometry("900x600")

canvas = tk.Canvas(root, width=900, height=600, bg="#73738c")
canvas.pack()

bg_image = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 600), Image.ANTIALIAS))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="Histogram Comparison", font=("Arial", 20), bg="#417be8")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

image_labels = []
for i in range(2):
    label = tk.Label(root)
    label.place(relx=(0.3 + 0.4 * i), rely=0.4, anchor=tk.CENTER)
    image_labels.append(label)

open_button = tk.Button(root, text="Open Image", command=open_image, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
open_button.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

combine_button = tk.Button(root, text="Open Image", command=open_image, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
combine_button.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

combine_button = tk.Button(root, text="Compare", command=combine_images, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
combine_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

percentage_label = tk.Label(root, text="", font=("Arial", 12), bg="#417be8")
percentage_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

img_data = []

root.mainloop()
