import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet
import cv2


def generate_key():
    key = Fernet.generate_key()
    with open("AES.key", "wb") as key_file:
        key_file.write(key)


def encrypt():
    file_path = filedialog.askopenfilename()
    with open(file_path, "rb") as file:
        audio_bytes = file.read()

    key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if not key_path:
        messagebox.showerror("Error", "Please select an AES key file.")
        return

    with open(key_path, "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)
    encrypted_audio = cipher_suite.encrypt(audio_bytes)

    save_file_path = filedialog.asksaveasfilename(defaultextension=".wav")
    with open(save_file_path, "wb") as file:
        file.write(encrypted_audio)

    messagebox.showinfo("Info", "Encryption successful!")


def decrypt():
    file_path = filedialog.askopenfilename()
    with open(file_path, "rb") as file:
        encrypted_audio = file.read()

    key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
    if not key_path:
        messagebox.showerror("Error", "Please select an AES key file.")
        return

    with open(key_path, "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)
    decrypted_audio = cipher_suite.decrypt(encrypted_audio)

    save_file_path = filedialog.asksaveasfilename(defaultextension=".wav")
    with open(save_file_path, "wb") as file:
        file.write(decrypted_audio)

    messagebox.showinfo("Info", "Decryption successful!")


root = tk.Tk()
root.title("Audio Encryption and Decryption With AES")
root.geometry("900x700+300+50")
root.config(bg="#73738c")
root.video = cv2.VideoCapture("bb.mp4")
root.video_label = tk.Label(root)
root.video_label.place(x=0, y=0)


def update_frame():
    ret, frame = root.video.read()

    if ret:
        frame = cv2.resize(frame, (900, 700))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        root.video_label.configure(image=photo)
        root.video_label.image = photo
    root.after(33, update_frame)


update_frame()


title = tk.Label(
    root,
    text="Audio Cryptography with AES",
    font=("arial", 20, "bold"),
    width=50,
    height=3,
    bg="#417be8",
)
title.pack(padx=30, pady=50)


def on_enter(event):
    root.encrypt_button.config(bg="#03fcca")


def on_leave(event):
    root.encrypt_button.config(bg="#3f256e")


root.encrypt_button = tk.Button(
    root,
    text="Encrypt",
    command=encrypt,
    bg="#7fe3e1",
    font=("Helvetica", 12),
    width=20,
    height=2,
)
root.encrypt_button.pack(pady=10)
root.encrypt_button.bind("<Enter>", on_enter)
root.encrypt_button.bind("<Leave>", on_leave)


def on_enter(event):
    root.decrypt_button.config(bg="#03fcca")


def on_leave(event):
    root.decrypt_button.config(bg="#3f256e")


root.decrypt_button = tk.Button(
    root,
    text="Decrypt",
    command=decrypt,
    bg="#7fe3e1",
    font=("Helvetica", 12),
    width=20,
    height=2,
)
root.decrypt_button.pack(pady=10)
root.decrypt_button.bind("<Enter>", on_enter)
root.decrypt_button.bind("<Leave>", on_leave)

generate_key()

root.mainloop()
