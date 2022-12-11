import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win12 = tk.Tk()
win12.title("Search Window")

pic= PhotoImage(master=win12,file="BuySellCar.png")
pic_label = Label(win12,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

def check():
 
    f = ttk.LabelFrame(win12)
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
    cursor.execute("select rc, make, model, yr, run, colour, fuel, selling_price from inventory where stat = 0 and yr = '" +str(show.get())+ "'")
    
    ls = pd.DataFrame(cursor.fetchall())

    for i in range(0, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(f)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i+1, column=j,padx=10,pady=10)
            b.config(state = "readonly")

    conn.commit()

rf = Frame(win12)
rf.grid(column=0,row=2,columnspan=20)
lshow = tk.Label(rf, text="Enter Year: ",font=('times new roman',15)).grid(column=1,row=1,padx=10)
show = tk.IntVar() 
tshow = tk.Entry(rf,font=('times new roman',15), textvariable=show) 
tshow.grid(column=2, row=1)
insert=tk.Button(win12,font=('Times New Roman',15), text="Check!" ,command=check) 
insert.grid(column=7, row=3,columnspan=10)

def back():
    win12.quit()
    win12.destroy()
    import buy_car
    
back=tk.Button(win12,font=('Times New Roman',15), text="Back to Previous Menu",command=back)
back.grid(column=12, row=13,columnspan=1)



