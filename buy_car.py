import tkinter as tk
from tkinter import *

win4 = tk.Tk()
win4.title("Buy Window")

pic= PhotoImage(master=win4,file="BuySellCar.png")
pic_label = Label(win4,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)

def showall():
    win4.quit()
    win4.destroy()
    import show_all
      
def searchbymake():
    win4.quit()
    win4.destroy()
    import srch_make   
     
def searchbyyear():
    win4.quit()
    win4.destroy()
    import srch_year   
     
def finalize():
    win4.quit()
    win4.destroy()
    import fin_deal
    
def goback():
    win4.quit()
    win4.destroy()
    import next_menu   
    
sc=tk.Button(win4,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Show all Cars",width = 17 ,command=showall)
sc.grid(column=1, row=2,columnspan=1)

mm=tk.Button(win4,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Search by Make",width = 17,command=searchbymake)
mm.grid(column=8, row=2,columnspan=1)

yy=tk.Button(win4,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Search by Year",width = 17,command=searchbyyear)
yy.grid(column=1, row=4,columnspan=1)

fin=tk.Button(win4,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Finalize Deal",width = 17,command=finalize)
fin.grid(column=8, row=4,columnspan=1)

back=tk.Button(win4,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Back to Menu",command=goback)
back.grid(column=4, row=5,columnspan=1)





