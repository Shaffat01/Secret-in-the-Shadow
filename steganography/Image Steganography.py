import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import stegano
from stegano import lsb
from subprocess import call
import tkinter.messagebox as mbox
import os


def hide_message():
    global photo, original_image, label

    file_path = filedialog.askopenfilename(title="Select Cover Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        image_cover = Image.open(file_path)
        image_cover = image_cover.convert("RGB")

        secret_message = entry.get()

        if not secret_message:
            mbox.showerror("Error", "Please enter a secret message.")
            return

        image_stego = lsb.hide(image_cover, secret_message)
        output_path = os.path.join(os.getcwd(), "encoded.png")
        image_stego.save(output_path)

        window = tk.Toplevel()
        window.title("Stego Image")

        img = Image.open(output_path)
        img.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(window, image=photo)
        label.pack()
        original_image = output_path

        mbox.showinfo("Hide Message", "Secret message hidden successfully.")
        window.mainloop()


def extract_message():
    global photo, original_image, label

    file_path = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("Image Files", "*.png")])

    if file_path:
        image_stego = Image.open(file_path)
        image_stego = image_stego.convert("RGB")

        secret_message = lsb.reveal(image_stego)

        window = tk.Toplevel()
        window.title("Extracted Message")

        text = tk.Text(window, width=100, height=100)
        text.insert(tk.END, secret_message)
        text.pack(font=40)
        original_image = None

        mbox.showinfo("Extract Message", "Secret message extracted successfully.")
        window.mainloop()



window = tk.Tk()
window.title("Image Steganography")
window.geometry("900x700+300+50")
img = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 900),))
lbl = tk.Label(window, width=900, height=700, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, width=900, height=700, anchor='center')

title = tk.Label(window, text="Image Steganography", font=('arial', 20, 'bold'), width=50, height=3, bg="orange")
title.pack(padx=30, pady=50)

entry_label = tk.Label(window, text="Secret Message:", font=('arial', 15, 'bold'))
entry_label.pack()

entry = tk.Entry(window, font=('arial', 16))
entry.pack(pady=16)


def on_enter(event):
    window.hide_button.config(bg='#03fcca')
def on_leave(event):
    window.hide_button.config(bg='orange')
window.hide_button = tk.Button(window, text="Encrypt", command=hide_message, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.hide_button.pack(pady=10)
window.hide_button.bind("<Enter>", on_enter)
window.hide_button.bind("<Leave>", on_leave)


def on_enter(event):
    window.extract_button.config(bg='#03fcca')
def on_leave(event):
    window.extract_button.config(bg='orange')
window.extract_button = tk.Button(window, text="Decrypt", command=extract_message, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.extract_button.pack(pady=10)
window.extract_button.bind("<Enter>", on_enter)
window.extract_button.bind("<Leave>", on_leave)



def hist():
    call(["python", "histogram.py"])

def on_enter(event):
    window.hist.config(bg='#03fcca')
def on_leave(event):
    window.hist.config(bg='orange')
window.hist = tk.Button(window, text="Hystogram", command=hist, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.hist.pack(pady=10)
window.hist.bind("<Enter>", on_enter)
window.hist.bind("<Leave>", on_leave)



photo = None
original_image = None
label = None

window.mainloop()
