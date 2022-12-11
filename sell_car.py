import tkinter as tk
from tkinter import *

win5 = tk.Tk()
win5.title("Sell Window")

pic= PhotoImage(master=win5,file="BuySellCar.png")
pic_label = Label(win5,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)

def entercar():
    win5.quit()
    win5.destroy()
    import enter_details
    
def showowner():
    win5.quit()
    win5.destroy()
    import show_owner
    
def finalized():
    win5.quit()
    win5.destroy()
    import show_final
    
def pending():     
    win5.quit()
    win5.destroy()
    import show_pending

def modifycar():
    win5.quit()
    win5.destroy()
    import modify_car    

def deletecar():
    win5.quit()
    win5.destroy()
    import delete_car
    
def goback():
    win5.quit()
    win5.destroy()
    import next_menu

ec=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Add Car Details",width = 17 ,command=entercar)
ec.grid(column=1, row=2,columnspan=1)

fin=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Modify Car Details",width = 17,command=modifycar)
fin.grid(column=1, row=3,columnspan=1)

fin1=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Delete Car Details",width = 17,command=deletecar)
fin1.grid(column=1, row=4,columnspan=1)

eo=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Show Owner Details",width = 17,command=showowner)
eo.grid(column=8, row=2,columnspan=1)

pen1=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Finalized Deals",width = 17,command=finalized)
pen1.grid(column=8, row=3,columnspan=1)

pen=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Pending Transactions",width = 17,command=pending)
pen.grid(column=8, row=4,columnspan=1)

back=tk.Button(win5,font=('times new roman',16), bd=4, fg="blue", bg="grey", text="Back to Menu",command=goback)
back.grid(column=4, row=5,columnspan=1)



