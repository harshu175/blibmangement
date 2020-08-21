from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os
from PIL import ImageTk, Image


def login():
    unm=username.get()
    password=password1.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='south')
    a=conn.cursor()
    a.execute("Select * from registration where username='"+unm+"'and password1='"+password+"'")
    results=a.fetchall()
    count=a.rowcount
    if(count>0):
        os.system ('mainproject.py') 
    else:
        messagebox.showinfo("message","not login")

def forget():
    os.system('forgetpassword2.py')

def register():
    os.system('register2.py')
    


win=Tk()
win.attributes('-fullscreen',True)
win.title("windows application")

load=Image.open('ghost.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
win.attributes('-alpha',1.0)
img.place(x=0,y=0)

topframe=Frame(win,width=1500,height=200,bg='red',relief="raised",bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="BOOK LIBRARY MANAGEMENT",font=('italic',40,'bold'),width=41,fg='black',bd=4)
lb.grid(row=0,column=0)

mframe=Frame(win,width=1000,height=800,bg='maroon',relief="raised",bd=10)
mframe.pack(padx=50,pady=20)

lb=Label(mframe,text="LOGIN",font=('italic',15,'bold'),bd=5,width=30,fg='white',bg='black',relief="raised")
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(mframe,text="username",width=8)
lb2.grid(row=1,column=0,padx=10,pady=10)

lb3=Label(mframe,text="password",width=8)
lb3.grid(row=2,column=0,padx=10,pady=10)

username=StringVar()
tb1=Entry(mframe,textvariable=username)
tb1.grid(row=1,column=1)
password1=StringVar()
tb2=Entry(mframe,textvariable=password1)
tb2.grid(row=2,column=1)

btn=Button(mframe,text="LOGIN",font=('italic',15,'bold'),bd=5,width=12,fg='white',relief="raised",bg='black',command=login)
btn.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

btn=Button(mframe,text="forget password",font=('italic',15,'bold'),bd=5,width=15,fg='white',relief="raised",bg='black',command=forget)
btn.grid(row=6,column=1,columnspan=3,padx=10,pady=10)

btn=Button(mframe,text="register",font=('italic',15,'bold'),bd=5,width=12,fg='white',relief="raised",bg='black',command=register)
btn.grid(row=6,column=0,columnspan=1,padx=10,pady=10)

win.mainloop()

