import base64
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
import cv2

def encrypt():
    file_path = filedialog.askopenfilename()
    with open(file_path, "rb") as file:
        video_bytes = file.read()

    encrypted_video = base64.b64encode(video_bytes)

    save_file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    with open(save_file_path, "wb") as file:
        file.write(encrypted_video)

    messagebox.showinfo("Info", "Encryption successful!")

def decrypt():
    file_path = filedialog.askopenfilename()
    with open(file_path, "rb") as file:
        encrypted_video = file.read()

    decrypted_video = base64.b64decode(encrypted_video)

    save_file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    with open(save_file_path, "wb") as file:
        file.write(decrypted_video)

    messagebox.showinfo("Info", "Decryption successful!")

root = tk.Tk()
root.title("Video Encryption and Decryption")
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


title = tk.Label(root, text="Video Encryption and Decryption",font=('arial', 20, 'bold'),width=50,height=3,bg="#417be8")
title.pack(padx=30,pady=50)

def on_enter(event):
            root.encrypt_button.config(bg='#03fcca')
def on_leave(event):
            root.encrypt_button.config(bg='#3f256e')
root.encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
root.encrypt_button.pack(pady=10)
root.encrypt_button.bind("<Enter>", on_enter)
root.encrypt_button.bind("<Leave>", on_leave)

def on_enter(event):
            root.decrypt_button.config(bg='#03fcca')
def on_leave(event):
            root.decrypt_button.config(bg='#3f256e')
root.decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
root.decrypt_button.pack(pady=10)
root.decrypt_button.bind("<Enter>", on_enter)
root.decrypt_button.bind("<Leave>", on_leave)

root.mainloop()
