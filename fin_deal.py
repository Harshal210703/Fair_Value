import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win13 = tk.Tk()
win13.title("Deal Window")

pic= PhotoImage(master=win13,file="BuySellCar.png")
pic_label = Label(win13,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

def check():
 
    f = ttk.LabelFrame(win13)
    f.grid(column=12, row=4)

    f1 = tk.Label(f, text="Registration No.",font=('Times New Roman',15)).grid(column=0,row=0)
    f2 = tk.Label(f, text="Make",font=('Times New Roman',15)).grid(column=1,row=0)
    f3 = tk.Label(f, text="Model",font=('Times New Roman',15)).grid(column=2,row=0)
    f4 = tk.Label(f, text="Year",font=('Times New Roman',15)).grid(column=3,row=0)
    f5 = tk.Label(f, text="Run K.M.",font=('Times New Roman',15)).grid(column=4,row=0)
    f6 = tk.Label(f, text="Colour",font=('Times New Roman',15)).grid(column=5,row=0)
    f7 = tk.Label(f, text="Fuel Type",font=('Times New Roman',15)).grid(column=6,row=0)
    f8 = tk.Label(f, text="Price",font=('Times New Roman',15)).grid(column=7,row=0)

    conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute("select rc, make, model, yr, run, colour, fuel, selling_price from inventory where rc = '" +str(show.get())+ "'")

    ls = pd.DataFrame(cursor.fetchall())
    
    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(f)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i+1, column=j,padx=10,pady=10)
            b.config(state = "readonly")

    cursor.execute("update inventory set stat = '"+str(1)+"' ")        
    conn.commit()
    
def deal():
    
    conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
    cursor1 = conn.cursor()
    cursor1.execute("insert into ord (rc, amt_paid, amt_pending) values('"+str(show.get())+"','"+str(shown.get())+"','"+str(bal.get())+"')")    
    conn.commit()
    insert11=tk.Button(win13,font=('Times New Roman',15), text="CONGRATULATIONS!!!!" ,command=fin) 
    insert11.grid(column=7, row=10,columnspan=10)

def fin():
    win13.quit()
    win13.destroy()
    import buy_car
    
rf = Frame(win13)
rf.grid(column=0,row=2,columnspan=20)
lshow = tk.Label(rf, text="Enter RC No.: ",font=('times new roman',15)).grid(column=1,row=1,padx=10)

show = tk.StringVar() 
tshow = tk.Entry(rf,font=('times new roman',15), textvariable=show) 
tshow.grid(column=2, row=1)

insert=tk.Button(win13,font=('Times New Roman',15), text="Check!" ,command=check) 
insert.grid(column=7, row=3,columnspan=10)

rf1 = Frame(win13)
rf1.grid(column=0,row=8,columnspan=20)
lshow1 = tk.Label(rf1, text="Enter Amount : ",font=('times new roman',15)).grid(column=1,row=6,padx=10)

shown = tk.StringVar() 
tshow1 = tk.Entry(rf1,font=('times new roman',15), textvariable=shown)
tshow1.grid(column=2, row=6)

bshow1 = tk.Label(rf1, text="Amount Balance: ",font=('times new roman',15)).grid(column=1,row=8,padx=10)
bal = tk.StringVar() 
bshow1 = tk.Entry(rf1,font=('times new roman',15), textvariable=bal)
bshow1.grid(column=2, row=8)

insert1=tk.Button(win13,font=('Times New Roman',15), text="Deal!" ,command=deal) 
insert1.grid(column=7, row=10,columnspan=10)

def back():
    win13.quit()
    win13.destroy()
    import buy_car
        
back=tk.Button(win13,font=('Times New Roman',15), text="Back to Previous Menu",command=back)
back.grid(column=12, row=13,columnspan=1)



