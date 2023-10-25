import tkinter as tk
from tkinter import *
import cv2
from tkinter import Menu
from subprocess import call
from tkinter import messagebox as mBox
from PIL import ImageTk, Image


class AdsucApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio Cryptography")
        self.geometry("900x700+300+50")
        self.configure(bg="#73738c")
        self.video = cv2.VideoCapture("h.mp4")
        self.video_label = tk.Label(self)
        self.video_label.place(x=0, y=0)

        def update_frame():
            ret, frame = self.video.read()

            if ret:
                frame = cv2.resize(frame, (900, 700))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                self.video_label.configure(image=photo)
                self.video_label.image = photo

            self.after(33, update_frame)
        update_frame()

        self.resizable(0, 0)
        self.menuBar = tk.Menu(self)
        self.configure(menu=self.menuBar)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.exitt)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.clickabout)
        self.menuBar.add_cascade(label="About", menu=self.helpMenu)

        # ============================================================Frames============================================
        self.EFrame = LabelFrame(self, width=900, height=700, font=('arial', 10, 'bold'), bg='orange',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=0, column=0,padx=28, pady=100)

        self.btnExit = Button(self.EFrame, text='Audio CRYPTOGRAPHY',bg="#ffffff", font=('arial', 20, 'bold'), width=35, command=self.exitt)
        self.btnExit.grid(row=0, column=0, padx=50, pady=20)
        
        self.EFrame = LabelFrame(self, width=500, height=500, font=('arial', 10, 'bold'), bg='yellow',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=1, column=0,padx=50, pady=20)
        
        def on_enter(event):
            self.base.config(bg='#03fcca')
        def on_leave(event):
            self.base.config(bg='#3f256e')
        self.base = Button(self.EFrame, text='Base64 program', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.base)
        self.base.grid(row=0, column=0, padx=10, pady=10)
        self.base.bind("<Enter>", on_enter)
        self.base.bind("<Leave>", on_leave)


        def on_enter(event):
            self.aes.config(bg='#03fcca')
        def on_leave(event):
            self.aes.config(bg='#3f256e')
        self.aes = Button(self.EFrame, text='AES program', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.aes)
        self.aes.grid(row=0, column=1, padx=10, pady=10)
        self.aes.bind("<Enter>", on_enter)
        self.aes.bind("<Leave>", on_leave)


        def on_enter(event):
            self.rsa.config(bg='#03fcca')
        def on_leave(event):
            self.rsa.config(bg='#3f256e')
        self.rsa = Button(self.EFrame, text='RSA program', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.rsa)
        self.rsa.grid(row=0, column=2, padx=10, pady=10)
        self.rsa.bind("<Enter>", on_enter)
        self.rsa.bind("<Leave>", on_leave)


        def on_enter(event):
            self.exitt.config(bg='#03fcca')
        def on_leave(event):
            self.exitt.config(bg='#3f256e')
        self.exitt = Button(self.EFrame, text='Exit', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.exitt)
        self.exitt.grid(row=1, column=0, padx=10, pady=10)
        self.exitt.bind("<Enter>", on_enter)
        self.exitt.bind("<Leave>", on_leave)



        def on_enter(event):
            self.hist.config(bg='#03fcca')
        def on_leave(event):
            self.hist.config(bg='#3f256e')
        self.hist = Button(self.EFrame, text='histogram', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.hist)
        self.hist.grid(row=1, column=2, padx=10, pady=10)
        self.hist.bind("<Enter>", on_enter)
        self.hist.bind("<Leave>", on_leave)
        
        
    def base(self):
        call(["python", "cryptography/audio/audio.py"])

    def aes(self):
        call(["python", "cryptography/audio/aes.py"])

    def rsa(self):
        call(["python", "cryptography/audio/audio_rsa.py"])
    
    def hist(self):
         call(["python", "histogram.py"])



    def exitt(self):
        self.destroy()
        
    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()