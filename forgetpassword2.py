from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os
from PIL import ImageTk, Image

def forget():
  nm=name.get()
  emailid1=email.get()
  cn=contact.get()
  
  conn=pymysql.connect(host='localhost',user='root',password='',db='south')
  a=conn.cursor()
  a.execute("Select password1 from registration where username='"+nm+"'and emailid='"+emailid1+"'and contact='"+cn+"'")
  results=a.fetchall()
  count=a.rowcount

  if(count>0):
    for row in results:
      for j in range(0,count):
        messagebox.showinfo("your password is",row[j])

  else:
    messagebox.showinfo("message","not found")
      
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

lb2=Label(mframe,text="username",width=8)
lb2.grid(row=1,column=0,padx=10,pady=10)

lb4=Label(mframe,text="contact number",width=12)
lb4.grid(row=3,column=0,padx=10,pady=10)

lb5=Label(mframe,text="email id",width=8)
lb5.grid(row=2,column=0,padx=10,pady=10)

name=StringVar()
tb1=Entry(mframe,textvariable=name)
tb1.grid(row=1,column=1)

contact=StringVar()
tb2=Entry(mframe,textvariable=contact)
tb2.grid(row=3,column=1)

email=StringVar()
tb2=Entry(mframe,textvariable=email)
tb2.grid(row=2,column=1)
              
btn=Button(mframe,text="get password",font=('italic',10,'bold'),bd=5,width=12,fg='white',relief="raised",bg='black',command=forget)
btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
              
win.mainloop()
