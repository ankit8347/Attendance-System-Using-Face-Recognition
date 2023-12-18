from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Trian:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

 # top image
        title_lbl = Label(self.root,text="TRAIN DATA SET",font=('times new roman',35,"bold"),bg='white',fg='blue')
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top = Image.open(r"Main_Images\train_top.jpeg")
        img_top = img_top.resize((1530,325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        label_left = Label(self.root,image=self.photoimg_top)
        label_left.place(x=0,y=45,width=1530,height=325)



# train button

        b_1 = Button(self.root,text = "Train Data",cursor='hand2',command=self.train_classifier,font=('times new roman',40,"bold"),bg='darkblue',fg='white')
        b_1.place(x=0,y=370,width=1530,height=70)




# bottom image

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=('times new roman',35,"bold"),bg='white',fg='blue')
        title_lbl.place(x=0,y=0,width=1530,height=50)


        img_bottom = Image.open(r"Main_Images\train_bottom.jpeg")
        img_bottom = img_bottom.resize((1530,325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        label_left = Label(self.root,image=self.photoimg_bottom)
        label_left.place(x=0,y=440,width=1530,height=330)


    def train_classifier(self):
        data_dir = ('Data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] # list comprehension 24:50

        faces = []
        ids = []

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image

            image_np = np.array(img,"uint8")
            id = int(os.path.split(image)[1].split('.')[1]) # 31.09


            faces.append(image_np)
            ids.append(id)
            cv2.imshow('Training',image_np)
            cv2.waitKey(1)==13

        
        ids = np.array(ids)


        # ---------------------Train the classifier And Save----------------------------------------

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!!")














if __name__ == "__main__":
    root = Tk()
    obj = Trian(root)
    root.mainloop()