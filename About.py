import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


class AboutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ABOUT")
        self.geometry("900x700+300+50")
        self.configure(bg="gray")
        self.resizable(0, 0)
        WIDTH, HEIGHT = 900, 700
        # ============================================================Frames============================================

        self.MFrame = LabelFrame(self, width=900, height=700, font=('arial', 15, 'bold'), bg='lightblue', bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=5, pady=5)
        # Add image on a Label.
        self.img = ImageTk.PhotoImage(
            Image.open("images\sale.jpg").resize((WIDTH, HEIGHT),))
        self.lbl = tk.Label(self.MFrame, image=self.img,)
        self.lbl.img = self.img
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.


if __name__ == "__main__":
    abapp = AboutApp()
    abapp.mainloop()