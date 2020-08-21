from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os
from PIL import ImageTk, Image


def register():
  unm=username.get()
  eid=email.get()
  pw=password.get()
  cn=contact.get()
  try:
      conn=pymysql.connect(host='localhost',user='root',password='',db='south')
      a=conn.cursor()
      a.execute(" insert into registration(username,emailid,password1,contact)values('"+unm+"','"+eid+"','"+pw+"','"+cn+"')")
      conn.commit()
      messagebox.showinfo(" message","sucessfully registered")
      if(conn.commit==True):
        os.system('mainproject.py')
  except:
      conn.rollback()
      messagebox.showinfo(" message","failed")
  conn.close()


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


mframe1=Frame(win,bg="blue",relief='raise',bd=10)
mframe1.pack(padx=10,pady=20)

nb=Label(mframe1,text="REGISTER",font=('italic',15,'bold'),bd=5,width=15,fg='white',bg='black',relief='raised')
nb.grid(row=0,column=0,columnspan=2,padx=5,pady=10)

nb1=Label(mframe1,text="username")
nb1.grid(row=1,column=0,padx=10,pady=10)
username=StringVar()
nb1=Entry(mframe1,textvariable=username)
nb1.grid(row=1,column=2,columnspan=2,padx=10,pady=10)

nb2=Label(mframe1,text="email id")
nb2.grid(row=2,column=0,padx=10,pady=10)
email=StringVar()
nb2=Entry(mframe1,textvariable=email)
nb2.grid(row=2,column=2,columnspan=2,padx=10,pady=10)

nb3=Label(mframe1,text="pass word")
nb3.grid(row=3,column=0,padx=10,pady=10)
password=StringVar()
nb3=Entry(mframe1,textvariable=password)
nb3.grid(row=3,column=2,columnspan=2,padx=10,pady=10)

nb4=Label(mframe1,text="contact")
nb4.grid(row=4,column=0,padx=10,pady=10)
contact=StringVar()
nb4=Entry(mframe1,textvariable=contact)
nb4.grid(row=4,column=2,columnspan=2,padx=10,pady=10)

btn2=Button(mframe1,text="submit",font=('italic',15,'bold'),bd=5,width=10,bg='black',fg='white',relief='raise',command=register)
btn2.grid(row=5,column=1,columnspan=2,padx=10,pady=10)

win.mainloop()
