from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Customer





class SignupGUI:
    def __init__(self,master,conn):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("SIGN UP")
        
        
        self.conn = conn
        self.ucustomer = Customer(self.conn)

        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='First Name',bg='dodgerblue',fg='navy')
        self.label_10= Label(master,text='Middle Name',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Last Name',bg='dodgerblue',fg='navy')
        self.label_3= Label(master,text='Date of birth',bg='dodgerblue',fg='navy')
        self.label_11= Label(master,text='Email',bg='dodgerblue',fg='navy')
        self.label_4= Label(master,text='Credit Card #',bg='dodgerblue',fg='navy')
        self.label_7= Label(master,text='Username',bg='dodgerblue',fg='navy')
        self.label_8= Label(master,text='Password',bg='dodgerblue',fg='navy')
        self.label_9= Label(master,text='WELCOME TO BLUE BOX',bg='dodgerblue',fg='navy')
        
        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_10= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue')
        self.entry_3= Entry(master,bg='lightsteelblue')
        self.entry_11= Entry(master,bg='lightsteelblue')
        self.entry_4= Entry(master,bg='lightsteelblue')
        self.entry_5= Entry(master,bg='lightsteelblue')
       
        self.entry_7= Entry(master,bg='lightsteelblue')
        self.entry_8= Entry(master,bg='lightsteelblue',show='*')

        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_10.grid(row=2,sticky=E,pady=5)
        self.label_2.grid(row=3,sticky=E,pady=5)
        self.label_3.grid(row=4,sticky=E,pady=5)
        self.label_11.grid(row=5,sticky=E,pady=5)
        self.label_4.grid(row=6,sticky=E,pady=5)
        self.label_7.grid(row=9,sticky=E,pady=5)
        self.label_8.grid(row=10,sticky=E,pady=5)
        
        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_10.grid(row=2,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=3,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_3.grid(row=4,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_11.grid(row=5,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_4.grid(row=6,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        
        self.entry_7.grid(row=9,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_8.grid(row=10,column=1,ipadx=30,padx=30,pady=5,sticky=W)

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Sign up',bg='lightsteelblue',fg='navy', command=self.add)
        self.button2= Button(self.master,text='Clear',bg='lightsteelblue',fg='navy', command=self.clear)
        self.button1.grid(row=11,column=1,ipadx=15,pady=20)
        self.button2.grid(row=11,column=2,ipadx=15,pady=20)


   


    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_10.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_11.delete(0,END)
        self.entry_4.delete(0,END)
        self.entry_7.delete(0,END)
        self.entry_8.delete(0,END)


    def add(self):
        #read data
        data =(
        self.entry_1.get(),
        self.entry_10.get(),
        self.entry_2.get(),
        self.entry_3.get(),
        self.entry_11.get(),
        0,  #rented
        4,  #max rented
        self.entry_4.get(),  
        self.entry_8.get(), #password
        self.entry_7.get(),
        True) #can rent

        #call use case
        self.ucustomer.create(data)
         
        return True

    




#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
