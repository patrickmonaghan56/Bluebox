from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import PAYMENT




class PaymentGUI:
    def __init__(self,master,conn):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("Payment")
        self.conn = conn
        self.dPayment = PAYMENT(conn)

        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        
        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)
        
        self.button1.grid(row=2,column=1,ipadx=15,pady=20,sticky=W)
       
        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("P_ID","C_ID", "P_Amount", "Receipt", "DatePayment")

        self.tree.column("P_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("C_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("P_Amount", width=90, minwidth=90,stretch=False)
        self.tree.column("Receipt", width=90, minwidth=90,stretch=False)
        self.tree.column("DatePayment", width=90, minwidth=90,stretch=False)
        
        self.tree.heading("P_ID", text="P_ID", anchor=tk.W)
        self.tree.heading("C_ID",text="C_ID", anchor=tk.W)
        self.tree.heading("P_Amount",text="P_Amount", anchor=tk.W)
        self.tree.heading("Receipt", text="Receipt", anchor=tk.W)
        self.tree.heading("DatePayment", text="DatePayment", anchor=tk.W)

        self.tree.grid(row=10, column=1, ipadx=0,pady=5,sticky=W)


    def update(self):
        #read from database
        data = self.dPayment.readAll()
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
