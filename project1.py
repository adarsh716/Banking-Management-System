from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


f20=None
#----------------------------------user-------------------------------------#
class login:
    def __init__(self):
        f0=Frame(bg="#fff")
        f0.place(x=0,y=0,width=1500,height=988)
        self.l2=Label(f0,text="",font=("arial",20),fg="black",bg="lightgrey")
        self.l2.place(relx=0.02,rely=0.1,width=2000,height=300)
        self.l0=Label(f0,text="Welcome to our ",font=("arial",25),fg="black",bg="lightgrey")
        self.l0.place(relx=0.42,rely=0.18)
        self.l1=Label(f0,text="Banking Management System ",font=("arial black",40),fg="royalblue",bg="lightgrey")
        self.l1.place(relx=0.23,rely=0.23)
        self.l3=Label(f0,text="CHOOSE AN ACTION",font=("arial",25),fg="black",bg="#fff")
        self.l3.place(relx=0.38,rely=0.45)
        self.b3=Button(f0,text="ADMIN",bg="royalblue",fg="white",width=20,height=2,command=admin)
        self.b3.place(relx=0.45,rely=0.55)
        self.b4=Button(f0,text="USER",bg="royalblue",fg="white",width=20,height=2,command=self.custlog)
        self.b4.place(relx=0.45,rely=0.65)
      


    def custlog(self):
        self.an=StringVar()
        self.pi=StringVar()
        f1=Frame(bg="#fff")
        f1.place(x=0,y=0,width=1500,height=988)
        Label(f1,image=img,border=0,bg='white').place(x=50,y=90)
        self.a1=Label(f1,text="LOGIN",font=("algerian",40),fg="royalblue",bg="#fff")
        self.a1.place(relx=0.7,rely=0.1)
        self.l1=Label(f1,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
        self.l1.place(relx=0.6,rely=0.25)
        self.e1=Entry(f1,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.an)
        self.e1.place(relx=0.6,rely=0.3,width=500)
        self.c=Canvas(f1,width=500,height=2,bg="black",highlightthickness=0)
        self.c.place(relx=0.6,rely=0.33)
        self.l2=Label(f1,text="PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l2.place(relx=0.6,rely=0.4)
        self.e2=Entry(f1,font=("arial",15),show="*",highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e2.place(relx=0.6,rely=0.45,width=500)
        self.c1=Canvas(f1,width=500,height=2,bg="black",highlightthickness=0)
        self.c1.place(relx=0.6,rely=0.48)
        def home1():
            db=sqlite3.connect("back.db")
            cr=db.cursor()
            cr.execute("select * from account where acno='"+self.an.get()+"' and pin='"+self.pi.get()+"'")
            result = cr.fetchall()

            if len(result) == 0:
                db.close()
                messagebox.showerror("", "Invalid Account Number/PIN")

            else:
                db.commit()
                db.close()
                log(result[0])
            self.an.set("")
            self.pi.set("")
        self.b1=Button(f1,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=home1)
        self.b1.place(relx=0.6,rely=0.5)
        self.b2=Button(f1,text="Forgot PIN",bg="red",fg="white",width=20,height=2,command=self.forget)
        self.b2.place(relx=0.75,rely=0.5)
        self.l3=Label(f1,text="(No account?)",font=("arial",15),bg="#fff",fg="royalblue")
        self.l3.place(relx=0.65,rely=0.61)
        self.b3=Button(f1,text="Create Account",bg="green",fg="white",width=20,height=2,command=self.create)
        self.b3.place(relx=0.75,rely=0.6)


    def create(self):
        f=Frame(bg="#fff")
        f.place(x=800,y=0,width=800,height=988)
        self.ac=StringVar()
        self.n=StringVar()
        self.add=StringVar()
        self.pn=StringVar()
        self.g=StringVar()
        self.e=StringVar()
        self.p=StringVar()
        self.b=StringVar()
        self.p1=StringVar()
        self.a2=Label(f,text="Create account",font=("algerian",40),fg="royalblue",bg="#fff")
        self.a2.place(relx=0.1,rely=0.03)
        self.l4=Label(f,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
        self.l4.place(relx=0.05,rely=0.1)
        def genacno():
            f19=Frame(bg="#fff")
            f19.place(relx=0.88,rely=0.11,width=150,height=200)
            db=sqlite3.connect("back.db")
            cr=db.cursor()
            r=cr.execute("select acno+1 from account order by acno desc limit 1")
            for r1 in r:
                self.e3=Entry(f,font=("",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.ac)
                self.e3.insert(0,r1[0])
                self.e3.place(relx=0.05,rely=0.13,width=500)
            db.commit()
            db.close()
        self.b1=Button(f,text="Generate ac.no",bg="royalblue",fg="white",width=15,height=2,command=genacno)
        self.b1.place(relx=0.7,rely=0.11)
        self.c2=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c2.place(relx=0.05,rely=0.16)
        self.l5=Label(f,text="Name",font=("arial",15),bg="#fff",fg="royalblue")
        self.l5.place(relx=0.05,rely=0.18)
        self.e4=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.n)
        self.e4.place(relx=0.05,rely=0.21,width=500)
        self.c3=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.05,rely=0.24)
        self.l6=Label(f,text="Address",font=("arial",15),bg="#fff",fg="royalblue")
        self.l6.place(relx=0.05,rely=0.26)
        self.e5=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.add)
        self.e5.place(relx=0.05,rely=0.29,width=500)
        self.c4=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c4.place(relx=0.05,rely=0.32)
        self.l7=Label(f,text="Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
        self.l7.place(relx=0.05,rely=0.34)
        self.e6=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pn)
        self.e6.place(relx=0.05,rely=0.37,width=500)
        self.c5=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c5.place(relx=0.05,rely=0.4)
        self.l8=Label(f,text="Gender",font=("arial",15),bg="#fff",fg="royalblue")
        self.l8.place(relx=0.05,rely=0.42)
        self.e7=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.g)
        self.e7.place(relx=0.05,rely=0.45,width=500)
        self.c6=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c6.place(relx=0.05,rely=0.48)
        self.l9=Label(f,text="Email",font=("arial",15),bg="#fff",fg="royalblue")
        self.l9.place(relx=0.05,rely=0.5)
        self.e8=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.e)
        self.e8.place(relx=0.05,rely=0.53,width=500)
        self.c7=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c7.place(relx=0.05,rely=0.56)
        self.l10=Label(f,text="Set PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l10.place(relx=0.05,rely=0.58)
        self.e9=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.p)
        self.e9.place(relx=0.05,rely=0.61,width=500)
        self.c8=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c8.place(relx=0.05,rely=0.64)
        self.l11=Label(f,text="Enter amount you want to deposit",font=("arial",15),bg="#fff",fg="royalblue")
        self.l11.place(relx=0.05,rely=0.66)
        self.e10=Entry(f,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.p1)
        self.e10.place(relx=0.05,rely=0.69,width=500)
        self.c9=Canvas(f,width=500,height=2,bg="black",highlightthickness=0)
        self.c9.place(relx=0.05,rely=0.72)
        def create1():
            self.name = self.e4.get().title()
            self.email = self.e8.get().upper()
            self.mobile = self.e6.get()
            self.pin = self.e9.get()
            self.gender = self.e7.get().upper()
            self.address = self.e5.get()
            self.bal=self.e10.get()
            flag = False
            for i in range(0, 10):
                if str(i) in self.name:
                    flag = True
                    break
            s = len(self.email)
            if self.name == "" or self.email == "" or self.mobile == "" or self.pin == "" or self.gender == "" or self.address=="":
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif flag:
                messagebox.showerror("", "Do Not Enter Any Number In Name Field!")
            elif '@' not in self.email or not self.email.endswith(".COM") or self.email[0] == '@' or self.email[s - 5] == '@' or self.email.count('@') > 1:
                messagebox.showerror("", 'Enter A Valid Email!')
            elif not self.mobile.isnumeric() or len(self.mobile) != 10:
                messagebox.showerror("", "Enter a Valid Mobile Number!")
            elif not self.pin.isnumeric() or len(self.pin) != 4:
                messagebox.showerror("", "Enter a Valid PIN!")
            elif len(self.pin) > 4:
                messagebox.showwarning("", "PIN greater than rage !!")
            elif int(self.bal) < 5000:
                messagebox.showerror("", "Minimum amount to be deposit is 5000!!!")
            elif len(self.name) > 20:
                messagebox.showwarning("", "Name too long")
            elif len(self.address) > 50:
                messagebox.showwarning("", "Name too long")
            elif self.gender not in ("MALE","FEMALE","OTHERS"):
                messagebox.showerror("", "Your provided Gender type isn't available")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select * from account where email='"+self.e.get()+"' or phno='"+self.pn.get()+"' or pin='"+self.p.get()+"'")
                result = cr.fetchone()
                if result is None:
                    cr=db.cursor()
                    cr.execute("insert into account values('"+self.ac.get()+"','"+self.n.get()+"','"+self.add.get()+"','"+self.pn.get()+"','"+self.g.get()+"','"+self.e.get()+"','"+self.p.get()+"','"+self.p1.get()+"')")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "Registration successfull")
                else:
                    db.close()
                    messagebox.showerror("", "An Acount With Same Email or Mobile Number or PIN Already Exist!")
            self.ac.set("")
            self.n.set("")
            self.add.set("")
            self.pn.set("")
            self.g.set("")
            self.e.set("")
            self.p.set("")
            self.p1.set("")
        self.b4=Button(f,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=create1)
        self.b4.place(relx=0.16,rely=0.77)
        self.b5=Button(f,text="Back",bg="red",fg="white",width=20,height=2,command=self.custlog)
        self.b5.place(relx=0.36,rely=0.77)


    def forget(self):
        f3=Frame(bg="#fff")
        f3.place(x=800,y=0,width=800,height=988) 
        self.ac=StringVar()
        self.pi=StringVar()
        self.pi1=StringVar()
        self.a3=Label(pr,text="Forgot PIN",font=("algerian",40),fg="royalblue",bg="#fff")
        self.a3.place(relx=0.65,rely=0.2)
        self.l12=Label(pr,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
        self.l12.place(relx=0.6,rely=0.35)
        self.e11=Entry(pr,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.ac)
        self.e11.place(relx=0.6,rely=0.4,width=500)
        self.c10=Canvas(pr,width=500,height=2,bg="black",highlightthickness=0)
        self.c10.place(relx=0.6,rely=0.43)
        self.l13=Label(pr,text="Enter New PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l13.place(relx=0.6,rely=0.48)
        self.e12=Entry(pr,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e12.place(relx=0.6,rely=0.52,width=500)
        self.c11=Canvas(pr,width=500,height=2,bg="black",highlightthickness=0)
        self.c11.place(relx=0.6,rely=0.55)
        self.l14=Label(pr,text="Confirm PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l14.place(relx=0.6,rely=0.58)
        self.e13=Entry(pr,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi1)
        self.e13.place(relx=0.6,rely=0.63,width=500)
        self.c12=Canvas(pr,width=500,height=2,bg="black",highlightthickness=0)
        self.c12.place(relx=0.6,rely=0.66)
        def forgotpin():
                self.pin=self.e12.get()
                self.pin1=self.e13.get()
                self.an=self.e11.get()
                if self.pin == "" or self.pin1 == "" or self.an=="":
                    messagebox.showerror("", "All Fields Are Mandatory!")
                elif self.pin != self.pin1:
                    messagebox.showerror("","PIN is matched to last pin!!")
                elif len(self.pin) > 4:
                    messagebox.showwarning("", "PIN greater than rage !!")
                elif not self.pin.isnumeric() or len(self.pin) != 4:
                    messagebox.showerror("", "Enter a Valid PIN!")
                elif not self.pin1.isnumeric() or len(self.pin1) != 4:
                    messagebox.showerror("", "Enter a Valid PIN!")
                else:
                    db=sqlite3.connect("back.db")
                    cr=db.cursor()
                    cr.execute("select * from account where acno='"+self.ac.get()+"'")
                    result = cr.fetchone()
                    if result is None:
                        db.close()
                        messagebox.showerror("", "Accounnt doesnt Exist!!!")
                    else:
                        cr=db.cursor()
                        cr.execute("update account set pin='"+self.pi.get()+"' where acno='"+self.ac.get()+"'")
                        db.commit()
                        db.close()
                        messagebox.showinfo(" ", "PIN changed successfully")
                self.ac.set("")
                self.pi.set("")
                self.pi1.set("")
        self.b6=Button(pr,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=forgotpin)
        self.b6.place(relx=0.6,rely=0.75)
        self.b7=Button(pr,text="Back",bg="red",fg="white",width=20,height=2,command=self.custlog)
        self.b7.place(relx=0.75,rely=0.75)

class log:
    def __init__(self,user):
        self.user=user
        self.show_main()
        

    def show_main(self):
        f4=Frame(bg="#fff")
        f4.place(x=0,y=0,width=1500,height=988)
        pi=StringVar()
        Label(f4,image=img,border=0,bg='white').place(relx=0.3,rely=0.2)
        self.l17=Label(f4,text="Welcome",font=("arial black",40),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.42,rely=0.05)
        self.b8=Button(f4,text="Show My Details",bg="royalblue",fg="white",width=30,height=2,command=self.show_details)
        self.b8.place(relx=0.05,rely=0.1)
        self.b9=Button(f4,text="Update My Details",bg="royalblue",fg="white",width=30,height=2,command=self.update_details)
        self.b9.place(relx=0.05,rely=0.3)
        self.b10=Button(f4,text="Show My Balance",bg="royalblue",fg="white",width=30,height=2,command=self.show_balance)
        self.b10.place(relx=0.05,rely=0.5)
        self.b11=Button(f4,text="Change PIN",bg="royalblue",fg="white",width=30,height=2,command=self.change_pin)
        self.b11.place(relx=0.05,rely=0.7)
        self.b12=Button(f4,text="Withdraw Money",bg="royalblue",fg="white",width=30,height=2,command=self.withd_money)
        self.b12.place(relx=0.8,rely=0.1)
        self.b13=Button(f4,text="Deposit Money",bg="royalblue",fg="white",width=30,height=2,command=self.dep_money)
        self.b13.place(relx=0.8,rely=0.3)
        self.b14=Button(f4,text="Close My account",bg="royalblue",fg="white",width=30,height=2,command=self.close1)
        self.b14.place(relx=0.8,rely=0.5)
        self.b15=Button(f4,text="Log Out",bg="red",fg="white",width=30,height=2,command=login)
        self.b15.place(relx=0.8,rely=0.7)

    def show_details(self):
        f5=Frame(bg="#fff")
        f5.place(x=0,y=0,width=1500,height=988)
        Label(f5,image=img,border=0,bg='white').place(x=50,y=90)
        self.head_l=Label(f5,text="YOUR INFORMATION",font=("algerian",40),bg="#fff",fg="royalblue")
        self.head_l.place(relx=0.6,rely=0.05)
        db=sqlite3.connect("back.db")
        cr=db.cursor()
        cr.execute("select * from account where pin='"+self.user[6]+"'")
        result=cr.fetchone()
        if result[6] is None:
            messagebox.showerror("Error","No Invoice Available")
        else:
            r=cr.execute("select * from account where pin='"+result[6]+"'")
            for r1 in r:
                l15=Label(f5,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
                l15.place(relx=0.5,rely=0.15)
                l16=Label(f5,font=(" ",15), text = r1[0],bg="#fff",fg="black")
                l16.place(relx=0.65,rely=0.15)
                l17=Label(f5,text="Name",font=("arial",15),bg="#fff",fg="royalblue")
                l17.place(relx=0.5,rely=0.2)
                l17=Label(f5,font=(" ",15), text = r1[1],bg="#fff",fg="black")
                l17.place(relx=0.65,rely=0.2)
                l18=Label(f5,text="Address",font=("arial",15),bg="#fff",fg="royalblue")
                l18.place(relx=0.5,rely=0.25)
                l18=Label(f5,font=(" ",15), text = r1[2],bg="#fff",fg="black")
                l18.place(relx=0.65,rely=0.25)        
                l19=Label(f5,text="Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
                l19.place(relx=0.5,rely=0.3)
                l19=Label(f5,font=(" ",15), text = r1[3],bg="#fff",fg="black")
                l19.place(relx=0.65,rely=0.3) 
                l20=Label(f5,text="Gender",font=("arial",15),bg="#fff",fg="royalblue")
                l20.place(relx=0.5,rely=0.35)
                l20=Label(f5,font=(" ",15), text = r1[4],bg="#fff",fg="black")
                l20.place(relx=0.65,rely=0.35)  
                l21=Label(f5,text="E-Mail",font=("arial",15),bg="#fff",fg="royalblue")
                l21.place(relx=0.5,rely=0.4)
                l21=Label(f5,font=(" ",15), text = r1[5],bg="#fff",fg="black")
                l21.place(relx=0.65,rely=0.4)  
                b17=Button(f5,text="Back to Main Menu",bg="red",fg="white",width=20,height=2,command=self.show_main)
                b17.place(relx=0.75,rely=0.5) 
                db.commit()
                db.close()     
                break

    def update_details(self):
        self.pi1=StringVar()
        f6=Frame(bg="#fff")
        f6.place(x=0,y=0,width=1500,height=988)
        Label(f6,image=img,border=0,bg='white').place(x=50,y=90)
        self.l17=Label(f6,text="Enter Your PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.5,rely=0.05)
        self.e14=Entry(f6,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi1)
        self.e14.place(relx=0.6,rely=0.05,width=300)
        self.c13=Canvas(f6,width=300,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.08)
        self.n1=StringVar()
        self.ad1=StringVar()
        self.pn1=StringVar()
        self.em1=StringVar()
        self.l34=Label(f6,text="Enter Your New Details",font=("arial",15),bg="#fff",fg="royalblue")
        self.l34.place(relx=0.5,rely=0.2)
        self.l35=Label(f6,text="Enter Name",font=("arial",15),bg="#fff",fg="royalblue")
        self.l35.place(relx=0.5,rely=0.25)
        self.e4=Entry(f6,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.n1)
        self.e4.place(relx=0.65,rely=0.25,width=300)
        self.c3=Canvas(f6,width=300,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.65,rely=0.28)
        self.l36=Label(f6,text="Enter Address",font=("arial",15),bg="#fff",fg="royalblue")
        self.l36.place(relx=0.5,rely=0.31)
        self.e5=Entry(f6,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.ad1)
        self.e5.place(relx=0.65,rely=0.31,width=300)
        self.c3=Canvas(f6,width=300,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.65,rely=0.34)
        self.l37=Label(f6,text="Enter Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
        self.l37.place(relx=0.5,rely=0.37)
        self.e6=Entry(f6,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pn1)
        self.e6.place(relx=0.65,rely=0.37,width=300)
        self.c3=Canvas(f6,width=300,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.65,rely=0.4)
        self.l38=Label(f6,text="Enter E-mail",font=("arial",15),bg="#fff",fg="royalblue")
        self.l38.place(relx=0.5,rely=0.43)
        self.e8=Entry(f6,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.em1)
        self.e8.place(relx=0.65,rely=0.43,width=300)
        self.c3=Canvas(f6,width=300,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.65,rely=0.46)
        def ud1():
            self.name = self.e4.get().title()
            self.email = self.e8.get().upper()
            self.mobile = self.e6.get()
            self.address = self.e5.get()
            self.pin= self.e14.get()
            flag = False
            for i in range(0, 10):
                if str(i) in self.name:
                    flag = True
                    break
            s = len(self.email)
            if self.name == "" or self.email == "" or self.mobile == "" or self.address=="":
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif self.user[6]!=self.pin:
                messagebox.showerror("", "Wrong Pin")
            elif flag:
                messagebox.showerror("", "Do Not Enter Any Number In Name Field!")
            elif '@' not in self.email or not self.email.endswith(".COM") or self.email[0] == '@' or self.email[s - 5] == '@' or self.email.count('@') > 1:
                messagebox.showerror("", 'Enter A Valid Email!')
            elif not self.mobile.isnumeric() or len(self.mobile) != 10:
                messagebox.showerror("", "Enter a Valid Mobile Number!")
            elif len(self.name) > 20:
                messagebox.showwarning("", "Name too long")
            elif len(self.address) > 50:
                messagebox.showwarning("", "Name too long")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select * from account where email='"+self.em1.get()+"' or phno='"+self.pn1.get()+"'")
                result = cr.fetchone()
                if result is None:
                    cr=db.cursor()
                    cr.execute("UPDATE account SET name='"+self.n1.get()+"',address='"+self.ad1.get()+"',phno='"+self.pn1.get()+"',email='"+self.em1.get()+"' where pin='"+self.pi1.get()+"'")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "Information Updated Succesfully")
                else:
                    db.close()
                    messagebox.showerror("", "An Acount With Same Email or Mobile Number Already Exist!")
            self.n1.set("")
            self.ad1.set("")
            self.pn1.set("")
            self.em1.set("")
            self.pi1.set("")
        self.b18=Button(f6,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=ud1)
        self.b18.place(relx=0.55,rely=0.6)     
        self.b19=Button(f6,text="Back to Main Menu",bg="red",fg="white",width=20,height=2,command=self.show_main)
        self.b19.place(relx=0.75,rely=0.6)                
        

    def show_balance(self):
        self.pi=StringVar()
        f7=Frame(bg="#fff")
        f7.place(x=0,y=0,width=1500,height=988)
        Label(f7,image=img,border=0,bg='white').place(x=50,y=90)    
        self.l17=Label(f7,text="Enter Your PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.5,rely=0.05)
        self.e14=Entry(f7,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e14.place(relx=0.6,rely=0.05,width=300)
        self.c13=Canvas(f7,width=300,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.08)
        def sb():
            self.pin=self.e14.get()
            db=sqlite3.connect("back.db")
            cr=db.cursor()
            if self.user[6]!=self.pin:
                messagebox.showerror("", "Wrong Pin")
            else:
                r=cr.execute("select * from account where pin='"+self.pi.get()+"'")
                for r1 in r:
                    l26=Label(f7,font=(" ",20), text = 'Welcome '+r1[1],bg="#fff",fg="royalblue")
                    l26.place(relx=0.5,rely=0.2)            
                    l25=Label(f7,text="Your account Balace",font=("arial",15),bg="#fff",fg="royalblue")
                    l25.place(relx=0.5,rely=0.3)
                    l26=Label(f7,font=(" ",15), text = r1[7],bg="#fff",fg="black")
                    l26.place(relx=0.65,rely=0.3) 
                    break 
                else:
                    messagebox.showerror("","Invalid PIN!")   
            db.commit()
            db.close()
            self.pi.set("")
        self.b16=Button(f7,text="Submit",bg="royalblue",fg="white",width=15,height=2,command=sb)
        self.b16.place(relx=0.85,rely=0.03)  
        self.b19=Button(f7,text="Back to Main Menu",bg="red",fg="white",width=20,height=2,command=self.show_main)
        self.b19.place(relx=0.75,rely=0.6)     


    def change_pin(self):
        self.pn1=StringVar()
        self.pi1=StringVar()
        f8=Frame(bg="#fff")
        f8.place(x=0,y=0,width=1500,height=988)
        Label(f8,image=img,border=0,bg='white').place(x=50,y=90)
        self.l17=Label(f8,text="Enter Your Phone Number",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.5,rely=0.05)
        self.e14=Entry(f8,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pn1)
        self.e14.place(relx=0.5,rely=0.1,width=400)
        self.c13=Canvas(f8,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.5,rely=0.13)
        self.l17=Label(f8,text="Enter Your PIN",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.5,rely=0.2)
        self.e15=Entry(f8,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi1)
        self.e15.place(relx=0.5,rely=0.25,width=400)
        self.c13=Canvas(f8,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.5,rely=0.28)
        self.pi2=StringVar()
        self.l17=Label(f8,text="Enter Your New PIN",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.5,rely=0.35)
        self.e16=Entry(f8,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi2)
        self.e16.place(relx=0.5,rely=0.4,width=400)
        self.c13=Canvas(f8,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.5,rely=0.43)
        def cp2():
            self.pin=self.e15.get()
            self.pin1=self.e16.get()
            self.pn=self.e14.get()
            if self.pin == "" or self.pin1 == "" or self.pn=="":
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif self.user[6]!=self.pin:
                messagebox.showerror("", "Wrong Pin")
            elif self.pin == self.pin1:
                messagebox.showerror("","You Entered the same pervious PIN")
            elif len(self.pin) > 4:
                messagebox.showwarning("", "PIN greater than rage !!")
            elif len(self.pin) > 4:
                messagebox.showwarning("", "PIN greater than rage !!")
            elif not self.pin.isnumeric() or len(self.pin) != 4:
                messagebox.showerror("", "Enter a Valid PIN!")
            elif not self.pin1.isnumeric() or len(self.pin1) != 4:
                messagebox.showerror("", "Enter a Valid PIN!")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select * from account where pin='"+self.pi.get()+"'")
                result = cr.fetchone()

                if result is None:
                    cr=db.cursor()
                    cr.execute("UPDATE account SET pin='"+self.pi2.get()+"' where phno='"+self.pn1.get()+"'and pin='"+self.pi1.get()+"'")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "PIN changed successfully")
                else:
                    db.close()
                    messagebox.showerror("", "An Acount With Same PIN Already Exist please choose another pin!")
            self.pi2.set("")   
            self.pi1.set("")
            self.pn1.set("")
        self.b16=Button(f8,text="Submit",bg="royalblue",fg="white",width=15,height=2,command=cp2)
        self.b16.place(relx=0.5,rely=0.5)
        self.b17=Button(f8,text="Back",bg="red",fg="white",width=15,height=2,command=self.show_main)
        self.b17.place(relx=0.65,rely=0.5)    


    def withd_money(self):
        self.pi=StringVar()
        f9=Frame(bg="#fff")
        f9.place(x=0,y=0,width=1500,height=988)
        Label(f9,image=img,border=0,bg='white').place(x=50,y=90)
        self.l17=Label(f9,text="Enter Your PIN",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.6,rely=0.2)
        self.e14=Entry(f9,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e14.place(relx=0.6,rely=0.27,width=400)
        self.c13=Canvas(f9,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.3)
        self.wm=StringVar()
        self.l17=Label(f9,text="Enter Amount you want to withdraw ",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.6,rely=0.35)
        self.e15=Entry(f9,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.wm)
        self.e15.place(relx=0.6,rely=0.42,width=400)
        self.c13=Canvas(f9,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.45)
        def widm():
                self.wamt=self.e15.get()
                self.pin=self.e14.get()
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select balance from account where pin='"+self.user[6]+"' ")
                bal=cr.fetchone()
                db.commit()
                db.close()
                print(bal)
                if self.pin == "" or self.wamt == "":
                    messagebox.showerror("", "All Fields Are Mandatory!")
                elif int(int(self.user[7])-int(self.wamt)) <= 1000 :
                    messagebox.showerror("", "Minimum Balance should be 1000!")
                elif self.user[6]!=self.pin:
                    messagebox.showerror("", "Wrong Pin")
                elif int(self.wamt) > 5000:
                    messagebox.showerror("", "Maximum amount of withdraw is 5000!!!")
                elif int(self.wamt) < 500:
                    messagebox.showerror("", "Minimum amount of withdraw is 500!!!")
                else:
                    db=sqlite3.connect("back.db")
                    cr=db.cursor()
                    r=cr.execute("UPDATE account SET balance=balance-'"+self.wm.get()+"' where pin='"+self.pi.get()+"'")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "Money Withdraw successfully!!")
                self.wm.set("")         
                self.pi.set("")
        self.b16=Button(f9,text="Submit",bg="royalblue",fg="white",width=15,height=2,command=widm)
        self.b16.place(relx=0.6,rely=0.55)  
        self.b20=Button(f9,text="Back",bg="red",fg="white",width=15,height=2,command=self.show_main)
        self.b20.place(relx=0.7,rely=0.55)  

    def dep_money(self):
        f10=Frame(bg="#fff")
        self.pi=StringVar()
        f10.place(x=0,y=0,width=1500,height=988)
        Label(f10,image=img,border=0,bg='white').place(x=50,y=90) 
        self.l17=Label(f10,text="Enter Your PIN",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.6,rely=0.2)
        self.e14=Entry(f10,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e14.place(relx=0.6,rely=0.27,width=400)
        self.c13=Canvas(f10,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.3)
        self.dm=StringVar()
        self.l17=Label(f10,text="Enter Amount you want to deposit ",font=("arial",18),bg="#fff",fg="royalblue")
        self.l17.place(relx=0.6,rely=0.35)
        self.e15=Entry(f10,font=("arial",18),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.dm)
        self.e15.place(relx=0.6,rely=0.42,width=400)
        self.c13=Canvas(f10,width=400,height=2,bg="black",highlightthickness=0)
        self.c13.place(relx=0.6,rely=0.45)
        def dm():
            self.wamt=self.e15.get()
            self.pin=self.e14.get()
            if self.pin == "" or self.wamt == "":
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif self.user[6]!=self.pin:
                messagebox.showerror("", "Wrong Pin")
            elif int(self.wamt) < 500:
                messagebox.showerror("", "Minimum amount of deposit is 500!!!")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("UPDATE account SET balance=balance+'"+self.dm.get()+"' where pin='"+self.pi.get()+"'")
                db.commit()
                db.close()
                messagebox.showinfo(" ", "Money Deposit successfully!!")
            self.dm.set("")         
            self.pi.set("")
        self.b16=Button(f10,text="Submit",bg="royalblue",fg="white",width=15,height=2,command=dm)
        self.b16.place(relx=0.6,rely=0.55)  
        self.b16=Button(f10,text="Back",bg="red",fg="white",width=15,height=2,command=self.show_main)
        self.b16.place(relx=0.7,rely=0.55)  


    def close1(self):
        f11=Frame(bg="#fff")
        f11.place(x=0,y=0,width=1500,height=988)
        self.pi=StringVar()
        Label(f11,image=img,border=0,bg='white').place(x=50,y=90)
        self.l4=Label(f11,text="Enter Your PIN",font=("arial",15),bg="#fff",fg="royalblue")
        self.l4.place(relx=0.5,rely=0.25)
        self.e4=Entry(f11,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=self.pi)
        self.e4.place(relx=0.5,rely=0.3,width=300)
        self.c3=Canvas(f11,width=400,height=2,bg="black",highlightthickness=0)
        self.c3.place(relx=0.5,rely=0.33)
        def delete():
            self.pin=self.e4.get()
            if self.pin == "" :
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif self.user[6]!=self.pin:
                messagebox.showerror("", "Wrong Pin")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                r=cr.execute("delete from account where pin='"+self.pi.get()+"' ")
                db.commit()
                db.close()
                messagebox.showerror('Delete','Account Deleted Successfully')
                login()
            self.pi.set("")
        self.b4=Button(f11,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=delete)
        self.b4.place(relx=0.6,rely=0.4)
        self.b16=Button(f11,text="Back",bg="red",fg="white",width=15,height=2,command=self.show_main)
        self.b16.place(relx=0.75,rely=0.4)  

  #------------------------------------------------Admin---------------------------------------------------------# 

def admin():
    f12=Frame(bg="#fff")
    f12.place(x=0,y=0,width=1500,height=988)
    '''engine=pyttsx3.init()
    engine.setProperty('rate',135)
    engine.say("Welcome to admin login")
    engine.runAndWait()'''
    pi1=StringVar()
    Label(f12,image=img,border=0,bg='white').place(relx=0.5,rely=0.05)
    admin_label=Label(f12,text="ADMIN LOGIN",font=("algerian",40),fg="royalblue",bg="#fff")
    admin_label.place(relx=0.15,rely=0.1)
    l2=Label(f12,text="Enter Password",font=("arial",15),bg="#fff",fg="royalblue")
    l2.place(relx=0.1,rely=0.3)
    e2=Entry(f12,font=("arial",15),show="*",highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=pi1)
    e2.place(relx=0.1,rely=0.35,width=500)
    c1=Canvas(f12,width=500,height=2,bg="black",highlightthickness=0)
    c1.place(relx=0.1,rely=0.38)
    def checkadmin():
        db=sqlite3.connect("back.db")
        cr=db.cursor()
        r=cr.execute("select * from admin where password='"+pi1.get()+"'")
        for r1 in r:
            adminmain() 
            '''engine=pyttsx3.init()
            engine.setProperty('rate',135)
            engine.say("login successfully")
            engine.runAndWait()'''
            break
        else:
            messagebox.showerror('Wrong Password','Please enter correct password')
            '''engine=pyttsx3.init()
            engine.setProperty('rate',135)
            engine.say("Please enter correct password")
            engine.runAndWait()'''
        db.commit()
        db.close()
        pi1.set("")
    b1=Button(f12,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=checkadmin)
    b1.place(relx=0.12,rely=0.45)
    b5=Button(f12,text="Back",bg="red",fg="white",width=20,height=2,command=login)
    b5.place(relx=0.28,rely=0.45)

def adminmain():
    m=ttk.Notebook()
    m.place(x=0,y=0,width=1500,height=1000)
    create_by_admin(m)
    view(m)
    searchadmin(m)
    update_by_admin(m)
    delete_by_admin(m)
    logout_admin(m)


def create_by_admin(m):
        f13=Frame(bg="#fff")
        m.add(f13,text="  Create  Account          ")
        ac=StringVar()
        n=StringVar()
        add=StringVar()
        pn=StringVar()
        g=StringVar()
        e=StringVar()
        p=StringVar()
        b=StringVar()
        a2=Label(f13,text="Create account",font=("algerian",40),fg="royalblue",bg="#fff")
        a2.place(relx=0.35,rely=0.03)
        l4=Label(f13,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
        l4.place(relx=0.05,rely=0.1)
        e4=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=ac)
        e4.place(relx=0.05,rely=0.13,width=500)
        c3=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c3.place(relx=0.05,rely=0.16)
        l5=Label(f13,text="Enter Name",font=("arial",15),bg="#fff",fg="royalblue")
        l5.place(relx=0.55,rely=0.1)
        e5=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=n)
        e5.place(relx=0.55,rely=0.13,width=500)
        c3=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c3.place(relx=0.55,rely=0.16)
        l6=Label(f13,text="Address",font=("arial",15),bg="#fff",fg="royalblue")
        l6.place(relx=0.05,rely=0.19)
        e6=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=add)
        e6.place(relx=0.05,rely=0.22,width=500)
        c4=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c4.place(relx=0.05,rely=0.25)
        l7=Label(f13,text="Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
        l7.place(relx=0.55,rely=0.18)
        e7=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=pn)
        e7.place(relx=0.55,rely=0.22,width=500)
        c5=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c5.place(relx=0.55,rely=0.25)
        l8=Label(f13,text="Gender",font=("arial",15),bg="#fff",fg="royalblue")
        l8.place(relx=0.05,rely=0.27)
        e8=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=g)
        e8.place(relx=0.05,rely=0.31,width=500)
        c6=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c6.place(relx=0.05,rely=0.34)
        l9=Label(f13,text="Email",font=("arial",15),bg="#fff",fg="royalblue")
        l9.place(relx=0.55,rely=0.27)
        e9=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=e)
        e9.place(relx=0.55,rely=0.31,width=500)
        c7=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c7.place(relx=0.55,rely=0.34)
        l10=Label(f13,text="Set PIN",font=("arial",15),bg="#fff",fg="royalblue")
        l10.place(relx=0.05,rely=0.37)
        e10=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=p)
        e10.place(relx=0.05,rely=0.41,width=500)
        c8=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c8.place(relx=0.05,rely=0.44)
        l11=Label(f13,text="Enter Amount deposit",font=("arial",15),bg="#fff",fg="royalblue")
        l11.place(relx=0.55,rely=0.37)
        e11=Entry(f13,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=b)
        e11.place(relx=0.55,rely=0.41,width=500)
        c9=Canvas(f13,width=500,height=2,bg="black",highlightthickness=0)
        c9.place(relx=0.55,rely=0.44)
        def create1():
            name = e5.get().title()
            email = e9.get().upper()
            mobile =e7.get()
            pin = e10.get()
            gender = e8.get().upper()
            address = e6.get()
            bal=e11.get()
            flag = False
            for i in range(0, 10):
                if str(i) in name:
                    flag = True
                    break
            s = len(email)
            if name == "" or email == "" or mobile == "" or pin == "" or gender == "" or address=="":
                messagebox.showerror("", "All Fields Are Mandatory!")
            elif flag:
                messagebox.showerror("", "Do Not Enter Any Number In Name Field!")
            elif not mobile.isnumeric() or len(mobile) != 10:
                messagebox.showerror("", "Enter a Valid Mobile Number!")
            elif not pin.isnumeric() or len(pin) != 4:
                messagebox.showerror("", "Enter a Valid PIN!")
            elif len(pin) > 4:
                messagebox.showwarning("", "PIN greater than rage !!")
            elif int(bal) < 5000:
                messagebox.showerror("", "Minimum amount to be deposit is 5000!!!")
            elif len(name) > 20:
                messagebox.showwarning("", "Name too long")
            elif len(address) > 50:
                messagebox.showwarning("", "Name too long")
            elif gender not in ("MALE","FEMALE","OTHERS"):
                messagebox.showerror("", "Your provided Gender type isn't available")
            else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select * from account where email='"+e.get()+"' or phno='"+pn.get()+"' or pin='"+p.get()+"'")
                result = cr.fetchone()

                if result is None:
                    cr=db.cursor()
                    cr.execute("insert into account values('"+ac.get()+"','"+n.get()+"','"+add.get()+"','"+pn.get()+"','"+g.get()+"','"+e.get()+"','"+p.get()+"','"+b.get()+"')")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "Registration successfull")
                else:
                    db.close()
                    messagebox.showerror("", "An Acount With Same Email or Mobile Number or PIN Already Exist!")
            ac.set("")
            n.set("")
            add.set("")
            pn.set("")
            g.set("")
            e.set("")
            p.set("")
            b.set("")
            viewadmin(f20)
        b4=Button(f13,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=create1)
        b4.place(relx=0.43,rely=0.5)


def view(m):
    f14=Frame(bg="#fff")
    m.add(f14,text="  All   Accounts           ")
    global f20
    f20=f14
    viewadmin(f14)

def viewadmin(f14):
    l1=Label(f14,text="Accounts Detail",font=("algerian",40),bg="#fff",fg="royalblue")
    l1.place(relx=0.35,rely=0.02)
    l4=Label(f14,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
    l4.place(relx=0.02,rely=0.1)
    l5=Label(f14,text="Name",font=("arial",15),bg="#fff",fg="royalblue")
    l5.place(relx=0.15,rely=0.1)
    l6=Label(f14,text="Address",font=("arial",15),bg="#fff",fg="royalblue")
    l6.place(relx=0.3,rely=0.1)
    l7=Label(f14,text="Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
    l7.place(relx=0.45,rely=0.1)
    l8=Label(f14,text="Gender",font=("arial",15),bg="#fff",fg="royalblue")
    l8.place(relx=0.6,rely=0.1)
    l9=Label(f14,text="Email",font=("arial",15),bg="#fff",fg="royalblue")
    l9.place(relx=0.75,rely=0.1)
    l11=Label(f14,text="Balance",font=("arial",15),bg="#fff",fg="royalblue")
    l11.place(relx=0.9,rely=0.1)
    db=sqlite3.connect("back.db")
    cr=db.cursor()
    r=cr.execute("select * from account")
    x=0.04
    y=0.15
    for r1 in r:
        Label(f14,text=r1[0],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.1
        Label(f14,text=r1[1],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.17
        Label(f14,text=r1[2],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.16
        Label(f14,text=r1[3],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.14
        Label(f14,text=r1[4],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.125
        Label(f14,text=r1[5],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        x +=0.165
        Label(f14,text=r1[7],font=("arial",10),bg="#fff",fg="black").place(relx=x,rely=y)
        y += 0.05
        x=0.04
    db.commit()
    db.close()

def searchadmin(m):
    f15=Frame(bg="#fff")
    ac=StringVar()
    m.add(f15,text="  Search Account          ") 
    a2=Label(f15,text="Search account",font=("algerian",40),fg="royalblue",bg="#fff")
    a2.place(relx=0.35,rely=0.05) 
    l4=Label(f15,text="Enter Account Number",font=("arial",15),bg="#fff",fg="royalblue")
    l4.place(relx=0.05,rely=0.15)
    e4=Entry(f15,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=ac)
    e4.place(relx=0.05,rely=0.2,width=300)
    c3=Canvas(f15,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.05,rely=0.23)
    def search1():
        db=sqlite3.connect("back.db")
        cr=db.cursor()
        r=cr.execute("select * from account where acno='"+ac.get()+"' ")
        for r1 in r:
            l15=Label(f15,text="Account Number",font=("arial",15),bg="#fff",fg="royalblue")
            l15.place(relx=0.3,rely=0.3)
            l16=Label(f15,font=(" ",15), text = r1[0],bg="#fff",fg="black")
            l16.place(relx=0.45,rely=0.3)
            l17=Label(f15,text="Name",font=("arial",15),bg="#fff",fg="royalblue")
            l17.place(relx=0.3,rely=0.35)
            l17=Label(f15,font=(" ",15), text = r1[1],bg="#fff",fg="black")
            l17.place(relx=0.45,rely=0.35)
            l18=Label(f15,text="Address",font=("arial",15),bg="#fff",fg="royalblue")
            l18.place(relx=0.3,rely=0.4)
            l18=Label(f15,font=(" ",15), text = r1[2],bg="#fff",fg="black")
            l18.place(relx=0.45,rely=0.4)        
            l19=Label(f15,text="Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
            l19.place(relx=0.3,rely=0.45)
            l19=Label(f15,font=(" ",15), text = r1[3],bg="#fff",fg="black")
            l19.place(relx=0.45,rely=0.45) 
            l20=Label(f15,text="Gender",font=("arial",15),bg="#fff",fg="royalblue")
            l20.place(relx=0.3,rely=0.5)
            l20=Label(f15,font=(" ",15), text = r1[4],bg="#fff",fg="black")
            l20.place(relx=0.45,rely=0.5)  
            l21=Label(f15,text="E-Mail",font=("arial",15),bg="#fff",fg="royalblue")
            l21.place(relx=0.3,rely=0.55)
            l21=Label(f15,font=(" ",15), text = r1[5],bg="#fff",fg="black")
            l21.place(relx=0.45,rely=0.55)
            l22=Label(f15,text="Balance",font=("arial",15),bg="#fff",fg="royalblue")
            l22.place(relx=0.3,rely=0.6)
            l23=Label(f15,font=(" ",15), text = r1[7],bg="#fff",fg="black")
            l23.place(relx=0.45,rely=0.6)
            break
        else:
            messagebox.showinfo('Search Menu','Invalid Account Number ')
        db.commit()
        db.close()
        ac.set("")
    b4=Button(f15,text="Search",bg="royalblue",fg="white",width=20,height=2,command=search1)
    b4.place(relx=0.3,rely=0.18)


def update_by_admin(m):
    f16=Frame(bg="#fff")
    m.add(f16,text="  Update  Account          ")
    ac=StringVar()
    u1=StringVar()
    u2=StringVar()
    u3=StringVar()
    u4=StringVar()
    u5=StringVar()
    a2=Label(f16,text="Update account",font=("algerian",40),fg="royalblue",bg="#fff")
    a2.place(relx=0.35,rely=0.05) 
    l4=Label(f16,text="Enter Account Number",font=("arial",15),bg="#fff",fg="royalblue")
    l4.place(relx=0.05,rely=0.15)
    e4=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=ac)
    e4.place(relx=0.05,rely=0.2,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.05,rely=0.23)
    l34=Label(f16,text="Enter New Details",font=("algerian",30),bg="#fff",fg="royalblue")
    l34.place(relx=0.5,rely=0.25)
    l35=Label(f16,text="Enter Name",font=("arial",15),bg="#fff",fg="royalblue")
    l35.place(relx=0.5,rely=0.4)
    e4=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=u1)
    e4.place(relx=0.65,rely=0.4,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.65,rely=0.43)
    l36=Label(f16,text="Enter Address",font=("arial",15),bg="#fff",fg="royalblue")
    l36.place(relx=0.5,rely=0.45)
    e5=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=u2)
    e5.place(relx=0.65,rely=0.45,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.65,rely=0.48)
    l37=Label(f16,text="Enter Phone Number",font=("arial",15),bg="#fff",fg="royalblue")
    l37.place(relx=0.5,rely=0.5)
    e6=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=u3)
    e6.place(relx=0.65,rely=0.5,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.65,rely=0.53)
    l38=Label(f16,text="Enter E-mail",font=("arial",15),bg="#fff",fg="royalblue")
    l38.place(relx=0.5,rely=0.55)
    e8=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=u4)
    e8.place(relx=0.65,rely=0.55,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.65,rely=0.58)
    l38=Label(f16,text="Enter PIN",font=("arial",15),bg="#fff",fg="royalblue")
    l38.place(relx=0.5,rely=0.6)
    e7=Entry(f16,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=u5)
    e7.place(relx=0.65,rely=0.6,width=300)
    c3=Canvas(f16,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.65,rely=0.63)
    def update1():
        name = e4.get().title()
        email = e8.get().upper()
        mobile = e6.get()
        address = e5.get()
        pin=e7.get()
        flag = False
        for i in range(0, 10):
            if str(i) in name:
                flag = True
                break
        s = len(email)
        if name == "" or email == "" or mobile == "" or address=="" or pin=="":
                messagebox.showerror("", "All Fields Are Mandatory!")
        elif flag:
            messagebox.showerror("", "Do Not Enter Any Number In Name Field!")
        elif '@' not in email or not email.endswith(".COM") or email[0] == '@' or email[s - 5] == '@' or email.count('@') > 1:
                messagebox.showerror("", 'Enter A Valid Email!')
        elif not mobile.isnumeric() or len(mobile) != 10:
                messagebox.showerror("", "Enter a Valid Mobile Number!")
        elif len(name) > 20:
                messagebox.showwarning("", "Name too long")
        elif len(pin) > 4:
                messagebox.showwarning("", "PIN greater than rage !!")
        elif len(address) > 50:
                messagebox.showwarning("", "Name too long")
        else:
                db=sqlite3.connect("back.db")
                cr=db.cursor()
                cr.execute("select * from account where email='"+u4.get()+"' or phno='"+u3.get()+"' or pin='"+u5.get()+"'")
                result = cr.fetchone()
                if result is None:
                    cr=db.cursor()
                    cr.execute("update account set name='"+u1.get()+"',address='"+u2.get()+"',phno='"+u3.get()+"',email='"+u4.get()+"',pin='"+u5.get()+"' where acno='"+ac.get()+"'")
                    db.commit()
                    db.close()
                    messagebox.showinfo(" ", "Information Updated Succesfully")
                else:
                    db.close()
                    messagebox.showerror("", "An Acount With Same Email or Mobile Number or PIN Already Exist!")
        u1.set("")
        u2.set("")
        u3.set("")
        u4.set("")
        u5.set("")
        ac.set("")
        viewadmin(f20)
    b4=Button(f16,text="Update",bg="green",fg="white",width=20,height=2,command=update1)
    b4.place(relx=0.45,rely=0.7)
    
    


def delete_by_admin(m):
    f17=Frame(bg="#fff")
    ac=StringVar()
    m.add(f17,text="   Delete  Account")
    a2=Label(f17,text="Delete account",font=("algerian",40),fg="royalblue",bg="#fff")
    a2.place(relx=0.35,rely=0.05) 
    l4=Label(f17,text="Enter Account Number",font=("arial",15),bg="#fff",fg="royalblue")
    l4.place(relx=0.3,rely=0.25)
    e4=Entry(f17,font=("arial",15),highlightthickness=0,relief=FLAT,bg="#fff",fg="black",textvariable=ac)
    e4.place(relx=0.35,rely=0.3,width=300)
    c3=Canvas(f17,width=300,height=2,bg="black",highlightthickness=0)
    c3.place(relx=0.35,rely=0.33)
    def delete1():
        pin=e4.get()
        if pin=="":
            messagebox.showerror("","Please Enter the PIN")
        else:
            db=sqlite3.connect("back.db")
            cr=db.cursor()
            cr.execute("select * from account where  acno='"+ac.get()+"'")
            result = cr.fetchone()
            if result is None:
                db.close()
                messagebox.showerror("", "This Account Number has no account")
            else:
                cr=db.cursor()
                cr.execute("delete from account where acno='"+ac.get()+"' ")
                db.commit()
                db.close()
                messagebox.showinfo(" ", "Account Deleted Succesfully")

        ac.set("")
        viewadmin(f20)
    b4=Button(f17,text="Submit",bg="royalblue",fg="white",width=20,height=2,command=delete1)
    b4.place(relx=0.6,rely=0.3)


def logout_admin(m):
    f18=Frame(bg="#fff")
    m.add(f18,text="      LogOut     ")
    a2=Label(f18,text="Admin! Do you really want to logout....",font=("algerian",40),fg="royalblue",bg="#fff")
    a2.place(relx=0.15,rely=0.25)
    b4=Button(f18,text="Yess",bg="royalblue",fg="white",width=20,height=2,command=login)
    b4.place(relx=0.45,rely=0.5) 

def ext():
    pr.destroy()


pr=Tk()
pr.title("Banking Management System")
pr.minsize(1500,1000)
pr.state('zoomed')
img=PhotoImage(file='Screenshot (94).png') 
pr.configure(bg="#fff")
first=login()
pr.mainloop()