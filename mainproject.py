from tkinter import*
import pymysql
import pymysql.cursors
from tkinter import messagebox
from PIL import ImageTk, Image


def find():
    uid=idd.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='south')
    a=conn.cursor()

    a.execute("select * from lib where studentrollno='"+uid+"'")
    results=a.fetchall()
    count=a.rowcount
    if(count>0):
        for row in results:
            iid.set(row[0])
            bname.set(row[1])
            sname.set(row[2])
            date.set(row[3])
    else:
        messagebox.showinfo("hello","Record Not Found")


def insert():
    uid1=iid1.get()
    stuname1=sname1.get()
    bookid=bid1.get()
    bookname1=bname1.get()
    idate1=date1.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='south')
    a=conn.cursor()
    a.execute(" insert into lib(studentrollno ,studentname,bookid,bookname,issuedate)values('"+uid1+"','"+stuname1+"','"+bookname1+"','"+bookid+"','"+idate1+"')")
    conn.commit()
    messagebox.showinfo(" message","INSERTED")
    
    conn.rollback()
    messagebox.showinfo(" message","failed")
    conn.close()

def update():
    uid=iid2.get()
    bookid3=bid3.get()
    bookname3=bname3.get()
    
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',db='south')
        a=conn.cursor()
        b=conn.cursor()
        a.execute(" update  lib set bookid='"+bookid3+"' where id='" +uid+"'")
        b.execute(" update  lib set bookname='"+bookname3+"' where id='" +uid+"'")
        conn.commit()
        messagebox.showinfo(" message","UPDATED")
       
    except:
        
        conn.rollback()
        messagebox.showinfo("message", "not updated")
    conn.close()


win=Tk()
#win.geometry("1500x1300")
win.attributes('-fullscreen',True)
#win.title("windows application")

load=Image.open('ghost.jpg')
render=ImageTk.PhotoImage(load)
img=Label(win,image=render)
win.attributes('-alpha',1.0)

img.place(x=0,y=0)
#Label(win,text='project').pack(padx=0)

win.title("windows application")
win.config(bg='black')
topframe=Frame(win,width=1500,height=200,bg="yellow",relief="raise",bd=10)
topframe.pack(side=TOP)

lb=Label(topframe,text="BOOK LIBRARY MANAGEMENT",font=('italic',40,'bold'),width=41,fg='black',bd=4)
lb.grid(row=0,column=0)

mframe=Frame(win,width=900,height=800,bg="orange",relief='raise',bd=10)
mframe.pack(ipadx=0,side='right')

lb=Label(mframe,text="Search Result",font=('italic',15,'bold'),bd=5,width=30,fg='black',relief='raise')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb66=Label(mframe,text='Student roll number',width=20)
lb66.grid(row=1,column=0,padx=10,pady=10)

idd=StringVar()
tb=Entry(mframe,textvariable=idd)
tb.grid(row=1,column=1)

btn1=Button(mframe,text="search",font=('italic',15,'bold'),bd=5,width=12,fg='black',relief='raise',command=find)
btn1.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

lb3=Label(mframe,text='Book id',width=15)
lb3.grid(row=3,column=0,padx=10,pady=10)


lb4=Label(mframe,text='Book name',width=15)
lb4.grid(row=4,column=0,padx=10,pady=10)


lb5=Label(mframe,text='Student Name',width=15)
lb5.grid(row=5,column=0,padx=10,pady=10)


lb6=Label(mframe,text='Issue Date',width=15)
lb6.grid(row=6,column=0,padx=10,pady=10)

iid=StringVar()
tb1=Entry(mframe,textvariable=iid)
tb1.grid(row=3,column=1)

bname=StringVar()
tb2=Entry(mframe,textvariable=bname)
tb2.grid(row=4,column=1)

sname=StringVar()
tb3=Entry(mframe,textvariable=sname)
tb3.grid(row=5,column=1)

date=StringVar()
tb4=Entry(mframe,textvariable=date)
tb4.grid(row=6,column=1)

mframe1=Frame(win,width=900,height=800,bg="blue",relief='raise',bd=10)
mframe1.pack(padx=10,pady=0,side='left')

nb=Label(mframe1,text="Insert into Table",font=('italic',15,'bold'),bd=5,width=20,fg='black',relief='raised')
nb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

nb1=Label(mframe1,text="Student roll no",width=15)
nb1.grid(row=1,column=0,padx=10,pady=10)
iid1=StringVar()
nb1=Entry(mframe1,textvariable=iid1)
nb1.grid(row=1,column=2,columnspan=2,padx=10,pady=10)

nb2=Label(mframe1,text="Student name",width=15)
nb2.grid(row=2,column=0,padx=10,pady=10)
sname1=StringVar()
nb2=Entry(mframe1,textvariable=sname1)
nb2.grid(row=2,column=2,columnspan=2,padx=10,pady=10)

nb3=Label(mframe1,text="Book id",width=15)
nb3.grid(row=3,column=0,padx=10,pady=10)
bid1=StringVar()
nb3=Entry(mframe1,textvariable=bid1)
nb3.grid(row=3,column=2,columnspan=2,padx=10,pady=10)

nb4=Label(mframe1,text="Book name",width=15)
nb4.grid(row=4,column=0,padx=10,pady=10)
bname1=StringVar()
nb4=Entry(mframe1,textvariable=bname1)
nb4.grid(row=4,column=2,columnspan=2,padx=10,pady=10)

nb11=Label(mframe1,text="Issue date",width=15)
nb11.grid(row=5,column=0,padx=10,pady=10)
date1=StringVar()
nb11=Entry(mframe1,textvariable=date1)
nb11.grid(row=5,column=2,columnspan=2,padx=10,pady=10)


btn2=Button(mframe1,text="submit",font=('italic',15,'bold'),bd=5,width=12,fg='black',relief='raise',command=insert)
btn2.grid(row=6,column=1,columnspan=1,padx=10,pady=10)


mframe2=Frame(win,bg="red",width=500,height=400,relief='raise',bd=10)
mframe2.pack(ipadx=60,ipady=60,side='top')

zb=Label(mframe2,text="Update Information",font=('italic',15,'bold'),bd=5,fg='black',relief='raise')
zb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

yb1=Label(mframe2,text="Student Roll No",width=15)
yb1.grid(row=1,column=0,padx=10,pady=10)
iid2=StringVar()
hb1=Entry(mframe2,textvariable=iid2)
hb1.grid(row=1,column=1,padx=10,pady=10)

yb2=Label(mframe2,text="Book id",width=15)
yb2.grid(row=2,column=1,padx=10,pady=10)
bid3=StringVar()
hb2=Entry(mframe2,textvariable=bid3)
hb2.grid(row=2,column=2,columnspan=2,padx=10,pady=10)

yb3=Label(mframe2,text="Book name",width=15)
yb3.grid(row=4,column=1,padx=10,pady=10)
bname3=StringVar()
hb3=Entry(mframe2,textvariable=bname3)
hb3.grid(row=4,column=2,columnspan=2,padx=10,pady=10)

yb4=Label(mframe2,text='STUDENT ROLL NO AND NAME WILL NOT BE EDITED',font=('italic',10,'bold'),fg='blue',bg='black')
yb4.grid(row=6,padx=10,pady=10,rowspan=4,columnspan=3)

btn3=Button(mframe2,text="UPDATE",font=('italic',15,'bold'),bd=5,width=12,fg='black',relief='raise',command=update)
btn3.grid(row=5,column=1,columnspan=2,padx=10,pady=10)

win.mainloop()

