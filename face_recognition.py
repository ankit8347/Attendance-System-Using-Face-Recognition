from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


# lable
        title_lbl = Label(self.root,text="FACE RECOGNITION",font=('times new roman',35,"bold"),bg='white',fg='purple')
        title_lbl.place(x=0,y=0,width=1530,height=45)

 # image 1
        img_top = Image.open(r"Main_Images\face_recognition.jpeg")
        img_top = img_top.resize((650,700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        label_left = Label(self.root,image=self.photoimg_top)
        label_left.place(x=0,y=45,width=650,height=700)
 # image 2

        img_bottom = Image.open(r"Main_Images\face_recognition2.jpeg")
        img_bottom = img_bottom.resize((950,700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        label_left = Label(self.root,image=self.photoimg_bottom)
        label_left.place(x=650,y=45,width=950,height=700)

# train button

        b_1 = Button(label_left,text = "Face Recognition",command=self.face_recog,cursor='hand2',font=('times new roman',18,"bold"),bg='navy',fg='white')
        b_1.place(x=400,y=620,width=200,height=40)


#  ------------------------Attendance--------------------------------------
    def mark_attendance(self,Id_select,roll_no_select,name_select,Departmenat_select):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((Id_select not in name_list)) and (roll_no_select not in name_list) and (name_list not in name_list) and (Departmenat_select not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{Id_select},{roll_no_select},{name_select},{Departmenat_select},{dtString},{d1},Present")



# -------------------------Face Recognition -------------------------------

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            corrd = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) # predict the data

                confidence = int((100*(1-predict/300))) # formula


                my_db = mysql.connector.connect(host="localhost",user='root',password='peace@123',database='face_recognition')
                my_cursor = my_db.cursor()
                
                my_cursor.execute("Select Name from student_info where Id="+str(id))
                name_select = my_cursor.fetchone()
                name_select = "+".join(name_select)

                my_cursor.execute("Select Roll_no from student_info where Id="+str(id))
                roll_no_select = my_cursor.fetchone()
                roll_no_select = '+'.join([str(i) for i in roll_no_select])      # roll_no_select = "+".join(roll_no_select)



                my_cursor.execute("Select Departmenat from student_info where Id="+str(id))
                Departmenat_select = my_cursor.fetchone()
                Departmenat_select = "+".join(Departmenat_select)

                my_cursor.execute("Select ID from student_info where Id="+str(id))
                Id_select = my_cursor.fetchone()
                Id_select = '+'.join([str(i) for i in Id_select])


                if confidence > 77:
                    cv2.putText(img,f"ID:{Id_select}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{roll_no_select}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{name_select}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Departmenat:{Departmenat_select}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    self.mark_attendance(Id_select,roll_no_select,name_select,Departmenat_select)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                corrd = [x,y,w,h]

            return corrd

        def recognize(img,clf,faceCascade):
            corrd=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap = cv2.VideoCapture(0)        #     video Capture--------------------------------------------

        while True:
            ret , img  = video_cap.read()
            img  = recognize(img,clf,faceCascade)


            cv2.imshow("Welcome to Face Recognition",img)

            
            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()







if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()





