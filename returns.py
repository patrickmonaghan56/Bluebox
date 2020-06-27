from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Customer
from database_class import RENT
from database_class import PAYMENT


from datetime import datetime



class ReturnGUI:
    def __init__(self,master,conn):
        self.master = master 
       

        master.configure(bg='dodgerblue')
        master.title("Return")

         #database
        self.conn = conn
        self.dbcustomer = Customer(conn)
        self.drent = RENT(conn)
        self.dpayment = PAYMENT(conn)

        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='ID MOVIE',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Type',bg='dodgerblue',fg='navy')
        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue')
        
        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_2.grid(row=2,sticky=E,pady=5)

        
        
        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=2,column=1,ipadx=30,padx=30,pady=5,sticky=W)

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='RETURN',bg='lightsteelblue',fg='navy', command=self.update)
        self.button2= Button(self.master,text='CLEAR',bg='lightsteelblue',fg='navy', command=self.clear)
        

        self.button1.grid(row=12,column=1,ipadx=15,pady=20,sticky=W)
        self.button2.grid(row=13,column=1,ipadx=15,pady=20,sticky=W)

    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)


    def update(self):
        DateReturn = datetime.now()
        Disk_ID = int(self.entry_1.get())
        data=[]
        data =[
        DateReturn, #date returned       
        Disk_ID
        ]
        Type = self.entry_2.get()
        #call use case
                
        self.dpayment.add(Type,data)
        return True

    def delete(self):
        print("delete")
        return True

  
    


#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
