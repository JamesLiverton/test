from tkinter import *
from tkinter.ttk import *
import sqlite3
from datetime import date

class Database():
    def __init__(self): # creates a connection with the database
        self.db = 'database.db'
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()

    def fetch_data(self):
        ids = []
        names = []
        startdates = []
        returndates = []
        location = []

        sql = '''SELECT * FROM machines'''
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        return [rows] # allows for all of the database to be stored in one variable

    def add_machine(self, data):
        sql = '''INSERT INTO machines(id, machineName, RentStartDate, ReturnDate, Location)
        VALUES (?,?,?,?,?);'''
        self.cur.execute(sql, data)
        self.conn.commit()
    
    def location_change(self,data):
        sql = '''UPDATE machines
            SET Location = ?
            WHERE id = ?;'''
        self.cur.execute(sql, data)
        self.conn.commit() 

db = Database()
#db.add_machine(('PLL126','hedgecutter','1/04/2021','7/04/2021','Felixstowe'))


data = db.fetch_data()
today = date.today()
for d in data:
    for count, entity in enumerate(d):
        temp = entity[3]
        temp = temp.split('/')

        if int(temp[2]) <= today.year:
            if int(temp[1]) <= today.month:
                if int(temp[0]) <= today.day:
                    db.location_change(("Yard", entity[0]))


def main_window():
    tk = Tk()
    canvas = Canvas(tk, width='150', height='300')#to hold image
    canvas.grid(row=0,column=0)

    

    tk.geometry("1500x1000") #whole window size
    tk.wm_iconbitmap('assets/favicon.ico')#sets logo of the window - must use .ico files
    tk.title("James Super Duper program he made himself for Tracey x")

    Button(tk, text='Tractor 1', command=tractor1_window).grid(row=0, column=1) #button to open machine 

    #logo
    img = PhotoImage(file="assets/pllLogo.png") #loads image and assigns it to variable to make usable

    #display data
    canvas.create_image(0,0, anchor=NW, image=img)
    tree = Treeview(tk) # creates a tree
    tree['columns']=('id','machineName','RentStartDate','ReturnDate','Location') #creates names of columns
    tree['show'] = 'headings' 

    tree.column("id", width=150)
    tree.column("machineName", width=200)
    tree.column("RentStartDate", width=150)
    tree.column("ReturnDate", width=150)
    tree.column("Location", width=100)
    
    tree.heading("id", text="Machine Identification", anchor=W)
    tree.heading("machineName", text="Machine Name")
    tree.heading("RentStartDate", text="Hire Start Date")
    tree.heading("ReturnDate", text="Hire Return Date")
    tree.heading("Location", text="Location")

    data = db.fetch_data()
    
    for d in data:
        for entity in d:
            tree.insert('','end',values=[entity[0],entity[1],entity[2],entity[3],entity[4]])

    tree.grid(row=1, column=1)
    
    tk.mainloop()

def tractor1_window():
    tk = Tk()
    tk.title('Tractor1Window')


main_window()
