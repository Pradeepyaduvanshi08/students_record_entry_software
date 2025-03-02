from tkinter import *
from tkinter import ttk
import psycopg2
import tkinter
from tkinter import messagebox
import datetime



mypass="abcd1234"
mydatabase="student"

class Student:
    def __init__(self,root):
        self.root =root
        self.root.title("Student Management System")
        self.root.geometry("1379x800+0+0")
        title=Label(self.root,text="Student Management System" ,bg="yellow",fg="Black",font=("times new roman" ,40 ,"bold"))
        title.pack(side=TOP , fill=X)

        #variable for database

        self.Roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        
        self.search_by=StringVar()

        self.search_txt=StringVar()
        

        #Mainframe design
        Mainframe=Frame(self.root,relief=RIDGE, bg="pink" ,bd=12 ,padx=10)
        Mainframe.place(x=20 ,y=80,width=450,height=620)
        mtitle=Label(Mainframe ,text="Manage student" ,bg="powder blue",fg="Black",font=("times new roman", 40 ,"bold"))
        mtitle.grid(row=0,columnspan=2 ,pady=2)


        lbl_roll=Label(Mainframe ,text="Roll NO", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_roll.grid(row=1,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_roll=Entry(Mainframe,textvariable=self.Roll ,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1 ,pady=10 ,padx=10,sticky="w")
        
        lbl_name=Label(Mainframe ,text="Name", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_name.grid(row=2,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_name=Entry(Mainframe ,textvariable=self.name,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1 ,pady=10 ,padx=10,sticky="w")

        lbl_Email=Label(Mainframe ,text="Email", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_Email.grid(row=3,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_Email=Entry(Mainframe ,textvariable=self.email,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1 ,pady=10 ,padx=10,sticky="w")

        lbl_Gender=Label(Mainframe ,text="Gender", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_Gender.grid(row=4,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_Gender=ttk.Combobox(Mainframe, textvariable=self.gender,font=("times new roman" ,15 ,"bold"),state="readonly")
        txt_Gender['values']=("Male","female","others")
        txt_Gender.grid(row=4,column=1 ,pady=10 ,padx=10,sticky="w")

        lbl_contact=Label(Mainframe  ,text="Contact", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_contact.grid(row=5,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_contact=Entry(Mainframe ,textvariable=self.contact,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1 ,pady=10 ,padx=10,sticky="w")

        lbl_Dob=Label(Mainframe ,text="Date of Birth", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_Dob.grid(row=6,column=0 ,pady=10 ,padx=10,sticky="w")

        txt_Dob=Entry(Mainframe ,textvariable=self.dob ,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1 ,pady=10 ,padx=10,sticky="w")

        lbl_Address=Label(Mainframe ,text="Address", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_Address.grid(row=7,column=0 ,pady=10 ,padx=10,sticky="w")

        self.txt_Address=Text(Mainframe  ,font=("times new roman" ,15 ,"bold"),width=20,height=3,bd=5,relief=GROOVE)
        self.txt_Address.grid(row=7,column=1 ,pady=10 ,padx=10,sticky="w")


        #button frame
        btn_frame=Frame(Mainframe,bd=6,bg="pink",relief=GROOVE)
        btn_frame.place(x=5,y=520,width=410,height=60)

        Addbtn=Button(btn_frame,text="Add",width=10 ,command=self.add_students).grid(padx=10,pady=10,row=0,column=0)
        Updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(padx=10,pady=10,row=0,column=1)
        Deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(padx=10,pady=10,row=0,column=2)
        Celearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(padx=10,pady=10,row=0,column=3)


        #Details Frame

        Detail_frame=Frame(self.root,bd=6,bg="pink",relief=GROOVE)
        Detail_frame.place(x=500,y=75,width=820,height=880)

        lbl_search=Label(Detail_frame ,text="Search By", bg="pink",fg="Black",font=("times new roman" ,20 ,"bold"))
        lbl_search.grid(row=0,column=0,padx=10,pady=20,sticky="w")

        combo_Search=ttk.Combobox(Detail_frame ,textvariable=self.search_by,font=("times new roman" ,15 ,"bold"),state="readonly")
        combo_Search['values']=("rollno")
        combo_Search.grid(row=0,column=1 ,pady=10 ,padx=10,sticky="w")
        
        
        txt_search=Entry(Detail_frame ,textvariable=self.search_txt,font=("times new roman" ,15 ,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2 ,pady=10 ,padx=10,sticky="w")

        Seacrhbtn=Button(Detail_frame,text="Search",width=10,command=self.search_data ).grid(padx=10,pady=10,row=0,column=3)
        Showallbtn=Button(Detail_frame,text="Showall",width=10, command=self.fetch_data).grid(padx=10,pady=10,row=0,column=4)
        

        #table frame
        Table_frame=Frame(Detail_frame,bd=6,bg="yellow",relief=GROOVE)
        Table_frame.place(x=10,y=75,width=790,height=550)

        scrollx=Scrollbar(Table_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(Table_frame,orient=VERTICAL)

        #treeview of student details

        self.Student_table=ttk.Treeview(Table_frame,column=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scrollx,yscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM ,fill=X)
        scrolly.pack(side=LEFT ,fill=Y)

        scrollx.config(command=self.Student_table.xview)
        scrolly.config(command=self.Student_table.yview)

        #heading of student_table

        self.Student_table.heading("roll",text="Roll_NO")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=150)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=180)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


        #all database work

        #function to add information

    def add_students(self):
        if(self.Roll.get()=="" or self.name.get()==""):
            messagebox.showerror("Error","all feilds are required")
        else:
            con = psycopg2.connect(host="localhost",user="postgres",password=mypass,database=mydatabase)
            cur=con.cursor()
            self.fetch_data()
            cur.execute('insert into "StdData" values(%s,%s,%s,%s,%s,%s,%s)',
                                (self.Roll.get(),
                                self.name.get(),
                                self.email.get(),
                                self.gender.get(),
                                self.contact.get(),
                                self.dob.get(),
                                self.txt_Address.get("1.0",END))  )
            
            con.commit()
            self.clear()
            con.close()
            messagebox.showinfo("success","student information added")


    

    def fetch_data(self):
        conn= psycopg2.connect(host="localhost",user="postgres",password=mypass,database=mydatabase)

        mycur=conn.cursor()
        mycur.execute('select * from "StdData" ')
        rows=mycur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,value=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.Roll.set(""),
        self.name.set(""),
        self.email.set(""),
        self.gender.set(""),
        self.contact.set(""),
        self.dob.set(""),
        self.txt_Address.delete("1.0",END)


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        self.Roll.set(row[0]),
        self.name.set(row[1]),
        self.email.set(row[2]),
        self.gender.set(row[3]),
        self.contact.set(row[4]),
        self.dob.set(row[5]),
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])



    def update_data(self):
        con = psycopg2.connect(host="localhost",user="postgres",password=mypass,database=mydatabase)
        cur=con.cursor()
        self.fetch_data()
        cur.execute(' update "StdData" set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where rollno=%s',
                                           (self.name.get(),
                                            self.email.get(),
                                            self.gender.get(),
                                            self.contact.get(),
                                            self.dob.get(),
                                            self.txt_Address.get("1.0",END),
                                            self.Roll.get())  )
            
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success","student information Updated")


    def delete_data(self):
        con = psycopg2.connect(host="localhost",user="postgres",password=mypass,database=mydatabase)
        cur=con.cursor()
        cur.execute('delete from "StdData" where rollno= '+ str(self.Roll.get()))
       
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
        con = psycopg2.connect(host="localhost",user="postgres",password=mypass,database=mydatabase)
        cur=con.cursor()
        cur.execute('select * from "StdData" where   rollno = '  +str( self.search_txt.get()))
   
        rows=cur.fetchall()
        
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,value=row)
                con.commit()
        con.close()
        

        
        
        
        
        
        
       

    
        
        
    
            
        


        




root = Tk()
ob =Student(root)
root.mainloop()
