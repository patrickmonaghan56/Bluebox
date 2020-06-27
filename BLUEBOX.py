from tkinter import*
import tkinter as tk
from tkinter import ttk


import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Customer

#classes for the use cases

from signin import SignInGUI
from customer import CustomerGUI
from signup import SignupGUI
from rent import RentGUI
from returns import ReturnGUI
from movie import MovieGUI
from dvd import DVDGUI
from bluray import BlurayGUI
from payment import PaymentGUI
from house import HouseGUI
from database_class import CreateDatabase


class GeneralGUI:
    def __init__(self,master):
        self.master = master 
        master.configure(bg='dodgerblue')
        master.title("BLUEBOX")
        self.conn = None
        self.DBFile = "/Users/Patrickmonaghan/Desktop/proj_sof_eng 430 final/myDB.db"
        self.setupDB()



        self.button1= Button(text='Sign up',bg='lightsteelblue',fg='navy', command=self.signup)
        self.button2= Button(text='Rent',bg='lightsteelblue',fg='navy',command=self.rent)
        self.button3= Button(text='Return',bg='lightsteelblue',fg='navy', command=self.returns)
        self.button4= Button(text='Movie Management',bg='lightsteelblue',fg='navy', command=self.movie)
        self.button5= Button(text='DVD Management',bg='lightsteelblue',fg='navy', command=self.dvd)
        self.button6= Button(text='Bluray Management',bg='lightsteelblue',fg='navy', command=self.bluray)
        self.button7= Button(text='Customer Management',bg='lightsteelblue',fg='navy', command=self.customer)
        self.button8= Button(text='Payment Management',bg='lightsteelblue',fg='navy', command=self.payment)
        self.button9= Button(text='Create Database',bg='lightsteelblue',fg='navy', command=self.createDatabase)
        self.button10= Button(text='Search',bg='lightsteelblue',fg='navy', command=self.house)
        self.button11= Button(text='Sign In',bg='lightsteelblue',fg='navy', command=self.signin)

        self.button1.grid(row=1,column=1,ipadx=15,pady=20)
        self.button2.grid(row=2,column=1,ipadx=20,pady=20)
        self.button3.grid(row=3,column=1,ipadx=20,pady=20)
        self.button4.grid(row=4,column=1,ipadx=30,pady=20)
        self.button5.grid(row=5,column=1,ipadx=40,pady=20)
        self.button6.grid(row=6,column=1,ipadx=50,pady=20)
        self.button7.grid(row=7,column=1,ipadx=60,pady=20)
        self.button8.grid(row=8,column=1,ipadx=70,pady=20)
        self.button9.grid(row=9,column=1,ipadx=70,pady=20)
        self.button10.grid(row=10,column=1,ipadx=70,pady=20)
        self.button11.grid(row=11,column=1,ipadx=70,pady=20)
   



    def customer(self):
        top = Toplevel()
        newwindow = CustomerGUI(top,self.conn) 
        return True


    def movie(self):
        top = Toplevel()
        newwindow = MovieGUI(top,self.conn) 
        return True


    def dvd(self):
        top = Toplevel()
        newwindow = DVDGUI(top,self.conn) 
        return True

  
    def bluray(self):
        top = Toplevel()
        newwindow = BlurayGUI(top,self.conn) 

    def rent(self):
        top = Toplevel()
        newwindow = RentGUI(top,self.conn) 

    def returns(self):
        top = Toplevel()
        newwindow = ReturnGUI(top,self.conn) 

    def signup(self):
        top = Toplevel()
        newwindow = SignupGUI(top,self.conn) 

    def payment(self):
        top = Toplevel()
        newwindow = PaymentGUI(top,self.conn) 
    
    def signin(self):
        top = Toplevel()
        
        newwindow = SignInGUI(top,self.conn)     

    
    def createDatabase(self):
        x = CreateDatabase(self.conn)
        x.createMovie()
        x.createCustomer()
        x.createDVD()
        x.createBluray()
        x.createPayment()
        x.createRent()

    def house(self):
        top = Toplevel()
        newwindow = HouseGUI(top,self.conn) 

    def setupDB(self):
        #create connection
        try:
            self.conn = sqlite3.connect(self.DBFile)
        except Error as e:
            print(e)

    


root = Tk()
Cust = GeneralGUI(root)
root.mainloop()
