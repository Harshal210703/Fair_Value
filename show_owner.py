import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win7 = tk.Tk()
win7.title("Owner Window")

pic= PhotoImage(master=win7,file="BuySellCar.png")
pic_label = Label(win7,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

f = ttk.LabelFrame(win7)
f.grid(column=12, row=2)

f1 = tk.Label(f, text="Contact No.",font=('Times New Roman',15)).grid(column=0,row=0)
f2 = tk.Label(f, text="Registration No",font=('Times New Roman',15)).grid(column=1,row=0)
f3 = tk.Label(f, text="Owner's Name",font=('Times New Roman',15)).grid(column=2,row=0)
f4 = tk.Label(f, text="Owner's Price",font=('Times New Roman',15)).grid(column=3,row=0)
        
conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
cursor = conn.cursor()
cursor.execute("select contact_no, rc, owner_name, owner_price from ownr ")

ls = pd.DataFrame(cursor.fetchall())
  
for i in range(0, len(ls.index)):
    for j in range(0, len(ls.columns)):
        b = tk.Entry(f)
        b.insert(0, ls.iloc[i][j])
        b.grid(row=i+1, column=j,padx=10,pady=10)
        b.config(state = "readonly")

conn.commit()

def back():
    win7.quit()
    win7.destroy()
    import sell_car
    
back=tk.Button(win7,font=('Times New Roman',15), text="Back to Previous Menu",command=back)
back.grid(column=12, row=13,columnspan=1)



