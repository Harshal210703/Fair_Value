import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win2 = tk.Tk()
win2.title("Register")

pic2=PhotoImage(master=win2,file='Background.png')
pic2_label=Label(win2, image= pic2).grid(column=0,row=0,columnspan=5, rowspan=10)

name = tk.StringVar()
tcname = tk.Entry(win2,font=('arial',15), width=15, textvariable=name)
tcname.grid(column=2, row=1,columnspan=3)

pas = tk.StringVar() 
upass = tk.Entry(win2,font=('arial',15), width=15, textvariable=pas, show="*") 
upass.grid(column=2, row=2,columnspan=3)

def reg():
    
    try: 
        conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
        
        cursor1 = conn.cursor()
        cursor1.execute("insert into login ( user_id, pwd) values('"+str(name.get())+"', '"+str(pas.get())+"')")
            
        conn.commit()
        
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        
    win2.quit()
    win2.destroy()
    import main_menu
    
lid = tk.Label(win2, text="New Login Id. : ")
lid.grid(column=0, row=1,columnspan=3)
lid.configure(font=('Times New Roman',15), width=15,bg='white')

pwd = tk.Label(win2, text="New Password : ") 		
pwd.grid(column=0, row=2,columnspan=3)
pwd.configure(font=('Times New Roman',15), width=15,bg='white')

rd = tk.Button(win2,font=('Times New Roman',15) ,text='Register!',command = reg)
rd.grid(column=2, row=3,columnspan=3)


    

