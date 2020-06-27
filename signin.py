from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Customer
from house import HouseGUI
from signup import SignupGUI


class SignInGUI:
    def __init__(self,master,conn):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("Customer")
        self.top = Toplevel()
        
        #database
        self.conn = conn
        self.dcustomer = Customer(self.conn)
        
        labelfont = ('algerian', 20,'underline','bold')
        
        self.label= Label(master,text='BlueBox',bg='dodgerblue',fg='navy')
        self.label_1= Label(master,text='User Name',bg='dodgerblue',fg='navy')
        self.label_2= Label(master,text='Password',bg='dodgerblue',fg='navy')
       
        
        self.entry_1= Entry(master,bg='lightsteelblue')
        self.entry_2= Entry(master,bg='lightsteelblue',show = '*')

        self.label.grid(row=0,column=1,ipady=25,ipadx=30,padx=30,pady=5,sticky=W)

        self.label_1.grid(row=1,sticky=E,pady=5)
        self.label_2.grid(row=3,sticky=E,pady=5)
        
        
        self.entry_1.grid(row=1,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        self.entry_2.grid(row=3,column=1,ipadx=30,padx=30,pady=5,sticky=W)
        

        self.label.config(font=labelfont)

        self.button1= Button(self.master,text='Sign in',bg='lightsteelblue',fg='navy', command=self.signin)
        self.button2= Button(self.master,text='Clear',bg='lightsteelblue',fg='navy', command=self.clear)
        self.button3= Button(self.master,text='Guest checkout',bg='lightsteelblue',fg='navy', command=self.signup)
        self.button1.grid(row=11,column=0,ipadx=15,pady=20)
        self.button2.grid(row=11,column=1,ipadx=15,pady=20)
        self.button3.grid(row=11,column=2,ipadx=15,pady=20)


    def clear(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
    def signup(self):
        newwindow = SignupGUI(self.top,self.conn) 

    def signin(self):
        signedin = self.dcustomer.signin(self.entry_1.get(),self.entry_2.get())
        if(signedin):
            messagebox.showinfo("Success",'Welcome! Processing Rental!' )
            newwindow = HouseGUI(self.top,self.conn) 
            return True
        else:
            messagebox.showinfo("Failure",'Invalid Username and password' )
            return False    

        