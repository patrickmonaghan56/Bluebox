from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Customer







class CustomerGUI:
    def __init__(self,master,conn):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("Customer")

        #database
        self.conn = conn
        self.dcustomer = Customer(self.conn)
        
        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)
        

        self.button1.grid(row=12,column=1,ipadx=15,pady=20,sticky=W)
   
        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("ID", "First Name", "Middle Name", "Last Name", "Date of Birth", "Email", "Rented", "Max Rented", "Credit Card #", "Password","Username","Can Rent" )

        self.tree.column("ID", width=90, minwidth=90,stretch=False)
        self.tree.column("First Name", width=90, minwidth=90,stretch=False)
        self.tree.column("Middle Name", width=90, minwidth=90,stretch=False)
        self.tree.column("Last Name", width=90, minwidth=90,stretch=False)
        self.tree.column("Date of Birth", width=90, minwidth=90,stretch=False)
        self.tree.column("Email", width=90, minwidth=90,stretch=False)
        self.tree.column("Rented", width=90, minwidth=90,stretch=False)
        self.tree.column("Max Rented", width=90, minwidth=90,stretch=False)
        self.tree.column("Credit Card #", width=90, minwidth=90,stretch=False)
        self.tree.column("Password", width=90, minwidth=90,stretch=False)
        self.tree.column("Username", width=90, minwidth=90,stretch=False)
        self.tree.column("Can Rent", width=90, minwidth=90,stretch=False)

        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("First Name",text="First Name", anchor=tk.W)
        self.tree.heading("Middle Name",text="Middle Name", anchor=tk.W)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.W)
        self.tree.heading("Date of Birth", text="Date of Birth", anchor=tk.W)
        self.tree.heading("Email", text="Email", anchor=tk.W)
        self.tree.heading("Rented", text="Rented", anchor=tk.W)
        self.tree.heading("Max Rented", text="Max Rented", anchor=tk.W)
        self.tree.heading("Credit Card #", text="Credit Card #", anchor=tk.W)
        self.tree.heading("Password", text="Password", anchor=tk.W)
        self.tree.heading("Username", text="Username", anchor=tk.W)
        self.tree.heading("Can Rent", text="Can Rent", anchor=tk.W)
        self.tree.grid(row=13, column=1, ipadx=0,pady=5,sticky=tk.W)



    def update(self):
        #read from database
        data = self.dcustomer.readAll()
        #clear tree
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True


    def clearTree(self):
       for i in self.tree.get_children():
           self.tree.delete(i)
    


#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
