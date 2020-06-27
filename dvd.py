from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import DVD
from database_class import Movie





class DVDGUI:
    def __init__(self,master,conn):
        self.master = master 
        
        self.conn = conn 
        self.dDVD = DVD(conn)
        self.dMovie = Movie(conn)
        
        master.configure(bg='dodgerblue')
        master.title("DVD")
        
        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='ID_Movie',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Cost',bg='dodgerblue',fg='navy')
        
        
        
        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue')
        
        

        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_2.grid(row=2,sticky=E,pady=5)
        
        
        
        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=2,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        
        

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Clear',bg='lightsteelblue',fg='navy', command=self.clear)
        self.button2= Button(self.master,text='Add',bg='lightsteelblue',fg='navy',command=self.add)
        self.button3= Button(self.master,text='Delete',bg='lightsteelblue',fg='navy', command=self.delete)
        self.button4= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)


        self.button1.grid(row=12,column=1,ipadx=15,pady=20,sticky=W)
        self.button2.grid(row=12,column=2,ipadx=20,pady=20,sticky=W)
        self.button3.grid(row=11,column=1,ipadx=20,pady=20,sticky=W)
        self.button4.grid(row=11,column=2,ipadx=20,pady=20,sticky=W)

        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("DVD_ID","Movie_ID","Cost", "Rented_Out")

        self.tree.column("DVD_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("Movie_ID", width=90, minwidth=90,stretch=False)
        self.tree.column("Cost", width=90, minwidth=90,stretch=False)
        self.tree.column("Rented_Out", width=90, minwidth=90,stretch=False)
        
        self.tree.heading("DVD_ID", text="DVD_ID", anchor=tk.W)
        self.tree.heading("Movie_ID", text="Movie_ID", anchor=tk.W)
        self.tree.heading("Cost",text="Cost", anchor=tk.W)
        self.tree.heading("Rented_Out",text="Rented_Out", anchor=tk.W)
        self.tree.grid(row=10, column=0,columnspan=3, ipadx=0,pady=5,sticky=tk.W)


    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        


    def add(self):
        data=[]
        data =[
        self.entry_1.get(),
        self.entry_2.get(),
        False  
        ]
        if((len(self.dMovie.read(data[0])))==1):
         self.dDVD.create(data)
        else:
         print('Invalid Movie ID, add Movie first')
        
        return True


    def update(self):
        #read from database
        data = self.dDVD.readAll()
        #clear tree
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True

    def delete(self):
        data = self.entry_1.get()
        self.dDVD.delete(data)
        return True

  
    def clearTree(self):
       for i in self.tree.get_children():
           self.tree.delete(i)
    


#root = Tk()
#root.mainloop()
