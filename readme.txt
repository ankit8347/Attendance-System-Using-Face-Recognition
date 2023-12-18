 "M.Sc. IT in Data Management & Visual Insight (B.Sc. IT+ M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in FinTech (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in IT Game Design & Development (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in Digital Design (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in IT IMS & Cyber Security (B.Sc. + M.Sc.) (5 Years Integrated)",
 "M.Sc. IT in Software Development (Web & Mobile) (B.Sc. IT+ M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in Animation & VFX (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in Cloud & Application Development (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in Architecture & Network Security (B.Sc. IT + M.Sc. IT) (5 Years Integrated)",
 "M.Sc. IT in Information Security & Cyber Forensic (5 Years Integrated)",
 "IMBA in Financial Services (BBA+MBA) (5 Years Integrated)",
 "M.Sc. IT in Game Design & Development (Post Graduate)",
 "M.Sc. IT in Business Intelligence & Analytics (Post Graduate)",
 "M.Sc. IT in Mobile App & UI Development (Post Graduate)",
 "M.Sc. IT in IMS and Cloud Technology (Post Graduate)",
 "M.Sc. IT in Animation & VFX (Post Graduate)",
 "M.Sc. IT in Network Security (Post Graduate)",
 "M.Sc. IT in FinTech (Post Graduate)"










        dep_combo["values"] = ("Select Department" , "M.Sc. IT in Business Intelligence & Analytics",
 "M.Sc. IT in Game Design & Development",
 "M.Sc. IT in Mobile App & UI Development",
 "M.Sc. IT in IMS and Cloud Technology",
 "M.Sc. IT in Animation & VFX",
 "M.Sc. IT in Network Security",
 "M.Sc. IT in FinTech")








Departmenat
"Course"
"Year"
"Semester"
"Id"
"Name"
"Division"
"Roll_no"
"Gender"
"DOB"
"Email"
"Phone"
"Address"
"Teacher"
"Photo"




----------------------mysql workbench--------------------------------------
CREATE database face_recognition;
use face_recognition;

Create table Student_info( Departmenat Varchar(50),
Course Varchar(50),
Year Varchar(50),
Semester Varchar(50),
Id int(20) PRIMARY KEY,
Name Varchar(50),
Division Varchar(50),
Roll_no int(25),
Gender Varchar(50),
DOB Varchar(50),
Email Varchar(50),
Phone Varchar(50),
Address Varchar(50),
Teacher Varchar(50),
Photo Varchar(50)
);

select * from student_info;















# why we use LBPH Algoritham
https://youtu.be/ZLVvI4GPepI?si=A_rvVTJNt3iv-aKL
- 21:20


# Why we use numpy
-34:55

# module error
 https://stackoverflow.com/questions/45655699/attributeerror-module-cv2-face-has-no-attribute-createlbphfacerecognizer

# .join error
https://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found