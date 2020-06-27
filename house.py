from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3
import PIL
from PIL import ImageTk, Image

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Movie






class HouseGUI:
    def __init__(self,master,conn):
        self.master = master 
        self.conn = conn 
        self.dMovie = Movie(self.conn)

        master.configure(bg='dodgerblue')
        master.title("Movie")
        
        labelfont = ('algerian', 20,'underline','bold')
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.col = 0
        
        def change_dropdown(*args):
            print( self.tkvar.get() )
        
        #genre dropdown
        # Add a grid
        mainframe = Frame(master)
        mainframe.grid(column=1,row=4, sticky=(N,W,E,S) )
        mainframe.columnconfigure(1, weight = 1)
        mainframe.rowconfigure(3, weight = 1)
        mainframe.grid(pady = 100, padx = 100)

        # Create a Tkinter variable
        self.tkvar = StringVar(master)

        # list with options
        choices = [ 'Critically Acclaimed','Thriller','Action','Comedy','Drama','Documentary']
        self.tkvar.set('Critically Acclaimed') # set the default option
        
        popupMenu = OptionMenu(mainframe, self.tkvar, *choices)
        Label(mainframe, text="Genre",bg='dodgerblue',fg='navy').grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)
        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)

        #rating dropdown
        # Add a grid
        mainframe2 = Frame(master)
        mainframe2.grid(column=2,row=4, sticky=(N,W,E,S) )
        mainframe2.columnconfigure(1, weight = 1)
        mainframe2.rowconfigure(3, weight = 1)
        mainframe2.grid(pady = 100, padx = 100)

        # Create a Tkinter variable
        self.tkvar2 = StringVar(master)

        # list with options
        choices2 = [ 'None','PG','PG13','R','G']
        self.tkvar2.set('None') # set the default option
        
        popupMenu2 = OptionMenu(mainframe2, self.tkvar2, *choices2)
        Label(mainframe2, text="Rating",bg='dodgerblue',fg='navy').grid(row = 1, column = 2)
        popupMenu2.grid(row = 2, column =2)
        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)



        #self.label_1= Label(master,text='Search',bg='dodgerblue',fg='navy')
        
        self.entry_1= Entry(master,bg='lightsteelblue')
       
        #self.label_1.grid(row=4,sticky=E,pady=5)
        
        self.entry_1.grid(row=4,column=0,ipadx=30,padx=30,pady=5,sticky=W)
        

        self.label.config(font=labelfont)

        self.button1 = Button(self.master,text='Left',bg='lightsteelblue',fg='navy', command=self.Left)
        self.button2 = Button(self.master,text='Right',bg='lightsteelblue',fg='navy',command=self.Right)
        self.button4 = Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)
        self.button5 = Button(self.master,text='Search',bg='lightsteelblue',fg='navy', command=self.Searchbar)
        
        self.button1.grid(row=5,column=1,ipadx=15,pady=10,sticky=W)
        self.button2.grid(row=5,column=2,ipadx=15,pady=10,sticky=W)
        self.button4.grid(row=5,column=3,ipadx=15,pady=10,sticky=W)
        self.button5.grid(row=5,column=0,ipadx=15,pady=10,sticky=W)

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
      

        self.tree.bind("<Double-1>",self.onDoubleClick)
        
        #gets paths from the movie class and puts them in a list
        self.path=[]
        self.path=[
            self.dMovie.getpath(self.col+1),
            self.dMovie.getpath(self.col+2),
            self.dMovie.getpath(self.col+3),
            self.dMovie.getpath(self.col+4)
        ]
        self.panel = []
        #display pictures        
        self.displayImage(self.path,self.col)

        

    def onDoubleClick(self,event):
        item = self.tree.selection()[0]
        item_text = self.tree.item(item)
        print(item_text)
        #id of the movie
        print(item_text['values'][0])
        print(self.tree.selection()[0])
        #put on screen
        #ask to sign in then generate rent
   
    #display 4 pictures that are in the database, the first four
    def displayImage(self,path,col):
        print(path)
        i=0
        for i in range(4):
            img = ImageTk.PhotoImage(Image.open(path[i]))
            self.panel.append(Label(self.master,image=img))
            self.panel[self.col+i].image = img
            self.panel[self.col+i].grid(row=3,column=i,ipadx=0,pady=20,sticky=W)
            

  
    def updatePicture(self,path):
        self.path=[
            self.dMovie.getpath(self.col+1),
            self.dMovie.getpath(self.col+2),
            self.dMovie.getpath(self.col+3),
            self.dMovie.getpath(self.col+4)
        ]
        print(self.path)
        i=0
        for i in range(4):
            self.panel[i].destroy()
        self.panel = []
        i=0
        for i in range(4):
            img = ImageTk.PhotoImage(Image.open(self.path[i]))
            self.panel.append(Label(self.master,image=img))
            self.panel[i].image = img
            self.panel[i].grid(row=3,column=i,ipadx=0,pady=20,sticky=W)
             
    def Left(self):
        if(self.col>=1):
            self.col = self.col-1
            self.updatePicture(self.path)
        else:
            print('left already = leftmost')


    def Right(self):
        self.col = self.col+1
        self.updatePicture(self.path)

    def clear(self):
        self.entry_1.delete(0,END)
        
        
    def Searchbar(self):
        Search_Text = self.entry_1.get()
        data = self.dMovie.Searchbar(Search_Text)
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True

    def update(self):
        genre = self.tkvar.get()
        rating = self.tkvar2.get()
        #read from database
        data = self.dMovie.Search(genre,rating)
        #clear tree
        self.clearTree()
        #add to tree
        for x in data:
            self.tree.insert('','end',values=x)            
        return True
        


    def delete(self):
        item = self.tree.selection()[0]
        item_text = self.tree.item(item)
        print(item_text)
        print(self.tree.selection()[0])
        self.dMovie.delete(item_text[0])
        return True

  
    def clearTree(self):
       for i in self.tree.get_children():
           self.tree.delete(i)
    


#root = Tk()
#Cust = CustomerGUI(master)
#root.mainloop()
