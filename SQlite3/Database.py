from tkinter import *
import sqlite3

root = Tk()
root.title("Database Address Book")
root.iconbitmap()

#Databases
#Creating a database or connect to one

conn = sqlite3.connect("Address_book.db")

#Creating a Cursor
#Cursor class is an instance using which you can invokemethods that execute SQlite statements,
#fetch data from the result sets of the queries.

c = conn.cursor()

#Creating a table
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text
        city text
        state text
        zipcode integer
        )""")
print("Table created successfully")

def submit():
    #create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    #Create cursor
    c=conn.cursor()
    #Insert into the table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",{
        'first_name':e1.get(),
        'last_name':e2.get(),
        'address':e3.get(),
        'city':e4.get(),
        'state':e5.get(),
        'zipcode':e6.get()
    })
    print('Address inserted successfully')
conn.commit()
conn.close()
#clear the text boxes
e1.delete(0,END)
e2.delete(0,END)
e3.delete(0,END)
e4.delete(0,END)
e5.delete(0,END)
e6.delete(0,END)

#label


#commit change
conn.commit()