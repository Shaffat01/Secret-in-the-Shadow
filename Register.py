import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db

class RegApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SIGN UP ")
        self.resizable(0, 0)
        img = ImageTk.PhotoImage(Image.open("bg.jpeg").resize((900, 700),))
        lbl = tk.Label(self,width=900,height=700, image=img)
        lbl.img = img
        lbl.place(relx=0.5, rely=0.5,width=900,height=800, anchor='center')
        self.geometry("%dx%d+%d+%d" % (900, 700, 300, 50))

        # ====================Variables========================#

        fastname = tk.StringVar()
        password = tk.StringVar()

        # ============================================================Frames============================================
        self.MFrame = LabelFrame(self, width=100, height=500, font=('arial', 15, 'bold'), bg='orange', bd=15,
                                 relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=300, pady=60)
        self.EFrame = LabelFrame(self, width=200, height=500, font=('arial', 10, 'bold'), bg='#73738c',
                                 relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels================================================
        self.Lsyslogin = Label(self.MFrame, text='SIGN UP:', font=('arial', 20, 'bold'), bg='orange')
        self.Lsyslogin.grid(row=1, column=0, sticky=W, padx=20)
        self.fastname = Label(self.MFrame, text='First_Name:', font=('arial', 15, 'bold'), bg='orange')
        self.fastname.grid(row=2, column=0, sticky=W, padx=20,pady=10)
        self.lastname = Label(self.MFrame, text='Last_Name:', font=('arial', 15, 'bold'), bg='orange')
        self.lastname.grid(row=3, column=0, sticky=W, padx=20,pady=10)
        self.password = Label(self.MFrame, text='Password:', font=('arial', 15, 'bold'), bg='orange')
        self.password.grid(row=4, column=0, sticky=W, padx=20,pady=10)
        self.mobile = Label(self.MFrame, text='Mobile_NO:', font=('arial', 15, 'bold'), bg='orange')
        self.mobile.grid(row=5, column=0, sticky=W, padx=20,pady=10)
        self.city = Label(self.MFrame, text='Your_city:', font=('arial', 15, 'bold'), bg='orange')
        self.city.grid(row=6, column=0, sticky=W, padx=20,pady=10)

        # ========================================================Entries of Frame======================================

        self.Txtfastname = Entry(self.MFrame, font=('arial', 10, 'bold'), textvariable=fastname)
        self.Txtfastname.grid(row=2, column=1, padx=10, pady=5)
        self.Txtlastname = Entry(self.MFrame, font=('arial', 10, 'bold'))
        self.Txtlastname.grid(row=3, column=1, padx=10, pady=5)
        self.Txtupass = Entry(self.MFrame, font=('arial', 10, 'bold') ,show="*", textvariable=password)
        self.Txtupass.grid(row=4, column=1, padx=10, pady=5)
        self.Txtmobile = Entry(self.MFrame, font=('arial', 10, 'bold')  )
        self.Txtmobile.grid(row=5, column=1, padx=10, pady=5)
        self.Txtcity = Entry(self.MFrame, font=('arial', 10, 'bold') )
        self.Txtcity.grid(row=6, column=1, padx=10, pady=5)


        # ========================================================Buttons of EFrame=====================================
        self.btnlogin = Button(self.EFrame, text='SIGN UP',bg="orange",font=('arial', 15, 'bold'), width=9, command=self.savst)
        self.btnlogin.grid(row=0, column=0, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='RESET',bg="orange", font=('arial', 15, 'bold'), width=9, command=self.allclear)
        self.btnExit.grid(row=0, column=1, padx=10, pady=10)

        self.btnAbout = Button(self.EFrame, text='EXIT',bg="orange", font=('arial', 15, 'bold'), width=9, command=self.exitt)
        self.btnAbout.grid(row=0, column=2, padx=10, pady=10)


        # ========================================================functions=================================================
        # ==========Exit Function==========

    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    def allclear(self):
        self.Txtfastname.delete(0, END)
        self.Txtupass.delete(0, END)

    def savst(self):
        fastname = self.Txtfastname.get()
        password = self.Txtupass.get()
        lastname=self.Txtlastname.get()
        mobile = self.Txtmobile.get()
        city = self.Txtcity.get()


        if fastname == ""or password == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from admin where fastname=%s", fastname)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "username. already used")
                else:
                    cursor.execute("Insert into admin( fastname,lastname,password,city,mobile)" "values(%s,%s,%s,%s,%s)", (fastname,lastname,password,city,mobile))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "Successfully Registered,Login")
                        self.destroy()
                    else:
                        mBox.showerror("Error", "Unable to Register")
                    cursor.close()
                    conn.close()
            except Exception as es:
                print('Error', f"due to :{str(es)}")

if __name__ == "__main__":
    regpapp = RegApp()
    regpapp.mainloop()

