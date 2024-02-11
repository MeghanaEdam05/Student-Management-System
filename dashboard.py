from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from results import resultClass
from report import reportClass

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1330x700+0+0")
        self.root.config(bg="white")
        #====icons=====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo1.jpg")
        #====title=====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #====menu=====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1265,height=80)

         
        #====button=====
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=10,y=4,width=190,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=215,y=4,width=190,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=430,y=4,width=190,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=640,y=4,width=190,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=850,y=4,width=190,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1070,y=4,width=190,height=40)
         
        #===content_window===
        self.bg_img=Image.open("images/bg.jpg")
        self.bg_img=self.bg_img.resize((900,300))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=900,height=300)

        #====update====
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy ols style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white").place(x=400,y=490,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy ols style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white").place(x=710,y=490,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy ols style",20),bd=10,relief=RIDGE,bg="#038074",fg="white").place(x=1020,y=490,width=300,height=100)
        
        #====footer=====
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issue: 9985xxxx53",font=("goudy old style",15),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


    def add_course(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=CourseClass(self.new_win) 

    def add_student(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=studentClass(self.new_win)     
    
    def add_result(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=reportClass(self.new_win)     

if __name__ == '__main__':
    root=Tk()
    obj=RMS(root)
    root.mainloop()
