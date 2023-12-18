from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



# ==========================Variable==================================

        self.var_dep          = StringVar()
        self.var_course       = StringVar()                                    
        self.var_Year         = StringVar()    
        self.var_Sem          = StringVar()           
        self.var_Stdid        = StringVar()           
        self.var_std_name     = StringVar()            
        self.var_div          = StringVar()            
        self.var_roll_no      = StringVar()                
        self.var_Gender       = StringVar()                
        self.var_DOB          = StringVar()                
        self.var_Email        = StringVar()                  
        self.var_Phone        = StringVar()                   
        self.var_Address      = StringVar()                   
        self.var_Teacher_name = StringVar()                



# frist image
        img1 = Image.open(r"Main_Images\bg1.jpeg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_1 = Label(self.root,image=self.photoimg1)
        label_1.place(x=0,y=0,width=500,height=130)
# 2nd image
        img2 = Image.open(r"Main_Images\bg3.jpeg")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_2 = Label(self.root,image=self.photoimg2)
        label_2.place(x=500,y=0,width=500,height=130)



# 3rd image
        img3 = Image.open(r"Main_Images\bg2.jpeg")
        img3 = img3.resize((550,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label_3 = Label(self.root,image=self.photoimg3)
        label_3.place(x=1000,y=0,width=550,height=130)

# bg image
        img4 = Image.open(r"Main_Images\background.jpg")
        img4 = img4.resize((1530,710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=('times new roman',35,"bold"),bg='blue',fg='white')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)


        #======================== Left label frame =============================================

        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"Main_Images\bg2.jpeg")
        img_left = img_left.resize((720,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        label_left = Label(Left_frame,image=self.photoimg_left)
        label_left.place(x=5,y=0,width=720,height=130)  

        # ======================= Current Course frame ==========================================
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infromation",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)
        
        # Departmenat label
        dep_label = Label(current_course_frame,text="Department :",font=("time new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",10,"bold"),state='readonly',width=20)
        dep_combo["values"] = ("Select Department" ,"M.Sc.IT","B.Sc.IT + M.Sc.IT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course label

        Course_label = Label(current_course_frame,text="Course    :",font=("time new roman",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",10,"bold"),state='readonly',width=40)
        Course_combo["values"] = ("Select Course" , "M.Sc. IT in Business Intelligence & Analytics",
 "M.Sc. IT in Game Design & Development",
 "M.Sc. IT in Mobile App & UI Development",
 "M.Sc. IT in IMS and Cloud Technology",
 "M.Sc. IT in Animation & VFX",
 "M.Sc. IT in Network Security",
 "M.Sc. IT in FinTech")        
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year label
        Year_label = Label(current_course_frame,text="Year            :",font=("time new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        Year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("time new roman",10,"bold"),state='readonly',width=20)
        Year_combo["values"] = ("Select Year" ,"2020-2021","2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester label
        Semester_label = Label(current_course_frame,text="Semester :",font=("time new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("time new roman",10,"bold"),state='readonly',width=40)
        Semester_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student Infromation frame
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Infromation",font=("time new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=720,height=290)

       # Student ID 
        StudentID_label = Label(class_Student_frame,text="Student ID      :",font=("time new roman",13,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Stdid,font=("time new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

       # Student Name
        Student_Name_label = Label(class_Student_frame,text="Student Name   :",font=("time new roman",13,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Student_Name_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("time new roman",13,"bold"))
        Student_Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


       # Class Division
        Class_div_label = Label(class_Student_frame,text="Class Division :",font=("time new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("time new roman",13,"bold"),state='readonly',width=18)
        class_div_combo["values"] = ("A" ,"B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


       # Roll No
        Roll_no_label = Label(class_Student_frame,text="Roll No              :",font=("time new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll_no,font=("time new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


       # Gender
        Student_gender_label = Label(class_Student_frame,text="Gender           :",font=("time new roman",13,"bold"),bg="white")
        Student_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_Gender,font=("time new roman",13,"bold"),state='readonly',width=18)
        gender_combo["values"] = ("Male" ,"Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


       # Date of Birth
        Student_dob_label = Label(class_Student_frame,text="DOB                  :",font=("time new roman",13,"bold"),bg="white")
        Student_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Student_dob_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_DOB,font=("time new roman",13,"bold"))
        Student_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


       # Email
        Student_email_label = Label(class_Student_frame,text="Email              :",font=("time new roman",13,"bold"),bg="white")
        Student_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Student_email_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Email,font=("time new roman",13,"bold"))
        Student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


       # Phone No
        Student_Phone_label = Label(class_Student_frame,text="Phone No          :",font=("time new roman",13,"bold"),bg="white")
        Student_Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Student_Phone_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Phone,font=("time new roman",13,"bold"))
        Student_Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


       # Address
        Student_address_label = Label(class_Student_frame,text="Address         :",font=("time new roman",13,"bold"),bg="white")
        Student_address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Student_address_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Address,font=("time new roman",13,"bold"))
        Student_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


       # Teacher name
        Teacher_Name_label = Label(class_Student_frame,text="Teacher Name   :",font=("time new roman",13,"bold"),bg="white")
        Teacher_Name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_Name_entry = ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Teacher_name,font=("time new roman",13,"bold"))
        Teacher_Name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)




        # radio Button

        self.var_radio1 = StringVar()
        radio_button_1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_button_1.grid(row=6,column=0)

        radio_button_2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_button_2.grid(row=6,column=1)

        # Button Frame
        Button_frame_2 = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame_2.place(x=0,y=200,width=715,height=30)

        # Save Button
        save_Button = Button(Button_frame_2,text="Save",command=self.add_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_Button.grid(row=0,column=0)

        # Update Button
        update_Button = Button(Button_frame_2,text="Update",command=self.update_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_Button.grid(row=0,column=1)

        # Delete Button
        delete_Button = Button(Button_frame_2,text="Delete",command=self.delete_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        delete_Button.grid(row=0,column=2)

        # Reset Button
        reset_Button = Button(Button_frame_2,text="Reset",command=self.reset_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_Button.grid(row=0,column=3)

        Button_frame_3 = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame_3.place(x=0,y=235,width=715,height=50)


# Take Photo Sample
        take_photo_Button = Button(Button_frame_3,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        take_photo_Button.grid(row=1,column=0)
# Update Photo Sample
        update_photo_Button = Button(Button_frame_3,command=self.generate_Update_dataset,text="Update Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_photo_Button.grid(row=1,column=1)



        # Right label frame

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right = Image.open(r"C:\Users\Lenovo\Python\CapStone_ Project\Main_Images\bg2.jpeg")
        img_right = img_right.resize((720,130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        label_right = Label(Right_frame,image=self.photoimg_right)
        label_right.place(x=5,y=0,width=720,height=130)

# ========================Serach System===================================================
       # Search Frame
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

      # Search label
        Search_label = Label(Search_frame,text="Search By:",font=("time new roman",15,"bold"),bg="red",fg='white')
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

     # Search Combo Button
        Search_combo = ttk.Combobox(Search_frame,font=("time new roman",10,"bold"),state='readonly',width=15)
        Search_combo["values"] = ("Select","Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


     # Search entry
        Search_entry = ttk.Entry(Search_frame,width=15,font=("time new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


    #  # Search Button

    #     Search_Button_1 = Button(Search_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
    #     Search_Button_1.grid(row=0,column=3,padx=4)

    # # Show All Buttton
    #     Show_All_Button = Button(Search_frame,text="Show All",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
    #     Show_All_Button.grid(row=0,column=4,padx=4)

       # ===============Table Frame==================================
        Table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=345)

        Scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
    
        self.student_table = ttk.Treeview(Table_frame,columns=('Departmenat','Course','Year','Semester',"Id","Name","Division","Roll_no",'Gender','DOB',"Email",'Phone','Address','Teacher','Photo'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Departmenat",text='Departmenat')  # 1
        self.student_table.heading("Course",text='Course')            # 2
        self.student_table.heading("Year",text='Year')                # 3
        self.student_table.heading("Semester",text='Semester')        # 4
        self.student_table.heading("Id",text='Student_ID')            # 5
        self.student_table.heading("Name",text='Student_Name')        # 6
        self.student_table.heading("Division",text='Division')        # 7
        self.student_table.heading("Roll_no",text='Roll_no')          # 8
        self.student_table.heading("Gender",text='Gender')            # 9
        self.student_table.heading("DOB",text='DOB')                  # 10
        self.student_table.heading("Email",text='Email')              # 11
        self.student_table.heading("Phone",text='Phone_no')           # 12
        self.student_table.heading("Address",text='Address')          # 13
        self.student_table.heading("Teacher",text='Teacher_Name')     # 14
        self.student_table.heading("Photo",text='PhotoSampleStatus')              # 15
        
        self.student_table['show'] = 'headings'


        self.student_table.column("Departmenat",width=90)  # 1
        self.student_table.column("Course",width=90)        # 2
        self.student_table.column("Year",width=90)          # 3
        self.student_table.column("Semester",width=90)       # 4
        self.student_table.column("Id",width=80)            # 5
        self.student_table.column("Name",width=90)          # 6
        self.student_table.column("Division",width=90)      # 7
        self.student_table.column("Roll_no",width=70)       # 8
        self.student_table.column("Gender",width=90)        # 9
        self.student_table.column("DOB",width=70)           # 10
        self.student_table.column("Email",width=90)         # 11
        self.student_table.column("Phone",width=90)         # 12
        self.student_table.column("Address",width=90)       # 13
        self.student_table.column("Teacher",width=90)       # 14
        self.student_table.column("Photo",width=100) 

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fecth_data()


    def add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()=='' or self.var_Stdid.get()=='':
            messagebox.showerror("Error","All filed required",parent=self.root)

        else:
            try:

                my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                my_cursor = my_db.cursor()

                my_cursor.execute("Insert into student_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_Year.get(),
                                                                                                                        self.var_Sem.get(),
                                                                                                                        self.var_Stdid.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll_no.get(),
                                                                                                                        self.var_Gender.get(),
                                                                                                                        self.var_DOB.get(),
                                                                                                                        self.var_Email.get(),
                                                                                                                        self.var_Phone.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_Teacher_name.get(),
                                                                                                                        self.var_radio1.get()                    
                                                                                                                                     
                                                                                                                  ))
                my_db.commit()
                self.fecth_data()
                my_db.close()
                messagebox.showinfo("Sucess","Student details has added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # -----------------------------------------------------fetchall data from databases----------------------------------------------------------------
   
    def fecth_data(self):
        my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
        my_cursor = my_db.cursor()

        my_cursor.execute("Select * from student_info")
        data = my_cursor.fetchall()

        if len(data) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                my_db.commit()
        my_db.close()


   # ---------------------- get curosr --------------------------------------------------------------------------------------------------

    def get_cursor(self,event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_Stdid.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll_no.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher_name.set(data[13]),
        self.var_radio1.set(data[14])

# ================================= Update_data ===============================================================
    def update_data(self,event=''):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()=='' or self.var_Stdid.get()=='':
            messagebox.showerror("Error","All filed required",parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this Student deatails",parent=self.root)
                if Update > 0:
                    my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                    my_cursor = my_db.cursor()

                    my_cursor.execute("Update student_info SET Departmenat=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where Id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_Year.get(),
                                                                                                                        self.var_Sem.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll_no.get(),
                                                                                                                        self.var_Gender.get(), 
                                                                                                                        self.var_DOB.get(),
                                                                                                                        self.var_Email.get(),
                                                                                                                        self.var_Phone.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_Teacher_name.get(),
                                                                                                                        self.var_radio1.get(),                    
                                                                                                                        self.var_Stdid.get()
  
                                                                                                                  ))
                
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Student details has added Successfully",parent=self.root)

                my_db.commit()
                self.fecth_data()
                my_db.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


# ------------------------------Delete function-----------------------------------


    def delete_data(self):
        if self.var_Stdid.get()=='':
            messagebox.showerror("Error","Student id Must be required",parent=self.root)

        else:
            try:
                delete = messagebox.askyesno("Delete Page","Do You want to delete this student detail",parent=self.root)
                if delete>0:
                    my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                    my_cursor = my_db.cursor()
                    sql = "Delete from student_info where Id=%s"
                    val = (self.var_Stdid.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                
                my_db.commit()
                self.fecth_data()
                my_db.close()

                messagebox.showinfo("Delete","Successfully deleted student deatails",parent=self.root)


            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


# -----------------------------Reset function------------------------------------------------------------

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Selete Course"),
        self.var_Year.set("Selete Year"),
        self.var_Sem.set("Selete Semester"),
        self.var_Stdid.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll_no.set(""),
        self.var_Gender.set("Male"),
        self.var_DOB.set(""),
        self.var_Email.set(""),
        self.var_Phone.set(""),
        self.var_Address.set(""),
        self.var_Teacher_name.set(""),
        self.var_radio1.set("")

                
# ---------------------Generate data set Take photo Smaples-------------------------------------

    def generate_dataset(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()=='' or self.var_Stdid.get()=='':
            messagebox.showerror("Error","All filed required",parent=self.root)

        else:
            try:

                my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                my_cursor = my_db.cursor()
                my_cursor.execute("Select * from student_info")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    
                my_cursor.execute("Update student_info SET Departmenat=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where Id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_Year.get(),
                                                                                                                        self.var_Sem.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll_no.get(),
                                                                                                                        self.var_Gender.get(), 
                                                                                                                        self.var_DOB.get(),
                                                                                                                        self.var_Email.get(),
                                                                                                                        self.var_Phone.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_Teacher_name.get(),
                                                                                                                        self.var_radio1.get(),                    
                                                                                                                        self.var_Stdid.get()==id+1
  
                                                                                                                  ))
                
                my_db.commit()
                self.fecth_data()
                self.reset_data()
                my_db.close


                # -------------------------Load predifiend data on face frontals from opencv-----------------------------------------------------------

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)

                    #scaling factor = 1.3
                    #Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
            

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1
            
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2BGRA)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:    # photo capture 
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def generate_Update_dataset(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()=='' or self.var_Stdid.get()=='':
            messagebox.showerror("Error","All filed required",parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this Student deatails",parent=self.root)
                if Update > 0:

                    my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                    my_cursor = my_db.cursor()
                    my_cursor.execute("Select * from student_info")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    
                    my_cursor.execute("Update student_info SET Departmenat=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where Id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_Year.get(),
                                                                                                                        self.var_Sem.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll_no.get(),
                                                                                                                        self.var_Gender.get(), 
                                                                                                                        self.var_DOB.get(),
                                                                                                                        self.var_Email.get(),
                                                                                                                        self.var_Phone.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_Teacher_name.get(),
                                                                                                                        self.var_radio1.get(),                    
                                                                                                                        self.var_Stdid.get()==id+1
  
                                                                                                                  ))
                
                    my_db.commit()
                    self.fecth_data()
                    self.reset_data()
                    my_db.close


                # -------------------------Load predifiend data on face frontals from opencv-----------------------------------------------------------

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)

                    #scaling factor = 1.3
                    #Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
            

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1
            
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2BGRA)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:    # photo capture 
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



            










if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()