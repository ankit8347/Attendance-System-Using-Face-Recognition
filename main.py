from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from trian import Trian
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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


        title_lbl = Label(bg_img,text="FACE RECOGNITION SYSTEM",font=('times new roman',35,"bold"),bg='white',fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)


# 1. student button
        img_1 = Image.open(r"Main_Images\button1.jpeg")
        img_1 = img_1.resize((220,220))
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        b1 = Button(bg_img,command=self.student_details,image = self.photoimg_1,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b_1 = Button(bg_img,command=self.student_details,text = "Student Details",cursor='hand2',font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_1.place(x=200,y=300,width=220,height=40)

# 2. Detect Face button
        img_2 = Image.open(r"Main_Images\button2.jpeg")
        img_2 = img_2.resize((220,220))
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        b1 = Button(bg_img,image = self.photoimg_2,cursor='hand2',command=self.face_data)
        b1.place(x=650,y=100,width=220,height=220)

        b_2 = Button(bg_img,text = "Face Detector",cursor='hand2',command=self.face_data,font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_2.place(x=650,y=300,width=220,height=40)

# 3. Attendace  button
        img_3 = Image.open(r"Main_Images\button3.jpeg")
        img_3 = img_3.resize((220,220))
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        b1 = Button(bg_img,image = self.photoimg_3,cursor='hand2',command=self.attendance_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b_3 = Button(bg_img,text = "Attendace",cursor='hand2',command=self.attendance_data,font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_3.place(x=1100,y=300,width=220,height=40)

# # 4. help  button
#         img_4 = Image.open(r"Main_Images\button4.jpeg")
#         img_4 = img_4.resize((220,220))
#         self.photoimg_4 = ImageTk.PhotoImage(img_4)

#         b1 = Button(bg_img,image = self.photoimg_4,cursor='hand2')
#         b1.place(x=1100,y=100,width=220,height=220)

#         b_4 = Button(bg_img,text = "Help Desk",cursor='hand2',font=('times new roman',15,"bold"),bg='darkblue',fg='white')
#         b_4.place(x=1100,y=300,width=220,height=40)


# 5. Train button
        img_5 = Image.open(r"Main_Images\button5.jpeg")
        img_5 = img_5.resize((220,220))
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        b1 = Button(bg_img,image = self.photoimg_5,cursor='hand2',command=self.trian_data)
        b1.place(x=200,y=380,width=220,height=220)

        b_5 = Button(bg_img,text = "Train Data",cursor='hand2',command=self.trian_data,font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_5.place(x=200,y=580,width=220,height=40)

# 6. Photo button
        img_6 = Image.open(r"Main_Images\button6.jpeg")
        img_6 = img_6.resize((220,220))
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        b1 = Button(bg_img,image = self.photoimg_6,cursor='hand2',command=self.open_img)
        b1.place(x=650,y=380,width=220,height=220)

        b_6 = Button(bg_img,text = "Photo",cursor='hand2',command=self.open_img,font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_6.place(x=650,y=580,width=220,height=40)

# # 7. Developer button
#         img_7 = Image.open(r"Main_Images\button7.jpeg")
#         img_7 = img_7.resize((220,220))
#         self.photoimg_7 = ImageTk.PhotoImage(img_7)

#         b1 = Button(bg_img,image = self.photoimg_7,cursor='hand2')
#         b1.place(x=800,y=380,width=220,height=220)

#         b_7 = Button(bg_img,text = "Developer",cursor='hand2',font=('times new roman',15,"bold"),bg='darkblue',fg='white')
#         b_7.place(x=800,y=580,width=220,height=40)

# 8. Exit button
        img_8 = Image.open(r"Main_Images\button8.jpeg")
        img_8 = img_8.resize((220,220))
        self.photoimg_8 = ImageTk.PhotoImage(img_8)

        b1 = Button(bg_img,image = self.photoimg_8,cursor='hand2',command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b_8 = Button(bg_img,text = "Exit",cursor='hand2',command=self.iExit,font=('times new roman',15,"bold"),bg='darkblue',fg='white')
        b_8.place(x=1100,y=580,width=220,height=40)


# open image

    def open_img(self):
        os.startfile('Data')



# ==========================Function Buttons=====================================

# student details function

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    


# Exit function

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

# trian data function

    def trian_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Trian(self.new_window)

# face recognition

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


# Attendance function
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()











