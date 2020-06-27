from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Movie






class MovieGUI:
    def __init__(self,master,conn):
        self.master = master 
        self.conn = conn 
        self.dMovie = Movie(conn)

        master.configure(bg='dodgerblue')
        master.title("Movie")
        
        labelfont = ('algerian', 20,'underline','bold')
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='Title',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Description',bg='dodgerblue',fg='navy')
        self.label_3= Label(master,text='Rating',bg='dodgerblue',fg='navy')
        self.label_4= Label(master,text='Year',bg='dodgerblue',fg='navy')
        self.label_5= Label(master,text='Quality',bg='dodgerblue',fg='navy')
        self.label_6= Label(master,text='Genre',bg='dodgerblue',fg='navy')
        self.label_7= Label(master,text='IMG path',bg='dodgerblue',fg='navy')

        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue')
        self.entry_3= Entry(master,bg='lightsteelblue')
        self.entry_4= Entry(master,bg='lightsteelblue')
        self.entry_5= Entry(master,bg='lightsteelblue')
        self.entry_6= Entry(master,bg='lightsteelblue')
        self.entry_7= Entry(master,bg='lightsteelblue')
        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_2.grid(row=2,sticky=E,pady=5)
        self.label_3.grid(row=4,sticky=E,pady=5)
        self.label_4.grid(row=5,sticky=E,pady=5)
        self.label_5.grid(row=6,sticky=E,pady=5)
        self.label_6.grid(row=7,sticky=E,pady=5)
        self.label_7.grid(row=8,sticky=E,pady=5)

        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=2,rowspan=2,column=1,ipadx=30,ipady=10,padx=30,pady=5,sticky=W)
        self.entry_3.grid(row=4,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_4.grid(row=5,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_5.grid(row=6,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_6.grid(row=7,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_7.grid(row=8,column=1,ipadx=30,padx=30,pady=5,sticky=W)

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Clear',bg='lightsteelblue',fg='navy', command=self.clear)
        self.button2= Button(self.master,text='Add',bg='lightsteelblue',fg='navy',command=self.add)
        self.button3= Button(self.master,text='Delete',bg='lightsteelblue',fg='navy', command=self.delete)
        self.button4= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)

        
        self.button1.grid(row=7,column=2,ipadx=15,pady=20,sticky=W)
        self.button2.grid(row=7,column=3,ipadx=15,pady=20,sticky=W)
        self.button3.grid(row=8,column=2,ipadx=15,pady=20,sticky=W)
        self.button4.grid(row=8,column=3,ipadx=15,pady=20,sticky=W)

        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("M_ID","Title","Description","Rating","Year","Quality","Genre","DVD_Quantity","BLU_Ray_Quantity", "CopyRentDVD","CopyRentedBluRay")

        self.tree.column("M_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("Title", width=90, minwidth=90,stretch=False)
        self.tree.column("Description", width=250, minwidth=250,stretch=False)
        self.tree.column("Rating", width=90, minwidth=90,stretch=False)
        self.tree.column("Year", width=90, minwidth=90,stretch=False)
        self.tree.column("Quality", width=90, minwidth=90,stretch=False)
        self.tree.column("Genre", width=90, minwidth=90,stretch=False)
        self.tree.column("DVD_Quantity", width=50, minwidth=50,stretch=False)
        self.tree.column("BLU_Ray_Quantity", width=50, minwidth=50,stretch=False)
        self.tree.column("CopyRentDVD", width=50, minwidth=50,stretch=False)
        self.tree.column("CopyRentedBluRay", width=50, minwidth=50,stretch=False)
        

        self.tree.heading("M_ID", text="M_ID", anchor=tk.W)
        self.tree.heading("Title", text="Title", anchor=tk.W)
        self.tree.heading("Description",text="Description", anchor=tk.W)
        self.tree.heading("Rating",text="Rating", anchor=tk.W)
        self.tree.heading("Year", text="Year", anchor=tk.W)
        self.tree.heading("Quality", text="Quality", anchor=tk.W)
        self.tree.heading("Genre", text="Genre", anchor=tk.W)
        self.tree.heading("DVD_Quantity",text="DVDs", anchor=tk.W)
        self.tree.heading("BLU_Ray_Quantity", text="BLURays", anchor=tk.W)
        self.tree.heading("CopyRentDVD", text="RentedDVD", anchor=tk.W)
        self.tree.heading("CopyRentedBluRay", text="RentedBlu", anchor=tk.W)
        self.tree.grid(row=10, column=0,columnspan=4, ipadx=0,pady=5,sticky=tk.W)


    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
        self.entry_4.delete(0,END)
        self.entry_5.delete(0,END)
        self.entry_6.delete(0,END)
        self.entry_7.delete(0,END)
        


    def add(self):
        data=[]
        data =[
        self.entry_1.get(),
        self.entry_2.get(),
        self.entry_3.get(),
        self.entry_4.get(),
        self.entry_5.get(),
        self.entry_6.get(),
        0,#DVDs of movie
        0,#Blu rays of movie
        0,#DVDs currently out 
        0,#Blu rays currently out 
        self.entry_7.get()#img file for title screen     
        ]
        self.dMovie.create(data)
       
        
        return True


    def update(self):
        #read from database
        data = self.dMovie.readAll()
        #clear tree
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True
        


    def delete(self):
        print("delete")
        return True

  
    def clearTree(self):
       for i in self.tree.get_children():
           self.tree.delete(i)
    


#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
