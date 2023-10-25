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

        # ============================================================Frames============================================
        self.EFrame = LabelFrame(self, width=500, height=200, font=('arial', 10, 'bold'), bg='orange',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=0, column=0,padx=28, pady=100)

        self.btnExit = Button(self.EFrame, text='Histogram',bg="#ffffff", font=('arial', 20, 'bold'), width=35, command=self.exitt)
        self.btnExit.grid(row=0, column=0, padx=10, pady=20)
        
        self.EFrame = LabelFrame(self, width=500, height=500, font=('arial', 10, 'bold'), bg='yellow',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0,padx=30, pady=20)
        
        def on_enter(event):
            self.btnExit.config(bg='#03fcca')
        def on_leave(event):
            self.btnExit.config(bg='orangered')
        self.btnExit = Button(self.EFrame, text='EXIT',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.exitt)
        self.btnExit.grid(row=2, column=1, padx=10, pady=10)
        self.btnExit.bind("<Enter>", on_enter)
        self.btnExit.bind("<Leave>", on_leave)
        
        

        def on_enter(event):
            self.hist_img.config(bg='#03fcca')
        def on_leave(event):
            self.hist_img.config(bg='#3f256e')
        self.hist_img = Button(self.EFrame, text='Image',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.hist_img)
        self.hist_img.grid(row=1, column=2, padx=10, pady=10)
        self.hist_img.bind("<Enter>", on_enter)
        self.hist_img.bind("<Leave>", on_leave)

        def on_enter(event):
            self.hist_aud.config(bg='#03fcca')
        def on_leave(event):
            self.hist_aud.config(bg='#3f256e')
        self.hist_aud = Button(self.EFrame, text='Audio',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.hist_aud)
        self.hist_aud.grid(row=1, column=0, padx=10, pady=10)
        self.hist_aud.bind("<Enter>", on_enter)
        self.hist_aud.bind("<Leave>", on_leave)


        def on_enter(event):
            self.hist_com.config(bg='#03fcca')
        def on_leave(event):
            self.hist_com.config(bg='#3f256e')
        self.hist_com = Button(self.EFrame, text='commpare',bg="#3f96d9", font=('arial', 10, 'bold'),fg="white", width=30,height=2, command=self.hist_com)
        self.hist_com.grid(row=1, column=1, padx=10, pady=10)
        self.hist_com.bind("<Enter>", on_enter)
        self.hist_com.bind("<Leave>", on_leave)




    def hist_img(self):
        call(["python", "histogram/histo_gen_img.py"])

    def hist_aud(self):
        call(["python", "histogram/histo_gen_aud.py"])

    def exitt(self):
        self.destroy()

    def hist_com(self):
        call(["python", "histogram/histo_com.py"])


if __name__ == "__main__":
   adapp = AdsucApp()
   adapp.mainloop()