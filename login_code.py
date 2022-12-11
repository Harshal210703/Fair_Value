import tkinter as tk
import os
from tkinter import *
import mysql.connector
from mysql.connector import Error

win1 = tk.Tk()
win1.title("Login")

pic2=PhotoImage(master=win1,file='Background.png')
pic2_label=Label(win1, image= pic2).grid(column=0,row=0,columnspan=5, rowspan=10)

name = tk.StringVar()
tcname = tk.Entry(win1,font=('arial',15), width=15, textvariable=name)
tcname.grid(column=1, row=1,columnspan=3)

pas = tk.StringVar() 
upass = tk.Entry(win1,font=('arial',15), width=15, textvariable=pas, show="*") 
upass.grid(column=1, row=2,columnspan=3)

def check():
    
    try: 
        conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
        cursor = conn.cursor() 
        cursor.execute("select * from login where user_id ='"+name.get()+"' and pwd = '"+pas.get()+"'") 
        ls = cursor.fetchall()
        if(len(ls)>0):
            win1.quit()
            win1.destroy()
            import next_menu
            
        else: 
            rd = tk.Button(win1,font=('Times New Roman',15) ,text='Wrong User Name or Password!',command = check)
            rd.grid(column=1, row=3,columnspan=3)
        
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")

lid = tk.Label(win1, text="Login Id. : ")
lid.grid(column=0, row=1,columnspan=3)
lid.configure(font=('Times New Roman',15), width=15,bg='white')

pwd = tk.Label(win1, text="Password : ") 		
pwd.grid(column=0, row=2,columnspan=3)
pwd.configure(font=('Times New Roman',15), width=15,bg='white')

rd = tk.Button(win1,font=('Times New Roman',15) ,text='Login!',command = check)
rd.grid(column=1, row=3,columnspan=3)


    

