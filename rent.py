from tkinter import*
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import RENT

#sigin GUI so that when rent is called a sign is required
from signin import SignInGUI





class RentGUI:
    def __init__(self,master,conn):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("RENT")
        
        #database
        self.conn = conn
        self.drent = RENT(conn)
        
        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='Customer ID',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Blu Ray ID',bg='dodgerblue',fg='navy')
        self.label_3= Label(master,text='DVD ID',bg='dodgerblue',fg='navy')
        self.label_4= Label(master,text='Type',bg='dodgerblue',fg='navy')
   

        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue')
        self.entry_3= Entry(master,bg='lightsteelblue')
        self.entry_4= Entry(master,bg='lightsteelblue')

        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_2.grid(row=2,sticky=E,pady=5)
        self.label_3.grid(row=3,sticky=E,pady=5)
        self.label_4.grid(row=4,sticky=E,pady=5)

        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=2,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_3.grid(row=3,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_4.grid(row=4,column=1,ipadx=30,padx=30,pady=5,sticky=W)

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Rent',bg='lightsteelblue',fg='navy', command=self.rent)
        self.button2= Button(self.master,text='Clear',bg='lightsteelblue',fg='navy', command=self.clear)
        self.button3= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)


        self.button1.grid(row=12,column=0,ipadx=15,pady=20,sticky=W)
        self.button2.grid(row=12,column=1,ipadx=15,pady=20,sticky=W)
        self.button3.grid(row=12,column=2,ipadx=15,pady=20,sticky=W)
        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("Date_Rent", "C_ID", "BLU_ID","DVD_ID", "Type", "DateReturn" )

        self.tree.column("Date_Rent", width=90, minwidth=90,stretch=False)
        self.tree.column("C_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("BLU_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("DVD_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("Type", width=90, minwidth=90,stretch=False)
        self.tree.column("DateReturn", width=90, minwidth=90,stretch=False)
        

        self.tree.heading("Date_Rent", text="Date_Rent", anchor=tk.W)
        self.tree.heading("C_ID",text="C_ID", anchor=tk.W)
        self.tree.heading("BLU_ID",text="BLU_ID", anchor=tk.W)
        self.tree.heading("DVD_ID", text="DVD_ID", anchor=tk.W)
        self.tree.heading("Type", text="Type", anchor=tk.W)
        self.tree.heading("DateReturn", text="DateReturn", anchor=tk.W)
        self.tree.grid(row=15, column=0, columnspan=3, ipadx=1,pady=5,sticky=tk.W)
   
    def update(self):
        #read from database
        data = self.drent.readAll()
        #clear tree
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True   
        


    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
    
    def clearTree(self):
       for i in self.tree.get_children():
           self.tree.delete(i)

    def rent(self):
        #makes datetimes
        DateReturn= datetime(1,1,1,0,0,0,0)
        Date_Rented = datetime.now()
        string=''
        string = self.entry_2.get()

        Blu_ID = int(string) #Blu_ID
        string=self.entry_3.get()
        DVD_ID = int(self.entry_3.get()) #DVD_ID
        
        #if blueray make DVD_ID=NULL, else visa versa
        Type = self.entry_4.get()
        if Type == 'b':
         DVD_ID = -1
        else: 
         Blu_ID = -1
        #reads data
        data=[]
        data =[
        Date_Rented, #date rented       
        self.entry_1.get(), #customer id
        Blu_ID, 
        DVD_ID,       
        self.entry_4.get(), #bluray or dvd(denoted by b or d)
        DateReturn #date returned
        ]
        top = Toplevel()
        signedin= False
        newwindow = SignInGUI(top,self.conn)
        #no implimentation of checking signin = True yet couldnt figure out how to pass from signinGUI to rentGUI
        self.drent.add(data)
        
        return True

   



  


#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
