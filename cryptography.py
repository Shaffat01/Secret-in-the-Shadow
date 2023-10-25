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
        self.EFrame = LabelFrame(self, width=500, height=200, font=('arial', 10, 'bold'), bg='orange',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=0, column=0,padx=28, pady=100)

        self.btnExit = Button(self.EFrame, text='CRYPTOGRAPHY',bg="#ffffff", font=('arial', 20, 'bold'), width=35, command=self.exitt)
        self.btnExit.grid(row=0, column=0, padx=10, pady=20)
        
        self.EFrame = LabelFrame(self, width=500, height=500, font=('arial', 10, 'bold'), bg='yellow',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0,padx=30, pady=20)
        
        def on_enter(event):
            self.btncrypto.config(bg='#03fcca')
        def on_leave(event):
            self.btncrypto.config(bg='#3f256e')
        self.btncrypto = Button(self.EFrame, text='Image_CryptoGraphy', bg="#3f96d9", font=('arial', 10, 'bold'),fg="white",width=30,height=2, command=self.clickcrypto)
        self.btncrypto.grid(row=0, column=0, padx=10, pady=10)
        self.btncrypto.bind("<Enter>", on_enter)
        self.btncrypto.bind("<Leave>", on_leave)
        
        def on_enter(event):
            self.btntext.config(bg='#03fcca')
        def on_leave(event):
            self.btntext.config(bg='#3f256e')
        self.btntext = Button(self.EFrame, text='Text_Cryptography',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2,
                              command=self.clicktext)
        self.btntext.grid(row=0, column=2, padx=10, pady=10)
        self.btntext.bind("<Enter>", on_enter)
        self.btntext.bind("<Leave>", on_leave)
        
        def on_enter(event):
            self.btnExit.config(bg='#03fcca')
        def on_leave(event):
            self.btnExit.config(bg='orangered')
        self.btnExit = Button(self.EFrame, text='EXIT',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.exitt)
        self.btnExit.grid(row=1, column=1, padx=10, pady=10)
        self.btnExit.bind("<Enter>", on_enter)
        self.btnExit.bind("<Leave>", on_leave)
        

        def on_enter(event):
            self.btnaudio.config(bg='#03fcca')
        def on_leave(event):
            self.btnaudio.config(bg='#3f256e')
        self.btnaudio = Button(self.EFrame, text='Audio_Cryptography', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.clickaudio)
        self.btnaudio.grid(row=2, column=0, padx=10, pady=10)
        self.btnaudio.bind("<Enter>", on_enter)
        self.btnaudio.bind("<Leave>", on_leave)

        def on_enter(event):
            self.btnvideo.config(bg='#03fcca')
        def on_leave(event):
            self.btnvideo.config(bg='#3f256e')
        self.btnvideo = Button(self.EFrame, text='Video_Cryptography', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.clickvideo)
        self.btnvideo.grid(row=2, column=2, padx=10, pady=10)
        self.btnvideo.bind("<Enter>", on_enter)
        self.btnvideo.bind("<Leave>", on_leave)

        self.EFrame = LabelFrame(self, width=500, height=100, font=('arial', 10, 'bold'), bg='yellow',relief='ridge', bd=13)
        self.EFrame.grid(row=3, column=0,padx=30, pady=10)

        def on_enter(event):
            self.Dashboard.config(bg='#03fcca')
        def on_leave(event):
            self.Dashboard.config(bg='#3f256e')
        self.Dashboard = Button(self.EFrame, text='Dashboard', bg='#3f96d9', font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.clickdashboard)
        self.Dashboard.grid(row=3, column=2, padx=10, pady=10)
        self.Dashboard.bind("<Enter>", on_enter)
        self.Dashboard.bind("<Leave>", on_leave)  


    def clickcrypto(self):
        call(["python", "cryptography/image_crypto.py"])

    def clicktext(self):
        call(["python", "cryptography/text.py"])

    def clickaudio(self):
        call(["python", "cryptography/Audio_crypto.py"])
    
    def clickvideo(self):
        call(["python", "cryptography/video.py"])

    def clickdashboard(self):
        call(["python", "dashboard.py"])
    
    def exitt(self):
        self.destroy()
        
    def clickabout(self):
        call(["python", "About.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()