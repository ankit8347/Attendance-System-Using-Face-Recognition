from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog




mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =====================Variables=========================


        self.var_atten_id         = StringVar()
        self.var_atten_roll       = StringVar()
        self.var_atten_name       = StringVar() 
        self.var_atten_dep        = StringVar()
        self.var_atten_time       = StringVar() 
        self.var_atten_date       = StringVar() 
        self.var_atten_attendance = StringVar()

# frist image
        img1 = Image.open(r"Main_Images\attendance_1.jpeg")
        img1 = img1.resize((1530,200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_1 = Label(self.root,image=self.photoimg1)
        label_1.place(x=0,y=0,width=1530,height=200)
# # 2nd image
#         img2 = Image.open(r"Main_Images\attendance_1.jpeg")
#         img2 = img2.resize((800,200))
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         label_2 = Label(self.root,image=self.photoimg2)
#         label_2.place(x=800,y=0,width=800,height=200)


# bg image
        img4 = Image.open(r"Main_Images\attendance_1.jpeg")
        img4 = img4.resize((1530,710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=('times new roman',35,"bold"),bg='white',fg='darkorchid3')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        # ------------------------Left frame-------------------------------


        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)


        img_left = Image.open(r"Main_Images\attendance_2.jpeg")
        img_left = img_left.resize((720,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        label_left = Label(Left_frame,image=self.photoimg_left)
        label_left.place(x=5,y=0,width=720,height=130) 


        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=735,height=422)


        # ------------------------------Lable and entry-------------------------

       # Attendance ID
       
        AttendanceID_label = Label(left_inside_frame,text="Attendance ID       :",font=("time new roman",13,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("time new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll No

        Roll_no_label = Label(left_inside_frame,text="Roll No           :     ",font=("time new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry = ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=("time new roman",13,"bold"))
        Roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Name
        Name_label = Label(left_inside_frame,text="Name                    :",font=("time new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("time new roman",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Department
        Department_label = Label(left_inside_frame,text="Department    :     ",font=("time new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Department_entry = ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("time new roman",13,"bold"))
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W) 


        # Time
        Time_label = Label(left_inside_frame,text="Time                     :",font=("time new roman",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("time new roman",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)  


        # date
        Date_label = Label(left_inside_frame,text="Date               :",font=("time new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry = ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=("time new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Attencdance

        Attendance_Lable = Label(left_inside_frame,text="Attendance Status    :",bg='white',font='comicsansns 11 bold')
        Attendance_Lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.attend_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state='readonly')
        self.attend_status["values"] = ("Status","Present","Absent")
        self.attend_status.grid(row=3,column=1,pady=8)
        self.attend_status.current(0)


        # Button Frame
        Button_frame_2 = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame_2.place(x=0,y=300,width=715,height=30)

        # Import Button
        Import_Button = Button(Button_frame_2,text="Import csv",command=self.open_csv,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        Import_Button.grid(row=0,column=0)

        # Export Button
        Export_Button = Button(Button_frame_2,text="Export csv",width=17,command=self.exportCsv,font=("time new roman",13,"bold"),bg="blue",fg="white")
        Export_Button.grid(row=0,column=1)
        
        # # Update Button
        # update_Button = Button(Button_frame_2,text="Update",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        # update_Button.grid(row=0,column=2)


        # Reset Button
        reset_Button = Button(Button_frame_2,text="Reset",command=self.reset_data,width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_Button.grid(row=0,column=3)



        



        # -----------------------Right label frame-----------------------------

        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)



        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=550)


        # ---------------------scroll bar table------------------------------

        Scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.Attendance_Report_Table = ttk.Treeview(table_frame,columns=("Id","Roll_no","Name",'Departmenat',"time","date","attendance"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)


        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)




        Scroll_x.config(command=self.Attendance_Report_Table.xview)
        Scroll_y.config(command=self.Attendance_Report_Table.yview)



        self.Attendance_Report_Table.heading("Id",text='Student_ID')            # 1
        self.Attendance_Report_Table.heading("Roll_no",text='Roll_no')          # 2
        self.Attendance_Report_Table.heading("Name",text='Student_Name')        # 3
        self.Attendance_Report_Table.heading("Departmenat",text='Departmenat')  # 4
        self.Attendance_Report_Table.heading("time",text='Time')  # 5
        self.Attendance_Report_Table.heading("date",text='Date')  # 6
        self.Attendance_Report_Table.heading("attendance",text='Attendance')  # 7

        self.Attendance_Report_Table["show"] = "headings"   # to remove space


        # --------------width set----------------------------------------

        self.Attendance_Report_Table.column("Id",width=100)            # 1
        self.Attendance_Report_Table.column("Roll_no",width=100)       # 2
        self.Attendance_Report_Table.column("Name",width=100)          # 3
        self.Attendance_Report_Table.column("Departmenat",width=100)   # 4
        self.Attendance_Report_Table.column("time",width=100)          # 5
        self.Attendance_Report_Table.column("date",width=100)          # 6
        self.Attendance_Report_Table.column("attendance",width=100)    # 7 


        self.Attendance_Report_Table.pack(fill=BOTH,expand=1)

        self.Attendance_Report_Table.bind("<ButtonRelease>",self.get_cursor)


        # --------------------------fecth data-----------------------------------------


    def fetchData(self,rows):
      self.Attendance_Report_Table.delete(*self.Attendance_Report_Table.get_children())
      for i in rows:
        self.Attendance_Report_Table.insert("",END,values=i)

    def open_csv(self):
      global mydata
      mydata.clear()
      file_path = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File,","*.csv"),("All Files","*.*")),parent=self.root)
      with open(file_path) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)



        # -------------------Export csv Data----------------------------------------------------
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No Data found to export",parent=self.root)
          return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File,","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write = csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your Data is Exported to"+os.path.basename(fln)+"Successfully")
      except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


        # get cursor take data

    def get_cursor(self,event=""):
      cursor_row = self.Attendance_Report_Table.focus()
      content = self.Attendance_Report_Table.item(cursor_row)
      rows = content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])



        # Reset data

    def reset_data(self):
       
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")
        

       











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()