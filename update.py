#import all modules
from tkinter import *
from tkinter import font
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

conn =mysql.connector.connect(host="localhost",database='crud',user="root",password='')

mycursor = conn.cursor()

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text='Update student information',font=('Courier new',40),fg='black')
        self.heading.place(x=100,y=0)

        #label and entry of id
        self.id_le = Label(master,text='Enter ID',font=('Courier new ',10))
        self.id_le.place(x=0,y=70)

        self.id_leb = Entry(master,font=('Courier new',10),width=10)
        self.id_leb.place(x=380,y=70)

        self.btn_search = Button(master,text="Search",width=8,height=0,bg='orange',command=self.search)
        self.btn_search.place(x=500,y=70)

        #label for the window
        self.first = Label(master,text="Enter First name",font=('Courier new',10,'bold'))
        self.first.place(x=0,y=120)

        self.last = Label(master,text="Enter Last name",font=('Courier new',10,'bold'))
        self.last.place(x=0,y=170)

        self.gender = Label(master,text="Enter gender",font=('Courier new',10,'bold'))
        self.gender.place(x=0,y=220)

        self.address = Label(master,text="Enter address",font=('Courier new',10,'bold'))
        self.address.place(x=0,y=270)

        self.contact = Label(master,text="Enter contact",font=('Courier new',10,'bold'))
        self.contact.place(x=0,y=320)

        self.course = Label(master,text="Enter course",font=('Courier new',10,'bold'))
        self.course.place(x=0,y=370)


        #enteries of window

        self.first = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.first.place(x=380,y=120)

        self.last = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.last.place(x=380,y=170)

        self.gender = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.gender.place(x=380,y=220)

        self.address = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.address.place(x=380,y=270)
        
        self.contact = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.contact.place(x=380,y=320)
        
        self.course = Entry(master,width=25,font=('Courier new',10,'bold'))
        self.course.place(x=380,y=370)


        #button to add to the database
        self.btn_add = Button(master,text='Update student',width=27,height=1,bg='green',fg='white',command=self.update)
        self.btn_add.place(x=380,y=420)

    def search(self,*args,**kwargs):
        mycursor.execute('SELECT * FROM tbl_student WHERE Stud_Id%s','&#91;self.id_leb.get()]')
        result = mycursor.fetchall()
        for r in result:
            print('')
            # self.n1 = r&#91;1] 
            # self.n2 = r&#91;2] 
            # self.n3 = r&#91;3] 
            # self.n4 = r&#91;4] 
            # self.n5 = r&#91;5] 
            # self.n6 = r&#91;6]
        conn.commit()

        #inster into the enteries to update
        self.first.delete(0,END)
        self.first.insert(0,str(self.n1))

        self.last.delete(0,END)
        self.last.insert(0,str(self.n2))

        self.gender.delete(0,END)
        self.gender.insert(0,str(self.n3))

        self.address.delete(0,END)
        self.address.insert(0,str(self.n4))

        self.contact.delete(0,END)
        self.contact.insert(0,str(self.n5))

        self.course.delete(0,END)
        self.course.insert(0,str(self.n6))


    def update(self,*args,**kwargs):
        self.u1 = self.first.get()
        self.u2 = self.last.get()
        self.u3 = self.gender.get()
        self.u4 = self.address.get()
        self.u5 = self.contact.get()
        self.u6 = self.course.get()

        mycursor.execute('UPDATE tbl_student SET FirstName=%s,LastName=%s,Gender=%s,Address=%s,ContactNumber=%s,Course=%s WHERE Stud_ID=%s",&#91;self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.id_leb.get()])')
        conn.commit()
        tkinter.messagebox.showinfo("Success","Update Student Successfully")


root = Tk()
b = Database(root)
root.geometry("1000x760,0+0")
root.title("Update Student Information")
root.mainloop()