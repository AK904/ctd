from tkinter import *
import hashlib

def login():
    user=username.get()
    pas=password.get()
    huser = hashlib.md5(user.encode('utf_8')).hexdigest()
    hpass = hashlib.md5(pas.encode('utf_8')).hexdigest()
    user1 = "Ahmed"
    pass1 = "1234"
    huser1 = hashlib.md5(user1.encode('utf_8')).hexdigest()
    hpass1 = hashlib.md5(pass1.encode('utf_8')).hexdigest()
    if user=='' or pas=='':
        message.set("fill the empty field!!!")
    else:

      if huser==huser1 and hpass==hpass1:
       message.set("login succeeded")
      else:
       message.set("Wrong username or password!!!")

def Loginform():

    global login_screen
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("500x350")

    global message
    global username
    global password

    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    Label(login_screen, text="Username : ").place(x=20,y=40)
    Entry(login_screen,width = "30",textvariable=username).place(x=90,y=42)
    Label(login_screen, text="Password : ").place(x=20,y=100)
    Entry(login_screen, width="30" ,textvariable=password ,show="*").place(x=90,y=100)
    Label(login_screen, text="",textvariable=message).place(x=160,y=150)
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=200,y=200)
    login_screen.mainloop()
Loginform()
