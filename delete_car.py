import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win15 = tk.Tk()
win15.title("Delete Details")

pic= PhotoImage(master=win15,file="BuySellCar.png")
pic_label = Label(win15,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
cursor = conn.cursor()

conn1 = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
cursor1 = conn1.cursor()

def check1():

    conn.commit()
    conn1.commit()
    win15.quit()
    win15.destroy()
    import sell_car    
    
def check():

    try: 
        cursor.execute("select * from inventory where rc = '" +str(show.get())+ "'") 
        ls = cursor.fetchall()

        rf.destroy()
        tinsert.lower()

        if(len(ls)==0):
            rd = tk.Button(win15,font=('Times New Roman',15) ,text='RC not found...Press to continue',command = check1)
            rd.grid(column=7, row=3,columnspan=10)
        else:

            cursor1.execute("delete from ownr where rc = '" +str(show.get())+ "'")
            conn1.commit()
            
            cursor.execute("delete from inventory where rc = '" +str(show.get())+ "'")
            conn.commit()

            win15.quit()
            win15.destroy()
            import sell_car    
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        

rf = Frame(win15)
rf.grid(column=0,row=2,columnspan=20)
lshow = tk.Label(rf, text="Enter RC No.: ",font=('times new roman',15)).grid(column=1,row=1,padx=10)

show = tk.StringVar() 
tshow = tk.Entry(rf,font=('times new roman',15), textvariable=show) 
tshow.grid(column=2, row=1)

tinsert=tk.Button(win15,font=('Times New Roman',15), text="Delete Details" ,command=check) 
tinsert.grid(column=7, row=3,columnspan=10)

