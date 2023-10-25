import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from subprocess import call
import numpy as np
import tkinter.messagebox as mbox
import os

def en_fun():
    global photo, original_image, label

    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        image_input = cv2.imread(file_path, 0)
        (x1, y) = image_input.shape
        image_input = image_input.astype(float) / 255.0

        mu, sigma = 0, 0.1
        key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
        image_encrypted = image_input / key
        cv2.imwrite('image_encrypted.jpg', image_encrypted * 255)

        window = tk.Toplevel()
        window.title("Encrypted Image")

        img = Image.open('image_encrypted.jpg')
        img.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(window, image=photo)
        label.pack()
        original_image = file_path

        mbox.showinfo("Encrypt Status", "Image Encrypted successfully.")
        window.mainloop()


def de_fun():
    global photo, original_image, label

    file_path = filedialog.askopenfilename(title="Select Encrypted Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        image_encrypted = cv2.imread(file_path, 0)
        (x1, y) = image_encrypted.shape
        image_encrypted = image_encrypted.astype(float) / 255.0

        mu, sigma = 0, 0.1
        key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
        image_decrypted = image_encrypted * key
        cv2.imwrite('image_decrypted.jpg', image_decrypted * 255)
        window = tk.Toplevel()
        window.title("Decrypted Image")

        img = Image.open('image_decrypted.jpg').convert("L")
        img.thumbnail((500, 500)) 
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(window, image=photo)
        label.pack()
        mbox.showinfo("Decrypt Status", "Image Decrypted successfully.")
        window.mainloop()


def reset_fun():
    global photo, original_image, label

    if original_image:
        if original_image == 'image_encrypted.jpg':
            file_path = 'image_encrypted.jpg'
        else:
            file_path = 'image_decrypted.jpg'
        try:
            os.remove(file_path)
        except OSError as e:
            mbox.showerror("Error", f"Failed to delete the file: {str(e)}")
            return

        img = Image.open(original_image)
        img.thumbnail((500, 500))  
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.image = photo
        mbox.showinfo("Reset Status", "Image Reset successfully.")
    else:
        mbox.showinfo("Reset Status", "No image to reset.")


window = tk.Tk()
window.title("Audio Encryption and Decryption")
window.geometry("900x700+300+50")
window.config(bg="#73738c")
window.video = cv2.VideoCapture("bb.mp4")  
window.video_label = tk.Label(window)
window.video_label.place(x=0, y=0)

def update_frame():
    ret, frame = window.video.read()

    if ret:
        frame = cv2.resize(frame, (900, 700))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        window.video_label.configure(image=photo)
        window.video_label.image = photo
    window.after(33, update_frame)

update_frame()


title = tk.Label(window, text="Image Encryption,Decryption and Reset",font=('arial', 20, 'bold'),width=50,height=3,bg="#417be8")
title.pack(padx=30,pady=50)

def on_enter(event):
            window.encrypt_button.config(bg='#03fcca')
def on_leave(event):
            window.encrypt_button.config(bg='#3f256e')
window.encrypt_button = tk.Button(window, text="Encrypt", command=en_fun, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.encrypt_button.pack(pady=10)
window.encrypt_button.bind("<Enter>", on_enter)
window.encrypt_button.bind("<Leave>", on_leave)

def on_enter(event):
            window.decrypt_button.config(bg='#03fcca')
def on_leave(event):
            window.decrypt_button.config(bg='#3f256e')
window.decrypt_button = tk.Button(window, text="Decrypt", command=de_fun, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.decrypt_button.pack(pady=10)
window.decrypt_button.bind("<Enter>", on_enter)
window.decrypt_button.bind("<Leave>", on_leave)

def on_enter(event):
            window.reset_button.config(bg='#03fcca')
def on_leave(event):
            window.reset_button.config(bg='#3f256e')
window.reset_button = tk.Button(window, text="Reset", command=reset_fun, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
window.reset_button.pack(pady=10)
window.reset_button.bind("<Enter>", on_enter)
window.reset_button.bind("<Leave>", on_leave)

def dash():
    call(["python", "dashboard.py"])

def on_enter(event):
            window.dash_button.config(bg='#03fcca')
def on_leave(event):
            window.dash_button.config(bg='#3f256e')
window.dash_button = tk.Button(window, text="Dashboard", bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2,command=dash)
window.dash_button.pack(pady=10)
window.dash_button.bind("<Enter>", on_enter)
window.dash_button.bind("<Leave>", on_leave)


def histogram():
    call(["python", "histogram.py"])

def on_enter(event):
            window.histogram.config(bg='#03fcca')
def on_leave(event):
            window.histogram.config(bg='#3f256e')
window.histogram = tk.Button(window, text="histogram", bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2,command=histogram)
window.histogram.pack(pady=10)
window.histogram.bind("<Enter>", on_enter)
window.histogram.bind("<Leave>", on_leave)

photo = None
original_image = None
label = None

window.mainloop()
