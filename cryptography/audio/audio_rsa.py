import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import cv2


def generate_keys():
    (public_key, private_key) = rsa.newkeys(2048)

    with open("private_key.pem", "wb") as file:
        file.write(private_key.save_pkcs1())

    with open("public_key.pem", "wb") as file:
        file.write(public_key.save_pkcs1())


def pad(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padding_value = bytes([padding_length]) * padding_length
    return data + padding_value


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def encrypt():
    file_path = filedialog.askopenfilename()
    save_file_path = filedialog.asksaveasfilename(defaultextension=".mp3")

    public_key_path = filedialog.askopenfilename(
        title="Select Public Key", filetypes=(("Public Key Files", "*.pem"),)
    )

    if not public_key_path:
        messagebox.showerror("Error", "Please select a public key file.")
        return

    with open(public_key_path, "rb") as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())

    aes_key = os.urandom(32)
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())

    with open(file_path, "rb") as input_file:
        with open(save_file_path, "wb") as output_file:
            output_file.write(encrypted_aes_key)
            output_file.write(iv)

            while True:
                chunk = input_file.read(4096)
                if not chunk:
                    break

                padded_chunk = pad(chunk, algorithms.AES.block_size)
                encrypted_chunk = cipher.encryptor().update(padded_chunk)

                output_file.write(encrypted_chunk)

    messagebox.showinfo("Info", "Encryption successful!")


def decrypt():
    file_path = filedialog.askopenfilename()
    save_file_path = filedialog.asksaveasfilename(defaultextension=".mp3")

    private_key_path = filedialog.askopenfilename(
        title="Select Private Key", filetypes=(("Private Key Files", "*.pem"),)
    )

    if not private_key_path:
        messagebox.showerror("Error", "Please select a private key file.")
        return

    with open(private_key_path, "rb") as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())

    with open(file_path, "rb") as input_file:
        encrypted_aes_key = input_file.read(256)
        iv = input_file.read(16)

        aes_key = rsa.decrypt(encrypted_aes_key, private_key)

        cipher = Cipher(
            algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend()
        )

        with open(save_file_path, "wb") as output_file:
            while True:
                encrypted_chunk = input_file.read(4096)
                if not encrypted_chunk:
                    break

                decrypted_chunk = cipher.decryptor().update(encrypted_chunk)
                unpadded_chunk = unpad(decrypted_chunk)

                output_file.write(unpadded_chunk)

    messagebox.showinfo("Info", "Decryption successful!")


root = tk.Tk()
root.title("Audio Encryption and Decryption With RSA")
root.geometry("900x700+300+50")
root.config(bg="#73738c")
# img = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 900), Image.ANTIALIAS))
# lbl = tk.Label(root, width=400, height=400, image=img)
# lbl.img = img
# lbl.place(relx=0.5, rely=0.5, width=900, height=700, anchor='center')


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
    text="Audio Cryptography with RSA",
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


generate_keys()

root.mainloop()
