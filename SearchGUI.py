from tkinter import*
import tkinter as tk
from tkinter import ttk

import sqlite3

#sqlite database 
from sqlite3 import Error

   
#classes for the database 
from database_class import Movie

class SearchGUI:
    def __init__(self,master,conn):
        self.master = master 
        self.conn = conn 
        self.dMovie = Movie(conn)

        master.configure(bg='dodgerblue')
        master.title("Movie")

        self.button1= Button(self.master,text='Update',bg='lightsteelblue',fg='navy', command=self.update)
        self.button1.grid(row=2,column=1,ipadx=15,pady=20,sticky=W)