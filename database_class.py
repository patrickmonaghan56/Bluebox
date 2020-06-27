from datetime import datetime
import sqlite3


#CUSTOMER
class Customer:
    def __init__(self,conn):
        self.conn = conn

    def create(self,data):
        sql = ''' INSERT INTO Customer(FirstName,MiddleName,LastName,Date_Of_Birth,Email,Rented,Max_Rented,Charge_Card_No,Password,Username,Can_Rent) VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def read(self, data):
        string=''
        string=data
        C_ID=int(string)
        print(C_ID)
        conn=self.conn
        cur = conn.cursor()
        cur.execute("SELECT * FROM Customer WHERE C_ID=?", (C_ID,))
        rows = cur.fetchall()
        return rows  

    def signin(self,username,password ):
        conn=self.conn
        cur = conn.cursor()
        cur.execute("SELECT * FROM Customer WHERE Username=? AND Password=?", (username,password))
        rows = cur.fetchall()
        
        if(len(rows)==1):
            return True  
        else:
            return False    

    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Customer")
        rows = cur.fetchall()
        return rows  

    def update(self,data):
        sql = ''' UPDATE Customer
                  SET  FirstName = ?, 
                    MiddleName = ?, 
                    LastName = ?
                  WHERE C_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def updateUsername(self,data):
        sql = ''' UPDATE Customer
                  SET Username = ?
                  WHERE C_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def updatePassword(self,data):
        sql = ''' UPDATE Customer
                  SET Password = ?
                  WHERE C_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def update_Charge_Card(self,data):
        sql = ''' UPDATE Customer
                  SET Charge_Card_No = ? 
                  WHERE C_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()


    def delete(self,data):
        sql = 'DELETE FROM Customer WHERE C_ID=?'
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()



#MOVIE 

class Movie:
    def __init__(self,conn):
        self.conn = conn

    def create(self,data):
        sql = ''' INSERT INTO Movie(Title,Description, Rating, Year,Quality, Genre, DVD_Quantity, BLU_Ray_Quantity,CopyRentDVD,CopyRentedBluRay,IMGFile)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def getmovie(self,data):
        cur = self.conn.cursor()
        cur.execute("SELECT Title FROM Movie WHERE M_ID=?", (data,))
        rows = cur.fetchall()
        return rows  

    def getpath(self,data):
        cur = self.conn.cursor()
        cur.execute("SELECT IMGFile FROM Movie WHERE M_ID=?", (data,))
        rows = cur.fetchone()
        
        rows=rows[0]
        return rows  
        


    def read(self, data):
        conn=self.conn
        cur = conn.cursor()
        cur.execute("SELECT * FROM Movie WHERE M_ID=?", (data,))
        rows = cur.fetchall()
        return rows  

    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Movie")
        rows = cur.fetchall()
        return rows  

    def Search(self,genre,rating):
        
        x = bool(genre == 'Critically Acclaimed')
        y = bool(rating == 'None')
        if(x and y):
            sql = "SELECT * FROM Movie"
        else:
            if(rating == 'None'):
                sql = "SELECT * FROM Movie WHERE Genre=?"
                data = [
                    genre
                ]
            if(genre == 'Critically Acclaimed'):
                sql = "SELECT * FROM Movie WHERE Rating=?"
                data=[
                rating
                ]
            if(rating!='None' and genre!='Critically Acclaimed'):
                sql = "SELECT * FROM Movie WHERE Genre=? AND Rating=?"
                data=[
                genre,
                rating
                ]
        cur = self.conn.cursor()
        if(x and y):
            cur.execute(sql)
        else:
            cur.execute(sql,data)
        
        rows = cur.fetchall()
        return rows  

    def Searchbar(self,Search_Text):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Movie WHERE Title LIKE ?",('%'+Search_Text+'%',))
        rows = cur.fetchall()
        return rows  

    def updateDVD(self,data):
        sql = ''' UPDATE Movie
                  SET DVD_Quantity = DVD_Quantity + 1
                  WHERE M_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()

    def updateBluray(self,data):
        sql = ''' UPDATE Movie
                  SET BLU_Ray_Quantity = BLU_Ray_Quantity + 1
                  WHERE M_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def updateQuality(self,data):
        sql = ''' UPDATE Movie
                  SET Quality = ?,
                  WHERE M_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        
    def updateRent(self,Type,data):
        cur = self.conn.cursor()
        if(Type == 'b'):
            
            sql = ''' UPDATE Movie
                      SET CopyRentedBluRay = CopyRentedBluRay + 1
                      WHERE M_ID = ?'''
        else:
            
            sql = ''' UPDATE Movie
                      SET CopyRentDVD = CopyRentDVD + 1
                      WHERE M_ID = ?'''
        string = ''
        string = data
        M_ID = int(string)
        cur.execute(sql, (M_ID,))
        self.conn.commit()

    def updateReturn(self,Type,data):
       
        if(Type=='b'):
            sql = ''' UPDATE Movie
                      SET CopyRentedBluRay = CopyRentedBluRay - 1
                      WHERE M_ID = ?'''
        else:
            sql = ''' UPDATE Movie
                      SET CopyRentDVD = CopyRentDVD - 1
                      WHERE M_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def delete(self,data):
        sql = 'DELETE FROM Movie WHERE M_ID=?'
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()


