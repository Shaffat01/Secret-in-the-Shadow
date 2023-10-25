import tkinter as tk
from tkinter import filedialog
from stegano import lsb

def hide_message(video_path, message):
    secret = lsb.hide(video_path, message)
    secret.save("output_video.avi")

def retrieve_message(video_path):
    secret = lsb.reveal(video_path)
    return secret

def select_video():
    file_path = filedialog.askopenfilename(title="Select Video File")
    video_path.set(file_path)

def hide_button_clicked():
    video = video_path.get()
    message = message_entry.get()
    try:
        hide_message(video, message)
        message_entry.delete(0, tk.END)
        message_entry.insert(0, "Message hidden successfully!")
    except Exception as e:
        message_entry.delete(0, tk.END)
        message_entry.insert(0, str(e))

def retrieve_button_clicked():
    video = video_path.get()
    try:
        message = retrieve_message(video)
        message_entry.delete(0, tk.END)
        message_entry.insert(0, message)
    except Exception as e:
        message_entry.delete(0, tk.END)
        message_entry.insert(0, str(e))

# GUI setup
window = tk.Tk()
window.title("Video Steganography")

video_path = tk.StringVar()

video_label = tk.Label(window, text="Video File:")
video_label.pack()

video_frame = tk.Frame(window)
video_frame.pack()

video_entry = tk.Entry(video_frame, textvariable=video_path, width=40)
video_entry.pack(side=tk.LEFT)

video_button = tk.Button(video_frame, text="Select", command=select_video)
video_button.pack(side=tk.LEFT)

message_label = tk.Label(window, text="Message:")
message_label.pack()

message_entry = tk.Entry(window, width=40)
message_entry.pack()

hide_button = tk.Button(window, text="Hide Message", command=hide_button_clicked)
hide_button.pack()

retrieve_button = tk.Button(window, text="Retrieve Message", command=retrieve_button_clicked)
retrieve_button.pack()

window.mainloop()
