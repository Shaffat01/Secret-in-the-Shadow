import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import librosa



def open_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav;*.mp3")])
    if file_path:
        audio, sr = librosa.load(file_path)
        plt.figure(figsize=(10, 4))
        plt.plot(audio)
        plt.title("Waveform")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()


root = tk.Tk()
root.title("Hystogram Generator")
root.geometry("600x600+400+100")
root.config(bg="#73738c")
img = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 900),))
lbl = tk.Label(root, width=400, height=400, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, width=600, height=600, anchor='center')

title = tk.Label(root, text="Hystogram Generator", font=('arial', 20, 'bold'), width=50, height=3, bg="#417be8")
title.pack(padx=30, pady=50)

def on_enter(event):
    root.open_audio.config(bg='#03fcca')

def on_leave(event):
    root.open_audio.config(bg='#3f256e')

root.open_audio = tk.Button(root, text="AUdio", command=open_audio, bg="#7fe3e1", font=("Helvetica", 12), width=20, height=2)
root.open_audio.pack(pady=10)
root.open_audio.bind("<Enter>", on_enter)
root.open_audio.bind("<Leave>", on_leave)

root.mainloop()