#DVD
class DVD:
    def __init__(self,conn):
        self.conn = conn
        

    def create(self,data):
        conn = self.conn
        sql = ''' INSERT INTO DVD(ID_Movie,Cost,Rented_Out)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        self.dMovie = Movie(conn)
        M_ID = data[0]
        self.dMovie.updateDVD(M_ID)


    def read(self, data):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM DVD WHERE DVD_ID=?", (data,))
        rows = cur.fetchall()
        return rows  

    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM DVD")
        rows = cur.fetchall()
        return rows  

    def update(self,data):
        sql = ''' UPDATE DVD
                  SET Cost = ?
                  WHERE DVD_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()


    def updateRent(self,data,rentedout):
        print(data)
        sql = ''' UPDATE DVD
                  SET Rented_Out = ?
                  WHERE DVD_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (rentedout,data))
        self.conn.commit()

    def getcost(self,data):
        cur = self.conn.cursor()
        cur.execute('SELECT Cost FROM DVD WHERE DVD_ID=?', (data,))
        rows = cur.fetchall()
        return rows  


    def delete(self,data):
        sql = 'DELETE FROM DVD WHERE DVD_ID=?'
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()

#BLU_RAY
class BLU_RAY:
    def __init__(self,conn):
        self.conn = conn

    def create(self,data):
        conn = self.conn
        sql = ''' INSERT INTO BLU_RAY(ID_Movie,Cost,Rented_Out)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        self.dMovie = Movie(conn)
        M_ID = data[0]
        self.dMovie.updateBluray(M_ID)
    
    def read(self, data):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM BLU_RAY WHERE DVD_id=?", (data,))
        rows = cur.fetchall()
        return rows  

    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM BLU_RAY")
        rows = cur.fetchall()
        return rows  

    def update(self,data):
        sql = ''' UPDATE BLU_RAY
                  SET Cost = ?
                  WHERE BLU_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def updateRent(self,data,rentedout):
        print(data)
        sql = ''' UPDATE BLU_RAY
                  SET Rented_Out = ?
                  WHERE BLU_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (rentedout,data))
        self.conn.commit()
    
    def getcost(self,data):
        cur = self.conn.cursor()
        cur.execute('SELECT Cost FROM BLU_RAY WHERE BLU_ID=?', (data,))
        rows = cur.fetchall()
        return rows  

    def delete(self,data):
        sql = 'DELETE FROM BLU_RAY WHERE BLU_ID=?'
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()
#RENT 
class RENT:
    def __init__(self,conn):
        self.conn = conn
        self.dbcustomer = Customer(conn)

    #logic validation
    def validate(self,data):
        conditions=(
             data[1],#C_ID
             data[0],#Date
             data[2],#bluID
             data[3]#dvdid
             )
        
        #if customer ID valid
        if(len(self.dbcustomer.read(conditions[0]))==1):
            #if movie id still rented out
            if(data[4]=='d'):
                x = self.Rented(data[4],conditions)
            else:
                x = self.Rented(data[4],conditions)
            if(x[0]): 
                return False
            else:  
              return True
        else:
            return False

    #success or failure message
    def message(self,success):
        if(success):
            print("\nRENTAL ADDED")
        else: 
            print("\nRENTAL EXISTS ALREADY")


    #add a Rental
    def add(self,data):

        #logic validation
        if(self.validate(data)):
            #add Rental in database 
            self.create(data)

            #display success message
            self.message(True)

            #display all the Rentals
            print(self.readAll())

        else:
            #display failure message
            self.message(False)

    #type can take the values d (for DVD) or 
    #b (for bluray)
    def create(self,data):
        conn = self.conn

        sql = ''' INSERT INTO RENT(Date_Rent,C_ID,BLU_ID,DVD_ID,type,DateReturn)
                  VALUES(?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()
        self.dMovie = Movie(conn)
        self.dDVD = DVD(conn)
        self.dBLURAY = BLU_RAY(conn)
        if(data[4]=='d'):
            sql = "SELECT ID_Movie FROM DVD WHERE DVD_ID=?"
            D_ID = int(data[3])
            cur.execute(sql, (D_ID,))
            self.dDVD.updateRent(D_ID,1)
        else:
            sql = "SELECT ID_Movie FROM BLU_RAY WHERE BLU_ID=?"
            B_ID = int(data[2])
            cur.execute(sql, (B_ID,))
            self.dBLURAY.updateRent(B_ID,1)
        temp=cur.fetchall()
        string = str(temp[0])
        M_ID = int(string[1])
        self.dMovie.updateRent(data[5],M_ID)
        
        

    def Rented(self, Type, data):
        cur = self.conn.cursor()
        
        DVD_ID=data[3]
        BLU_ID=data[2]
        print(Type)
        if(Type=='b'): 
            print(BLU_ID)
            cur.execute('''SELECT Rented_out FROM BLU_RAY WHERE BLU_ID=? ''', (BLU_ID,))
        else:
            print(DVD_ID)
            cur.execute('''SELECT Rented_out FROM DVD WHERE DVD_ID=? ''', (DVD_ID,))
        rows = cur.fetchall()
        print(rows[0])
        return rows[0]  

    def MostRecent(self, Type, data):
        cur = self.conn.cursor()
        
        Disk_ID=int(data[1])
        if(Type=='b'): 
            
            cur.execute('''SELECT MAX(Date_Rent) FROM RENT WHERE BLU_ID=? ''', (Disk_ID,))
        else:
            
            cur.execute('''SELECT MAX(Date_Rent) FROM RENT WHERE DVD_ID=? ''', (Disk_ID,))
        rows = cur.fetchall()
        print(rows)
        rows=str(rows)
        return rows  

    #return read for validation
    def read(self,conn,Type, conditions):
        self.conn = conn
        cur = self.conn.cursor()
        
        if(Type=='b'):
         sql = ''' SELECT * FROM RENT WHERE BLU_ID=? AND RentDate=? AND C_ID=?  '''
         cur.execute(sql, (conditions))
        else:
         sql = ''' SELECT * FROM RENT WHERE DVD_ID=? AND RentDate=? AND C_ID=?  '''
        cur.execute(sql, (conditions))
        rows = cur.fetchall()
        return rows 


    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM RENT")
        rows = cur.fetchall()
        return rows  

    def update(self,Type,data):
        if Type=='b':
         sql = ''' UPDATE RENT
                  SET DateReturn =?
                  WHERE BLU_ID = ? AND Date_Rent=?'''
        else:
         sql = ''' UPDATE RENT
                  SET DateReturn =?
                  WHERE DVD_ID = ? AND Date_Rent=?'''

        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def getrent(self,Type,data,Date_Rent):
        cur = self.conn.cursor()
        B_ID = data
        print(B_ID)
        print(Date_Rent)
        if (Type=='b'):
         sql = 'SELECT C_ID FROM RENT WHERE BLU_ID=? AND Date_Rent=?'
        else: 
         sql = 'SELECT C_ID FROM RENT WHERE DVD_ID=? AND Date_Rent=?'
        cur.execute(sql,(B_ID,Date_Rent))
        rows = cur.fetchall()
        print(rows)
        return rows  



    def delete(self,Type,data):
        if (Type=='b'):
         sql = 'DELETE FROM RENT WHERE BLU_ID=?'
        else: 
         sql = 'DELETE FROM RENT WHERE DVD_ID=?'
        
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()

#PAYMENT
class PAYMENT:
    def __init__(self,conn):
        self.conn = conn
        self.drent = RENT(conn)
        self.dBLURAY = BLU_RAY(conn)
        self.dDVD = DVD(conn)
        self.dbcustomer = Customer(conn)
    
    #datepayment = returndate
    def create(self,data):
        
        sql = ''' INSERT INTO PAYMENT(C_ID,P_AMOUNT,Receipt,DatePayment)
                  VALUES(?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    #logic validation
    def validate(self,Type,data):
        #number of Disk_ID with the same id <=1 (theres been at least one rent with this disk)
        
        Date_Rent = self.drent.MostRecent(Type,data)
        duration = datetime.strptime(
            Date_Rent[3:29],'%Y-%m-%d %H:%M:%S.%f'
            )
        Date_Rent = Date_Rent[3:29]
        print(Date_Rent)
        if(self.drent.getrent(Type,data[1],Date_Rent)):  
            wasrented = True
        else:          
            return False
        if(wasrented):            
            if(Type == 'b'):
                cost = self.dBLURAY.getcost(data[1])
                cost = cost[0]
            else:
                cost = self.dDVD.getcost(data[1]) 
                cost = cost[0]
            
            duration = data[0]-duration
            print(duration)
            #day is how many days of the rental, date of the return - start of rent + 1 day
            day = datetime(1,1,2)-datetime(1,1,1)
            if(duration<day):
                duration=1
            else:
                duration = duration.days+1
            
            C_ID = self.drent.getrent(Type,data[1],Date_Rent)
            C_ID=C_ID[0]
            P_AMOUNT = duration * cost[0]
            receipt ='Thank you for renting with us, %d will be charged to your card'
            data=[
            data[0],
            data[1],  
            Date_Rent          
            ]
            if(Type == 'b'):
                self.dBLURAY.updateRent(data[1],0)
            else:
                self.dDVD.updateRent(data[1],0) 
            self.drent.update(Type,data)
            data=[
                C_ID[0],
                P_AMOUNT,
                receipt,
                data[0]]
                
            
            self.create(data)
           
        return wasrented

    #success or failure message
    def message(self,success):
        if(success):
            print("\nRETURN ACCEPTED")
        else: 
            print("\nINVALID ID")


    #adds payment for the return date
    def add(self,Type,data):
        
        #logic validation
        if(self.validate(Type,data)):
            #add  in database 

            #display success message
            self.message(True)

        else:
            #display failure message
            self.message(False)


    def read(self, data):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM PAYMENT WHERE P_ID=?", (data,))
        rows = cur.fetchall()
        return rows  

    def readAll(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM PAYMENT")
        rows = cur.fetchall()
        return rows  

    def updateCharge(self,data):
        sql = ''' UPDATE PAYMENT
                  SET P_AMOUNT= ? 
                  WHERE P_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def updateC_ID(self,data):
        sql = ''' UPDATE PAYMENT
                  SET C_ID= ? 
                  WHERE P_ID = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def delete(self,data):
        sql = 'DELETE FROM PAYMENT WHERE P_ID=?'
        cur = self.conn.cursor()
        cur.execute(sql, (data,))
        self.conn.commit()





class CreateDatabase:
    def __init__(self,conn):
        self.conn = conn

    def createMovie(self):
        sql = '''CREATE TABLE Movie(M_ID INTEGER PRIMARY KEY AUTOINCREMENT, Title varchar(40), Description varchar(400), Rating varchar(5), Year int, Quality varchar(10),Genre varchar(20), DVD_Quantity int, BLU_Ray_Quantity int, CopyRentDVD int, CopyRentedBluRay int, IMGFile varchar(200))'''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def createCustomer(self):
        sql = '''CREATE TABLE Customer(C_ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName varchar(15),MiddleName varchar(10), LastName varchar(20),Date_Of_Birth date, Email Varchar(70),Rented int,Max_Rented int,Charge_Card_No varchar(16),Password varchar(20),Username varchar(20)UNIQUE,Can_Rent boolean)'''
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def createDVD(self):
        sql = 'CREATE TABLE DVD (DVD_ID INTEGER PRIMARY KEY AUTOINCREMENT, ID_Movie int, Cost real,Rented_out boolean, FOREIGN KEY(ID_Movie) REFERENCES Movie(M_ID))'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def createBluray(self):
        sql = 'CREATE TABLE BLU_RAY(BLU_ID INTEGER PRIMARY KEY AUTOINCREMENT, ID_Movie int, Cost real,Rented_out boolean, FOREIGN KEY(ID_Movie) REFERENCES Movie(M_ID))'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def createPayment(self):
        sql = 'CREATE TABLE PAYMENT (P_ID INTEGER PRIMARY KEY AUTOINCREMENT, C_ID int, P_Amount Double, Receipt varchar(100), DatePayment date, FOREIGN KEY(C_ID) REFERENCES Customer(C_ID))'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def createRent(self):
        sql = 'CREATE TABLE RENT (Date_Rent datetime,C_ID int, BLU_ID int, DVD_ID int, type char, DateReturn datetime,  FOREIGN KEY(C_ID) REFERENCES Customer(C_ID), FOREIGN KEY(DVD_ID) REFERENCES DVD(DVD_ID), FOREIGN KEY(BLU_ID) REFERENCES BLU_RAY(BLU_ID))'
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
