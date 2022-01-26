from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import* 
from tkinter import ttk 
import random 
import time 
import datetime
from tkinter import messagebox
from pandas import DataFrame

class Hospital: 
    def __init__(self,root): 
        self.root = root 
        self.root.title("ATU Hospital") 
        self.root.geometry("1540x800+0+0") 
    


        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="ATU HOSPITAL SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold")) 
        lbltitle.pack(side=TOP,fill=X)

###################################DATAFRAME################################################### 
        DataFrame = Frame(self.root,bd = 20,relief = RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10, 
                                                            font=("times new roman",12,"bold"),text= "Hangi Bölümden Randevu Alacak")
        DataFrameLeft.place(x=0,y=5,width=460,height=350)
        
        DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10, 
                                                            font=("times new roman",12,"bold"),text= "Doctors Information") 
        DataFrameRight.place(x=900,y=5,width=460,height=350) 
        
         

    
###################################BUTTON##################################################### 

        ButtonFrame = Frame(self.root,bd=20,relief=RIDGE) 
        ButtonFrame.place(x=0,y=530,width=1530,height=70) 
     
        
####################################DETAILS################################################### 

        DetailsFrame = Frame(self.root,bd=20,relief=RIDGE) 
        DetailsFrame.place(x=0,y=600,width=1530,height=190)  

#####################################DATAFRAMELEFT############################################ 
        
        lblNameTablet = Label(DataFrameLeft,text= " Clinics",font=("arial",12,"bold"),padx=2,pady=4)
        lblNameTablet.grid(row=0,column=0)

        conNametablet = ttk.Combobox(DataFrameLeft, font=("times new roman",12,"bold"), 
                                                                                    width=25)
        conNametablet["values"]=("Dahiliye","Cildiye","Nöroloji","Kulak Burun Boğaz","Korona")
        conNametablet.grid(row=0,column=1) 

        lblNameandSurname = Label(DataFrameLeft,font=("arial",12,"bold"),text= "Name and Surname",padx=2,pady=4)  
        lblNameandSurname.grid(row=1,column=0,sticky=W)
        txtNameandSurname = Entry(DataFrameLeft,font=("arial",12),width=17)
        txtNameandSurname.grid(row=1,column=1)
        
        lblGender = Label(DataFrameLeft,font=("arial",12,"bold"),text= "Gender",padx=2,pady=6)  
        lblGender.grid(row=2,column=0,sticky=W)
        txtGender = Entry(DataFrameLeft,font=("arial",12),width=17)
        txtGender.grid(row=2,column=1)
        
        lblAge = Label(DataFrameLeft,font=("arial",12,"bold"),text= "Age",padx=2,pady=6)  
        lblAge.grid(row=3,column=0,sticky=W)
        txtAge = Entry(DataFrameLeft,font=("arial",12),width=17)
        txtAge.grid(row=3,column=1) 
        
        lblCity = Label(DataFrameLeft,font=("arial",12,"bold"),text= "City",padx=2,pady=6)  
        lblCity.grid(row=4,column=0,sticky=W)
        txtCity = Entry(DataFrameLeft,font=("arial",12),width=17)
        txtCity.grid(row=4,column=1)  

        lblPhone = Label(DataFrameLeft,font=("arial",12,"bold"),text= "Phone Number",padx=2,pady=6)  
        lblPhone.grid(row=4,column=0,sticky=W)
        txtPhone = Entry(DataFrameLeft,font=("arial",12),width=17)
        txtPhone.grid(row=4,column=1)  
        
        

#############################################DataFrameRight#####################################  
        #self.txtDoctorsInfo = Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6) 
        #self.txtDoctorsInfo.grid(row=8,column=8) 

        #DoctorsInfo = Label(DataFrameLeft,text= " Doctors Informations",font=("arial",12,"bold"),padx=2,pady=4)
        #DoctorsInfo.grid(row=0,column=0)
        
        DoctorsInfo = Label(DataFrameRight, font=("times new roman",12,"bold"), 
                                                                                    width=25)
        DoctorsInfo.grid(row=0,column=1)  
        
        DoctorsNameandSurname = Label(DataFrameRight,font=("arial",12,"bold"),text= "Dr Name and Surname",padx=2)  
        DoctorsNameandSurname.grid(row=1,column=0,sticky=W)
        DtxtNameandSurname = Entry(DataFrameRight,font=("arial",12),width=17)
        DtxtNameandSurname.grid(row=1,column=1)
        
        DrClinic = Label(DataFrameRight,text= "Dr Clinic Name",font=("arial",12,"bold"),padx=2,pady=5)   
        DrClinic.grid(row=2,column=0,sticky=W) 

        DrNametablet = ttk.Combobox(DataFrameRight, font=("times new roman",12,"bold"), 
                                                                                    width=25)
        DrNametablet["values"]=("Dahiliye","Cildiye","Nöroloji","Kulak Burun Boğaz","Korona")
        DrNametablet.grid(row=2,column=1) 

        
        




root = Tk()  
def buttonFunction(): 
    print("GİRİS YAPINIZ")
b = Button(root, text="Giris", command=buttonFunction,padx=3,pady=8)
b.pack(side=TOP)  

b2 = Button(root,text="Click",command=buttonFunction)
b2.pack(side=BOTTOM)
ob = Hospital(root) 
root.mainloop()