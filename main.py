import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from PIL import Image
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db
from subprocess import call
from dashboard import AdsucApp
import turtle

# ....................................... STTARTING PAGE................................
s = turtle.Screen()
s.setup(900, 700)
image_path = "bg.png"
image = Image.open(image_path)
resized_image = image.resize((900, 700))
temp_image_path = "bg.png"
resized_image.save(temp_image_path)

s.bgpic(temp_image_path)
t = turtle.Turtle()
t.color("yellow")
t.penup()
t.goto(-5, 85)
t.pendown()
t.write("Welcome", align="center", font=("arial", 49, "bold"))

t.penup()
t.goto(-5, 5)
t.pendown()
t.write("To", align="center", font=("arial", 49, "bold"))

t.penup()
t.goto(-10, -70)
t.pendown()
t.color("orangered")
t.write("Secrets In the Shadow", align="center", font=("arial", 49, "bold"))

t.penup()
t.goto(-190, -125)
t.pendown()
t.write("Please ....... Tap on Screen !!!!", font=("arial", 19))

t.penup()
t.goto(-30, -175)
t.pendown()
t.write("&", font=("arial", 19))

t.penup()
t.goto(-65, -230)
t.pendown()
t.color("yellow")
t.write("Sign In", font=("arial", 21))

t.hideturtle()
turtle.exitonclick()

SplashApp = tk.Tk()
SplashApp.title("LOGIN SYSTEM")
SplashApp.geometry("900x700+300+50")
SplashApp.resizable(0, 0)
SplashApp.configure(bg="black")
WIDTH, HEIGHT = 900, 700
img = ImageTk.PhotoImage(
    Image.open("images\sale.jpg").resize((WIDTH, HEIGHT))
)
lbl = tk.Label(SplashApp, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, anchor="center")


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN SYSTEM")
        self.resizable(0, 0)
        img = ImageTk.PhotoImage(
            Image.open("bg.jpeg").resize((900, 700))
        )
        lbl = tk.Label(self, width=900, height=700, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5, width=900, height=800, anchor="center")
        self.geometry("%dx%d+%d+%d" % (900, 700, 300, 50))

        fastname = tk.StringVar()
        password = tk.StringVar()

        self.MFrame = LabelFrame(
            self,
            width=100,
            height=500,
            font=("arial", 15, "bold"),
            bg="orange",
            bd=15,
            relief="ridge",
        )
        self.MFrame.grid(row=1, column=0, padx=200, pady=50)
        self.EFrame = LabelFrame(
            self,
            width=100,
            height=500,
            font=("arial", 10, "bold"),
            bg="orange",
            relief="ridge",
            bd=13,
        )
        self.EFrame.grid(row=2, column=0, pady=10)

        self.Lsyslogin = Label(
            self.MFrame,
            text="SYSTEM LOGIN:",
            font=("arial", 15, "bold"),
            height=5,
            bg="orange",
        )
        self.Lsyslogin.grid(row=1, column=0, sticky=W, padx=20)
        self.LUsername = Label(
            self.MFrame, text="___Username___:", font=("arial", 15, "bold"), bg="orange"
        )
        self.LUsername.grid(row=2, column=0, sticky=W, padx=20)
        self.Lupass = Label(
            self.MFrame, text="___Password___:", font=("arial", 15, "bold"), bg="orange"
        )
        self.Lupass.grid(row=3, column=0, sticky=W, padx=20)

        self.Txtfastname = Entry(
            self.MFrame, font=("arial", 10, "bold"), width=35, textvariable=fastname
        )
        self.Txtfastname.grid(
            row=2,
            column=1,
            padx=30,
            pady=7,
        )
        self.Txtupass = Entry(
            self.MFrame,
            font=("arial", 10, "bold"),
            width=35,
            show="*",
            textvariable=password,
        )
        self.Txtupass.grid(row=3, column=1, padx=30, pady=7)

        def on_enter(event):
            self.btnlogin.config(bg="#03fcca")

        def on_leave(event):
            self.btnlogin.config(bg="#3f256e")

        self.btnlogin = Button(
            self.EFrame,
            text="LOGIN",
            bg="#3f96d9",
            font=("arial", 10, "bold"),
            width=9,
            command=self.adlogn,
        )
        self.btnlogin.grid(row=0, column=0, padx=10, pady=10)
        self.btnlogin.bind("<Enter>", on_enter)
        self.btnlogin.bind("<Leave>", on_leave)

        def on_enter(event):
            self.btnExit.config(bg="#03fcca")

        def on_leave(event):
            self.btnExit.config(bg="#3f256e")

        self.btnExit = Button(
            self.EFrame,
            text="EXIT",
            bg="#3f96d9",
            font=("arial", 10, "bold"),
            width=9,
            command=self.exitt,
        )
        self.btnExit.grid(row=0, column=1, padx=10, pady=10)
        self.btnExit.bind("<Enter>", on_enter)
        self.btnExit.bind("<Leave>", on_leave)

        def on_enter(event):
            self.btnAbout.config(bg="#03fcca")

        def on_leave(event):
            self.btnAbout.config(bg="#3f256e")

        self.btnAbout = Button(
            self.EFrame,
            text="ABOUT",
            bg="#3f96d9",
            font=("arial", 10, "bold"),
            width=9,
            command=self.clickabout,
        )
        self.btnAbout.grid(row=0, column=2, padx=10, pady=10)
        self.btnAbout.bind("<Enter>", on_enter)
        self.btnAbout.bind("<Leave>", on_leave)

        def on_enter(event):
            self.btnReg.config(bg="#03fcca")

        def on_leave(event):
            self.btnReg.config(bg="#3f256e")

        self.btnReg = Button(
            self.EFrame,
            text="REGISTER",
            bg="#3f96d9",
            font=("arial", 10, "bold"),
            width=9,
            command=self.clickreg,
        )
        self.btnReg.grid(row=1, column=1, padx=10, pady=10)
        self.btnReg.bind("<Enter>", on_enter)
        self.btnReg.bind("<Leave>", on_leave)

    def exitt(self):
        result = mBox.askquestion(
            self, "Are you sure you want to exit?", icon="warning"
        )
        if result == "yes":
            self.destroy()

    def clickabout(self):
        call(["python", "About.py"])

    def clickreg(self):
        call(["python", "Register.py"])

    def adlogn(self):
        fastname = self.Txtfastname.get()
        password = self.Txtupass.get()
        if fastname == "" or password == "":
            mBox.showerror(self, "Error Enter username & password")
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute(
                    "select * from admin where fastname=%s and password=%s",
                    (fastname, password),
                )
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo("Information", "Login Successfully")
                    self.destroy()
                    AdsucApp()
                else:
                    mBox.showinfo(
                        "Information",
                        "Login failed,Invalid Username or Password.Try again!!!",
                    )
                cursor.close()
                conn.close()
            except Exception as es:
                print("Error", f"due to :{str(es)}")


def callmainroot():
    SplashApp.destroy()
    LoginApp()


SplashApp.after(2000, callmainroot)
mainloop()
