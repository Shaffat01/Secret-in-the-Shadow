import tkinter as tk
from PIL import ImageTk, Image
import cv2

def encrypt_text():
    key = int(entry_key.get())
    plaintext = entry_text.get("1.0", "end-1c")
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            ascii_val = ord(char)
            if char.isupper():
                ascii_val = (ascii_val - 65 + key) % 26 + 65
            else:
                ascii_val = (ascii_val - 97 + key) % 26 + 97
            char = chr(ascii_val)
        encrypted_text += char
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)
    entry_text.delete("1.0", "end")  # Clear input data

def decrypt_text():
    key = int(entry_key.get())
    ciphertext = entry_text.get("1.0", "end-1c")
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_val = ord(char)
            if char.isupper():
                ascii_val = (ascii_val - 65 - key) % 26 + 65
            else:
                ascii_val = (ascii_val - 97 - key) % 26 + 97
            char = chr(ascii_val)
        decrypted_text += char
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)
    entry_text.delete("1.0", "end")  # Clear input data

# Create the main window
window = tk.Tk()
window.title("Video Encryption and Decryption")
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

# Create labels
label_key = tk.Label(window, text="Key:",font=('arial', 20, 'bold'), width=7, height=1, bg="#417be8")
label_key.grid(row=0, column=0, sticky=tk.W,padx=100,pady=50)
label_text = tk.Label(window, text="Text:",font=('arial', 20, 'bold'), width=7, height=1, bg="#417be8")
label_text.grid(row=1, column=0, sticky=tk.W,padx=100,pady=30)
label_output = tk.Label(window, text="Output:",font=('arial', 20, 'bold'), width=7, height=1, bg="#417be8")
label_output.grid(row=2, column=0, sticky=tk.W,padx=100,pady=30)

# Create entry fields
entry_key = tk.Entry(window,font=('arial', 20, 'bold'), bg="orange")
entry_key.grid(row=0, column=1)
entry_text = tk.Text(window, height=5, width=30,font=('arial', 20, 'bold'), bg="orange")
entry_text.grid(row=1, column=1,pady=30)
output_text = tk.Text(window, height=5, width=30,font=('arial', 20, 'bold'), bg="orange")
output_text.grid(row=2, column=1)

# Create buttons
encrypt_button = tk.Button(window, text="Encrypt",font=('arial', 20, 'bold'), width=7, height=1, bg="#417be8",command=encrypt_text)
encrypt_button.grid(row=3, column=1, padx=5, pady=5)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text,font=('arial', 20, 'bold'), width=7, height=1, bg="#417be8")
decrypt_button.grid(row=4, column=1, padx=5, pady=5)

# Run the main loop
window.mainloop()
