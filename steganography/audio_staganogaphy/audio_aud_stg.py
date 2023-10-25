import wave
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
import imageio
from PIL import Image, ImageTk


def encrypt_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
    selected_file_label.config(text="Selected File: " + file_path)

    with wave.open(file_path, 'rb') as audio_file:
        audio_data = bytearray(audio_file.readframes(audio_file.getnframes()))

    secret_file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
    secret_file_size = os.path.getsize(secret_file_path)

    if secret_file_size * 8 > len(audio_data):
        status_label.config(text="Host audio file is too short to embed the secret audio.")
        return

    with wave.open(secret_file_path, 'rb') as secret_file:
        secret_data = bytearray(secret_file.readframes(secret_file.getnframes()))

    secret_size = len(secret_data)

    for i, byte in enumerate(secret_data):
        for j in range(8):
            index = i * 8 + j
            audio_data[index] = (audio_data[index] & 0xFE) | ((byte >> (7 - j)) & 0x01)

    directory = os.path.dirname(file_path)
    output_path = os.path.join(directory, "encrypted_audio.wav")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    loading_image_path = os.path.join(current_dir, "h.gif")

    loading_frames = imageio.mimread(loading_image_path)
    num_frames = len(loading_frames)

    loading_images = [Image.fromarray(frame) for frame in loading_frames]

    loading_label = tk.Label(window)
    loading_label.pack()

    def update_loading_animation(frame_index):
        image = ImageTk.PhotoImage(loading_images[frame_index])
        loading_label.config(image=image)
        loading_label.image = image
        frame_index = (frame_index + 1) % num_frames
        window.after(100, update_loading_animation, frame_index)

    update_loading_animation(0)

    with wave.open(output_path, 'wb') as encrypted_file:
        encrypted_file.setparams(audio_file.getparams())
        encrypted_file.writeframes(audio_data)

    status_label.config(text="Audio encryption completed.")

    def hide_loading_label():
        loading_label.pack_forget()

    window.after(4000, hide_loading_label)


def decrypt_audio():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
    selected_file_label.config(text="Selected File: " + file_path)

    with wave.open(file_path, 'rb') as audio_file:
        audio_data = bytearray(audio_file.readframes(audio_file.getnframes()))

    secret_data = bytearray()
    byte = 0

    for i in range(len(audio_data)):
        bit = audio_data[i] & 0x01
        byte = (byte << 1) | bit

        if (i + 1) % 8 == 0:
            secret_data.append(byte)
            byte = 0

    output_path = os.path.join(os.path.dirname(file_path), "decrypted_audio.wav")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    loading_image_path = os.path.join(current_dir, "h.gif")

    loading_frames = imageio.mimread(loading_image_path)
    num_frames = len(loading_frames)

    loading_images = [Image.fromarray(frame) for frame in loading_frames]

    loading_label = tk.Label(window)
    loading_label.pack()

    def update_loading_animation(frame_index):
        image = ImageTk.PhotoImage(loading_images[frame_index])
        loading_label.config(image=image)
        loading_label.image = image
        frame_index = (frame_index + 1) % num_frames
        window.after(100, update_loading_animation, frame_index)

    update_loading_animation(0)

    with wave.open(output_path, 'wb') as decrypted_file:
        decrypted_file.setparams(audio_file.getparams())
        decrypted_file.writeframes(secret_data)

    status_label.config(text="Audio decryption completed")

    def hide_loading_label():
        loading_label.pack_forget()

    window.after(4000, hide_loading_label)


window = tk.Tk()
window.title("Audio to Audio Steganography")
window.geometry("900x700+300+50")
window.configure(bg="#73738c")
window.video = cv2.VideoCapture("h.mp4")

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

secret_message_label = tk.Label(window, text="Audio Steganography", bg="orangered", font=('arial', 30, 'bold'),
                                width=35, height=3)
secret_message_label.pack(pady=40)

encrypt_button = tk.Button(window, text="Encrypt", bg="orangered", font=('arial', 15, 'bold'), width=13,
                           command=encrypt_audio)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Decrypt", bg="orangered", font=('arial', 15, 'bold'), width=13,
                           command=decrypt_audio)
decrypt_button.pack(pady=5)



selected_file_label = tk.Label(window, text="File Path: ", bg="orangered", font=('arial', 15, 'bold'), width=50)
selected_file_label.pack(pady=5)

status_label = tk.Label(window, text="", bg="#765bf0", font=('arial', 20, 'bold'), width=45)
status_label.pack(pady=15)

window.mainloop()
