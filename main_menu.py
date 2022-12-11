import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Main Window")

pic= PhotoImage(master=win,file="Fairvalue.png")
pic_label = Label(win,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)

def login():
    win.quit()
    win.destroy()
    import login_code 

def register():
    win.quit()
    win.destroy()
    import register_code
    
Cust = tk.Button(win,font=('arial',12), bd=4, fg="blue", bg="grey", text="LOGIN", height =3, width = 13, command=login)
Cust.grid(column=3, row=5)

Emp = tk.Button(win,font=('arial',12), bd=4, fg="blue", bg="grey", text="REGISTER",height =3, width = 13, command=register)
Emp.grid(column=5, row=5,columnspan=2)

