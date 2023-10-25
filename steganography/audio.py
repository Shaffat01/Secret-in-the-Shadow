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
        self.title("LOGGED IN")
        self.geometry("900x700+300+50")
        self.configure(bg="#73738c")
        self.video = cv2.VideoCapture("bb.mp4")  
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
        self.EFrame = LabelFrame(self, width=500, height=200, font=('arial', 10, 'bold'), bg='orangered',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=0, column=0,padx=28, pady=100)

        self.btnExit = Button(self.EFrame, text='Audio STEGANOGRAPHY',bg="#ffffff", font=('arial', 20, 'bold'), width=35, command=self.exitt)
        self.btnExit.grid(row=0, column=0, padx=10, pady=20)
        
        self.EFrame = LabelFrame(self, width=500, height=500, font=('arial', 10, 'bold'), bg='yellow',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=1, column=0,padx=30, pady=20)

        
        def on_enter(event):
            self.btnExit.config(bg='#03fcca')
        def on_leave(event):
            self.btnExit.config(bg='orangered')
        self.btnExit = Button(self.EFrame, text='EXIT',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.exitt)
        self.btnExit.grid(row=2, column=1, padx=10, pady=10)
        self.btnExit.bind("<Enter>", on_enter)
        self.btnExit.bind("<Leave>", on_leave)
        
        

        def on_enter(event):
            self.audio_txt.config(bg='#03fcca')
        def on_leave(event):
            self.audio_txt.config(bg='#3f256e')
        self.audio_txt = Button(self.EFrame, text='Secret Text',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.audio_txt)
        self.audio_txt.grid(row=1, column=2, padx=10, pady=10)
        self.audio_txt.bind("<Enter>", on_enter)
        self.audio_txt.bind("<Leave>", on_leave)

        def on_enter(event):
            self.audio_img.config(bg='#03fcca')
        def on_leave(event):
            self.audio_img.config(bg='#3f256e')
        self.audio_img = Button(self.EFrame, text='Secret Image Steganography',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.audio_img)
        self.audio_img.grid(row=1, column=0, padx=10, pady=10)
        self.audio_img.bind("<Enter>", on_enter)
        self.audio_img.bind("<Leave>", on_leave)


        def on_enter(event):
            self.audio_aud.config(bg='#03fcca')
        def on_leave(event):
            self.audio_aud.config(bg='#3f256e')
        self.audio_aud = Button(self.EFrame, text='Secret Audio Steganography', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.audio_aud)
        self.audio_aud.grid(row=3, column=0, padx=10, pady=10)
        self.audio_aud.bind("<Enter>", on_enter)
        self.audio_aud.bind("<Leave>", on_leave)

        def on_enter(event):
            self.stg.config(bg='#03fcca')
        def on_leave(event):
            self.stg.config(bg='#3f256e')
        self.stg = Button(self.EFrame, text='Steganography Dashboard', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.stg)
        self.stg.grid(row=3, column=2, padx=10, pady=10)
        self.stg.bind("<Enter>", on_enter)
        self.stg.bind("<Leave>", on_leave)


        def on_enter(event):
            self.hist.config(bg='#03fcca')
        def on_leave(event):
            self.hist.config(bg='#3f256e')
        self.hist = Button(self.EFrame, text='Histogram ', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.hist)
        self.hist.grid(row=3, column=1, padx=10, pady=10)
        self.hist.bind("<Enter>", on_enter)
        self.hist.bind("<Leave>", on_leave)


    def audio_aud(self):
        call(["python", "steganography/audio_staganogaphy/audio_aud_stg.py"])

    def audio_img(self):
        call(["python", "steganography/audio_staganogaphy/audio_img_stg.py"])
    
    def audio_txt(self):
        call(["python", "steganography/audio_staganogaphy/audio_stg.py"])
    

    def stg(self):
        call(["python", "steganography.py"])

    def hist(self):
        call(["python", "histogram.py"])
    

    def exitt(self):
        self.destroy()

    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()