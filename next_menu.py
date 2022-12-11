import tkinter as tk
from tkinter import *

win3 = tk.Tk()
win3.title("Next Window")

pic= PhotoImage(master=win3,file="Buysell.png")
pic_label = Label(win3,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)

def bcar():
    win3.quit()
    win3.destroy()
    import buy_car
    
def scar():
    win3.quit()
    win3.destroy()
    import sell_car
    
bc = tk.Button(win3,font=('arial',12), bd=4, fg="blue", bg="grey", text="BUY A CAR", height =2, width = 13, command=bcar)
bc.grid(column=3, row=5)

sc = tk.Button(win3,font=('arial',12), bd=4, fg="blue", bg="grey", text="SELL A CAR",height =2, width = 13, command=scar)
sc.grid(column=5, row=5,columnspan=2)

