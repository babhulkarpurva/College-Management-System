#VIDEO LINK::
#https://drive.google.com/file/d/15FXPRVLo5wHu8PAeaRA2IKqFZ7mQbhdl/view?usp=sharing
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image



def login():
    username = e_username.get()
    password = e_password.get()

    if(username != "admin" or password != "sggs"):
        MessageBox.showinfo("INVALID","ENTER VALID USERNAME OR PASSWORD")
    else:
        def faculty():
            def get():
                if(e1_id.get()==""):
                    MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY TO FETCH")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("select * from faculty where id ='" + e1_id.get()+"'")
                    #command_handler.execute("commit")
                    rows = command_handler.fetchall()
                    if rows:
                        for row in rows:
                            e1_Name.insert(0,row[1])
                            e1_dept_name.insert(0,row[2])
                            e1_Salary.insert(0,row[3])
                    MessageBox.showinfo("FETCH STATUS","FETCHED SUCCESSFULLY")
                    db.close()
            def update():
                id1 = e1_id.get()
                Name1 = e1_Name.get()
                dept_name1 = e1_dept_name.get()
                Salary1 = e1_Salary.get()
                if(id1=="" or Name1 =="" or dept_name1 =="" or Salary1==""):
                    MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("UPDATE faculty set name='"+ Name1 +"', dept_name='"+ dept_name1 +"',tot_credit='"+ Salary1 +"'where id ='"+ id1 +"'")
                    command_handler.execute("commit")
                    e1_id.delete(0,"end")
                    e1_Name.delete(0,"end")
                    e1_dept_name.delete(0,"end")
                    e1_Salary.delete(0,"end")
                    show()
                    MessageBox.showinfo("UPDATE STATUS","UPDATED SUCCESSFULLY")
                    db.close()
            def delete():
                if(e1_id.get()==""):
                    MessageBox.showinfo("DELETE STATUS","ID IS COMPULSORY TO DELETE")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("delete from faculty where id='"+ e1_id.get() +"'")
                    command_handler.execute("commit")
                    e1_id.delete(0,"end")
                    e1_Name.delete(0,"end")
                    e1_dept_name.delete(0,"end")
                    e1_Salary.delete(0,"end")   
                    show()   
                    MessageBox.showinfo("DELETE STATUS","DELETED SUCCESSFULLY")
                    db.close()
            def insert():
                id1 = e1_id.get()
                Name1 = e1_Name.get()
                dept_name1 = e1_dept_name.get()
                Salary1 = e1_Salary.get()

                if(id1=="" or Name1 =="" or dept_name1 =="" or Salary1==""):
                    MessageBox.showinfo("INSERT STATUS","INSERT ALL FIELDS")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("insert into faculty values('"+id1+"','"+ Name1 +"','"+ dept_name1 +"','"+ Salary1 +"')")
                    command_handler.execute("commit")
                    show()
                    MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY")
                    db.close()
            def show():
                db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                command_handler = db.cursor(buffered=True)
                command_handler.execute("select * from faculty")
                rows = command_handler.fetchall()
                list.delete(0,list.size())
                for row in rows:
                    insertData = str(row[0])+'     '+row[1]+'     '+row[2]+'    '+str(row[3])
                    list.insert(list.size()+100,insertData)
                db.close()
        

            rt2 = Tk()
            rt2.geometry("800x800")
            rt2.title("FACULTY_PORTAL")
            rt2.configure(bg='hotpink')

   
            id1 = Label(rt2,text='Enter ID',font=('bold',10))
            id1.place(x=20,y=30)

            e1_id =Entry(rt2)
            e1_id.place(x=150,y=30)

            Name1 = Label(rt2,text='Enter Name',font=('bold',10))
            Name1.place(x=20,y=60)

            e1_Name =Entry(rt2)
            e1_Name.place(x=150,y=60)


            dept_name1 = Label(rt2,text='Department Name',font=('bold',10))
            dept_name1.place(x=20,y=90)

            e1_dept_name =Entry(rt2)
            e1_dept_name.place(x=150,y=90)

            Salary1 = Label(rt2,text='Salary',font=('bold',10))
            Salary1.place(x=20,y=120)

            e1_Salary =Entry(rt2)
            e1_Salary.place(x=150,y=120)


        
            insert = Button(rt2,text="insert",font=("italic",10),bg="white",command=insert)
            insert.place(x=20,y=190)

            delete = Button(rt2,text="delete",font=("italic",10),bg="white",command=delete)
            delete.place(x=70,y=190)

            update = Button(rt2,text="update",font=("italic",10),bg="white",command=update)
            update.place(x=120,y=190)

            get = Button(rt2,text="get",font=("italic",10),bg="white",command=get)
            get.place(x=170,y=190)

            
            list =Listbox(rt2,width=50,height=50)
            list.place(x=390,y=150)
            show()
            rt2.mainloop

        def department():
            def get():
                if(e_dept_name3.get()==""):
                    MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY TO FETCH")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("select * from department where dept_name ='" + e_dept_name3.get()+"'")
                    #command_handler.execute("commit")
                    rows = command_handler.fetchall()
                    if rows:
                        for row in rows:
                            e_budget.insert(0,row[1])
                            e_buiding.insert(0,row[2])
                    MessageBox.showinfo("FETCH STATUS","FETCHED SUCCESSFULLY")
                    db.close()
            def update():
                dept_name3= e_dept_name3.get()
                budget = e_budget.get()
                Buiding= e_buiding.get()
                if(dept_name3=="" or budget =="" or Buiding==""):
                    MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("UPDATE department set dept_name='"+ dept_name3 +"', buiding='"+ Buiding +"',budget='"+ budget+"'")
                    command_handler.execute("commit")
                    e_budget.delete(0,"end")
                    e_buiding.delete(0,"end")
                    e_dept_name3.delete(0,"end")
                    
                    show()
                    MessageBox.showinfo("UPDATE STATUS","UPDATED SUCCESSFULLY")
                    db.close()
            def delete():
                if(e_dept_name3.get()==""):
                    MessageBox.showinfo("DELETE STATUS","dept_name IS COMPULSORY TO DELETE")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("delete from department where dept_name='"+ e_dept_name3.get() +"'")
                    command_handler.execute("commit")
                    e_buiding.delete(0,"end")
                    e_budget.delete(0,"end")
                    e_dept_name3.delete(0,"end") 
                    show()   
                    MessageBox.showinfo("DELETE STATUS","DELETED SUCCESSFULLY")
                    db.close()
            def insert():
                dept_name3= e_dept_name3.get()
                budget = e_budget.get()
                Buiding= e_buiding.get()
                

                if(dept_name3=="" or  budget =="" or Buiding ==""):
                    MessageBox.showinfo("INSERT STATUS","INSERT ALL FIELDS")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("insert into department values('"+dept_name3+"','"+Buiding+"','"+budget+"')")
                    command_handler.execute("commit")
                    show()
                    MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY")
                    db.close()
            def show():
                db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                command_handler = db.cursor(buffered=True)
                command_handler.execute("select * from department")
                rows = command_handler.fetchall()
                list.delete(0,list.size())
                for row in rows:
                    insertData = row[0]+'     '+str(row[1])+'    '+str(row[2])
                    list.insert(list.size()+1,insertData)
                db.close()
        

            rt3 = Tk()
            rt3.geometry("600x600")
            rt3.title("DEPARTMENT_PORTAL")
            rt3.configure(bg='olive')

   
            dept_name3 = Label(rt3,text='Enter dept_name',font=('bold',10))
            dept_name3.place(x=20,y=30)

            e_dept_name3 =Entry(rt3)
            e_dept_name3.place(x=150,y=30)

            budget = Label(rt3,text='Enter budget',font=('bold',10))
            budget.place(x=20,y=60)

            e_budget =Entry(rt3)
            e_budget.place(x=150,y=60)


            Buiding = Label(rt3,text='Enter Buiding',font=('bold',10))
            Buiding.place(x=20,y=90)

            e_buiding =Entry(rt3)
            e_buiding.place(x=150,y=90)

            


        
            insert = Button(rt3,text="insert",font=("italic",10),bg="white",command=insert)
            insert.place(x=20,y=190)

            delete = Button(rt3,text="delete",font=("italic",10),bg="white",command=delete)
            delete.place(x=70,y=190)

            update = Button(rt3,text="update",font=("italic",10),bg="white",command=update)
            update.place(x=120,y=190)

            get = Button(rt3,text="get",font=("italic",10),bg="white",command=get)
            get.place(x=170,y=190)

            
            list =Listbox(rt3,width=45,height=45)
            list.place(x=290,y=30)
            show()
            rt3.mainloop


        def course():
            def get():
                if(e_course_id.get()==""):
                    MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY TO FETCH")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("select * from course where course_id ='" + e_course_id.get()+"'")
                    #command_handler.execute("commit")
                    rows = command_handler.fetchall()
                    if rows:
                        for row in rows:
                            
                            e_title.insert(0,row[1])
                            e_dept_name4.insert(0,row[2])
                            e_credits.insert(0,row[3])
                    MessageBox.showinfo("FETCH STATUS","FETCHED SUCCESSFULLY")
                    db.close()
            def update():
                course_id = e_course_id.get()
                title = e_title.get()
                dept_name4 = e_dept_name4.get()
                credits= e_credits.get()
                if(course_id=="" or title =="" or dept_name4=="" or credits==""):
                    MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("UPDATE course set title='"+ title +"', dept_name='"+dept_name4  +"',credits='"+ credits +"'where course_id ='"+ course_id +"'")
                    command_handler.execute("commit")
                    e_course_id.delete(0,"end")
                    e_title.delete(0,"end")
                    e_dept_name4.delete(0,"end")
                    e_credits.delete(0,"end") 
                    show()
                    MessageBox.showinfo("UPDATE STATUS","UPDATED SUCCESSFULLY")
                    db.close()
            def delete():
                if(e_course_id.get()==""):
                    MessageBox.showinfo("DELETE STATUS"," Course ID IS COMPULSORY TO DELETE")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("delete from course where id='"+ e_course_id.get() +"'")
                    command_handler.execute("commit")
                    e_course_id.delete(0,"end")
                    e_title.delete(0,"end")
                    e_dept_name4.delete(0,"end")
                    e_credits.delete(0,"end")   
                    show()   
                    MessageBox.showinfo("DELETE STATUS","DELETED SUCCESSFULLY")
                    db.close()
            def insert():
                course_id = e_course_id.get()
                title = e_title.get()
                dept_name4 = e_dept_name4.get()
                credits= e_credits.get()

                if(course_id=="" or title=="" or dept_name4 =="" or credits==""):
                    MessageBox.showinfo("INSERT STATUS","INSERT ALL FIELDS")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("insert into course values('"+course_id+"','"+title+"','"+dept_name4+"','"+credits+"')")
                    command_handler.execute("commit")
                    show()
                    MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY")
                    db.close()
            def show():
                db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                command_handler = db.cursor(buffered=True)
                command_handler.execute("select * from course")
                rows = command_handler.fetchall()
                list.delete(0,list.size())
                for row in rows:
                    insertData = str(row[0])+'     '+row[1]+'    '+row[2]+'    '+str(row[3])
                    list.insert(list.size()+1,insertData)
                db.close()
        

            rt4 = Tk()
            rt4.geometry("600x600")
            rt4.title("COURSE_PORTAL")
            rt4.configure(bg='darkorchid')

   
            course_id = Label(rt4,text='Enter Course_ID',font=('bold',10))
            course_id.place(x=20,y=30)

            e_course_id =Entry(rt4)
            e_course_id.place(x=150,y=30)

            title= Label(rt4,text='Enter Title',font=('bold',10))
            title.place(x=20,y=60)

            e_title =Entry(rt4)
            e_title.place(x=150,y=60)


            dept_name4 = Label(rt4,text='Department Name',font=('bold',10))
            dept_name4.place(x=20,y=90)

            e_dept_name4 =Entry(rt4)
            e_dept_name4.place(x=150,y=90)

            credits = Label(rt4,text='Total Credit',font=('bold',10))
            credits.place(x=20,y=120)

            e_credits =Entry(rt4)
            e_credits.place(x=150,y=120)


        
            insert = Button(rt4,text="insert",font=("italic",10),bg="white",command=insert)
            insert.place(x=20,y=190)

            delete = Button(rt4,text="delete",font=("italic",10),bg="white",command=delete)
            delete.place(x=70,y=190)

            update = Button(rt4,text="update",font=("italic",10),bg="white",command=update)
            update.place(x=120,y=190)

            get = Button(rt4,text="get",font=("italic",10),bg="white",command=get)
            get.place(x=170,y=190)

            
            list =Listbox(rt4,width=45,height=45)
            list.place(x=290,y=30)
            show()
            rt4.mainloop

        def contact_us():
            def show():
                msg1 = Label(rt5,text='FOR ANY QUERIES CONTACT',font=('bold',30))
                msg1.place(x=20,y=90)
                msg2 = Label(rt5,text='DIRECTOR:9527129211',font=('bold',30))
                msg2.place(x=100,y=200)
                msg3 = Label(rt5,text='DEAN:9890724611',font=('bold',30))
                msg3.place(x=100,y=250)

                
            rt5 = Tk()
            rt5.geometry("600x600")
            rt5.title("CONTACT US")
            rt5.configure(bg='orangered')
            show()
            rt5.mainloop


        def library():
            def get():
                if(e_id.get()==""):
                    MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY TO FETCH")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("select * from library where id ='" + e_id.get()+"'")
                    #command_handler.execute("commit")
                    rows = command_handler.fetchall()
                    if rows:
                        for row in rows:
                            e_Name.insert(0,row[0])
                            e_Issue_type.insert(0,row[2])
                            e_date.insert(0,row[3])
                    MessageBox.showinfo("FETCH STATUS","FETCHED SUCCESSFULLY")
                    db.close()
            def update():
                Name = e_Name.get()
                id = e_id.get()
                Issue_type = e_Issue_type.get()
                date = e_date.get()

                if(id=="" or Name =="" or Issue_type =="" or date==""):
                    MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("UPDATE library set name='"+ Name +"', date='"+ date +"',Issue_type='"+ Issue_type +"'where id ='"+ id +"'")
                    command_handler.execute("commit")
                    e_id.delete(0,"end")
                    e_Name.delete(0,"end")
                    e_Issue_type.delete(0,"end")
                    e_date.delete(0,"end")
                    MessageBox.showinfo("UPDATE STATUS","UPDATED SUCCESSFULLY")
                    db.close()
            def delete():
                if(e_id.get()==""):
                    MessageBox.showinfo("DELETE STATUS","ID IS COMPULSORY TO DELETE")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("delete from library where id='"+ e_id.get() +"'")
                    command_handler.execute("commit")
                    e_id.delete(0,"end")
                    e_Name.delete(0,"end")
                    e_Issue_type.delete(0,"end")
                    e_date.delete(0,"end")   
                    show()   
                    MessageBox.showinfo("DELETE STATUS","DELETED SUCCESSFULLY")
                    db.close()
            def insert():
                Name = e_Name.get()
                id = e_id.get()
                Issue_type = e_Issue_type.get()
                date = e_date.get()

                if(id=="" or Name =="" or Issue_type =="" or date==""):
                    MessageBox.showinfo("INSERT STATUS","INSERT ALL FIELDS")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("insert into library values('"+Name+"','"+id+"','"+Issue_type+"','"+date+"')")
                    command_handler.execute("commit")
                    show()
                    MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY")
                    db.close()
            def show():
                db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                command_handler = db.cursor(buffered=True)
                command_handler.execute("select * from library")
                rows = command_handler.fetchall()
                list.delete(0,list.size())
                for row in rows:
                    insertData = str(row[0])+'     '+row[1]+'    '+row[2]+'    '+str(row[3])
                    list.insert(list.size()+1,insertData)
                db.close()
        

            rt5 = Tk()
            rt5.geometry("600x600")
            rt5.title("LIBRARY_PORTAL")
            rt5.configure(bg='purple')

   
            Name= Label(rt5,text='Enter Name',font=('bold',10))
            Name.place(x=20,y=30)

            e_Name =Entry(rt5)
            e_Name.place(x=150,y=30)

            id = Label(rt5,text='Enter ID',font=('bold',10))
            id.place(x=20,y=60)

            e_id =Entry(rt5)
            e_id.place(x=150,y=60)


            Issue_type = Label(rt5,text='Issue Type',font=('bold',10))
            Issue_type.place(x=20,y=90)

            e_Issue_type =Entry(rt5)
            e_Issue_type.place(x=150,y=90)

            date = Label(rt5,text='Date',font=('bold',10))
            date.place(x=20,y=120)

            e_date=Entry(rt5)
            e_date.place(x=150,y=120)


        
            insert = Button(rt5,text="insert",font=("italic",10),bg="white",command=insert)
            insert.place(x=20,y=190)

            delete = Button(rt5,text="delete",font=("italic",10),bg="white",command=delete)
            delete.place(x=70,y=190)

            update = Button(rt5,text="update",font=("italic",10),bg="white",command=update)
            update.place(x=120,y=190)

            get = Button(rt5,text="get",font=("italic",10),bg="white",command=get)
            get.place(x=170,y=190)

            
            list =Listbox(rt5,width=45,height=45)
            list.place(x=290,y=30)
            show()
            rt5.mainloop


        def student():
            def get():
                if(e_id.get()==""):
                    MessageBox.showinfo("FETCH STATUS","ID IS COMPULSORY TO FETCH")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("select * from student where id ='" + e_id.get()+"'")
                    #command_handler.execute("commit")
                    rows = command_handler.fetchall()
                    if rows:
                        for row in rows:
                            e_Name.insert(0,row[1])
                            e_dept_name.insert(0,row[2])
                            e_tot_credit.insert(0,row[3])
                    MessageBox.showinfo("FETCH STATUS","FETCHED SUCCESSFULLY")
                    db.close()
            def update():
                id = e_id.get()
                Name = e_Name.get()
                dept_name = e_dept_name.get()
                tot_credit = e_tot_credit.get()
                if(id=="" or Name =="" or dept_name =="" or tot_credit==""):
                    MessageBox.showinfo("UPDATE STATUS","ALL FIELDS ARE REQUIRED")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("UPDATE student set name='"+ Name +"', dept_name='"+ dept_name +"',tot_credit='"+ tot_credit +"'where id ='"+ id +"'")
                    command_handler.execute("commit")
                    e_id.delete(0,"end")
                    e_Name.delete(0,"end")
                    e_dept_name.delete(0,"end")
                    e_tot_credit.delete(0,"end")
                    show()
                    MessageBox.showinfo("UPDATE STATUS","UPDATED SUCCESSFULLY")
                    db.close()
            def delete():
                if(e_id.get()==""):
                    MessageBox.showinfo("DELETE STATUS","ID IS COMPULSORY TO DELETE")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("delete from student where id='"+ e_id.get() +"'")
                    command_handler.execute("commit")
                    e_id.delete(0,"end")
                    e_Name.delete(0,"end")
                    e_dept_name.delete(0,"end")
                    e_tot_credit.delete(0,"end")   
                    show()   
                    MessageBox.showinfo("DELETE STATUS","DELETED SUCCESSFULLY")
                    db.close()
            def insert():
                id = e_id.get()
                Name = e_Name.get()
                dept_name = e_dept_name.get()
                tot_credit = e_tot_credit.get()

                if(id=="" or Name =="" or dept_name =="" or tot_credit==""):
                    MessageBox.showinfo("INSERT STATUS","INSERT ALL FIELDS")
                else:
                    db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                    command_handler = db.cursor(buffered=True)
                    command_handler.execute("insert into student values('"+id+"','"+Name+"','"+dept_name+"','"+tot_credit+"')")
                    command_handler.execute("commit")
                    show()
                    MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY")
                    db.close()
            def show():
                db = mysql.connect(host="localhost",user="root",password="",database="college_management_system")
                command_handler = db.cursor(buffered=True)
                command_handler.execute("select * from student")
                rows = command_handler.fetchall()
                list.delete(0,list.size())
                for row in rows:
                    insertData = str(row[0])+'     '+row[1]+'    '+row[2]+'    '+str(row[3])
                    list.insert(list.size()+1,insertData)
                db.close()
        

            rt1 = Tk()
            rt1.geometry("600x600")
            rt1.title("STUDENT_PORTAL")
            rt1.configure(bg='goldenrod')

   
            id = Label(rt1,text='Enter ID',font=('bold',10))
            id.place(x=20,y=30)

            e_id =Entry(rt1)
            e_id.place(x=150,y=30)

            Name = Label(rt1,text='Enter Name',font=('bold',10))
            Name.place(x=20,y=60)

            e_Name =Entry(rt1)
            e_Name.place(x=150,y=60)


            dept_name = Label(rt1,text='Department Name',font=('bold',10))
            dept_name.place(x=20,y=90)

            e_dept_name =Entry(rt1)
            e_dept_name.place(x=150,y=90)

            tot_credit = Label(rt1,text='Total Credit',font=('bold',10))
            tot_credit.place(x=20,y=120)

            e_tot_credit =Entry(rt1)
            e_tot_credit.place(x=150,y=120)


        
            insert = Button(rt1,text="insert",font=("italic",10),bg="white",command=insert)
            insert.place(x=20,y=190)

            delete = Button(rt1,text="delete",font=("italic",10),bg="white",command=delete)
            delete.place(x=70,y=190)

            update = Button(rt1,text="update",font=("italic",10),bg="white",command=update)
            update.place(x=120,y=190)

            get = Button(rt1,text="get",font=("italic",10),bg="white",command=get)
            get.place(x=170,y=190)

            
            list =Listbox(rt1,width=45,height=45)
            list.place(x=290,y=30)
            show()
            rt1.mainloop


    
        rt = Tk()
        rt.geometry("1000x1000")
        rt.title("COLLEGE_MANAGEMENT_SYSTEM")
        rt.configure(bg='#856ff8')
    
   


        msg = Label(rt,text='WELCOME TO THE COLLEGE MANAGEMENT SYSTEM',font=('bold',30))
        msg.place(x=20,y=90)

        student = Button(rt,text="STUDENT",bg="yellow",font=("italic",20),command = student)
        student.place(x=20, y=300)

        faculty= Button(rt,text="FACULTY",bg="yellow",font=("italic",20),command = faculty)
        faculty.place(x=20, y=400)

        course = Button(rt,text="COURSE",bg="yellow",font=("italic",20),command = course)
        course.place(x=20, y=500)

        library = Button(rt,text="LIBRARY",bg="yellow",font=("italic",20),command = library)
        library.place(x=500, y=500)

        department = Button(rt,text="DEPARTMENT",bg="yellow",font=("italic",20),command = department)
        department.place(x=500, y=400)

        contact = Button(rt,text="CONTACT US",bg="yellow",font=("italic",20),command = contact_us)
        contact.place(x=500, y=300)


        rt.mainloop()

root = Tk()
root.geometry("400x400")
root.title("LOGIN_PAGE")
root.configure(bg='green')


username = Label(root,text='Username',font=('bold',10),bg='pink')
username.place(x=20,y=60)

password = Label(root,text='Password',font=('bold',10),bg='pink')
password.place(x=20,y=90)

e_username = Entry()
e_username.place(x=150,y=60)

e_password = Entry()
e_password.place(x=150,y=90)


Login = Button(root,text="LOGIN",bg="yellow",font=("italic",20),command = login)
Login.place(x=70, y=140)

root.mainloop()
