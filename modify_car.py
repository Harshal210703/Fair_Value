import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win14 = tk.Tk()
win14.title("Modify Details")

pic= PhotoImage(master=win14,file="BuySellCar.png")
pic_label = Label(win14,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
cursor = conn.cursor()

conn1 = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')
cursor1 = conn1.cursor()

rc1 = tk.StringVar()
make1 = tk.StringVar()
make2 = tk.StringVar()
model1 = tk.StringVar()
model2 = tk.StringVar()
yr1 = tk.IntVar()
yr2 = tk.IntVar()
run1 = tk.IntVar()
run2 = tk.IntVar()
color1 = tk.StringVar()
color2 = tk.StringVar()
fuel1 = tk.StringVar()
fuel2 = tk.StringVar()
sell1 = tk.IntVar()
sell2 = tk.IntVar()
contact1 = tk.StringVar()
contact2 = tk.StringVar()
owner1 = tk.StringVar()
owner2 = tk.StringVar()
cost1 = tk.IntVar()
cost2 = tk.IntVar()

def check1():
    conn.commit()
    conn1.commit()
    win14.quit()
    win14.destroy()
    import sell_car
    
def updatecar():

    cursor.execute("update inventory set make = '" +str(make2.get())+ "', model = '" +str(model2.get())+ "', yr = '" +str(yr2.get())+ "', run = '" +str(run2.get())+ "', colour = '" +str(color2.get())+ "', fuel = '" +str(fuel2.get())+ "', selling_price = '" +str(sell2.get())+ "', stat = '" +str(0)+ "' where rc = '" +str(show.get())+ "'")
    conn.commit()

    cursor1.execute("update ownr set contact_no = '"+str(contact2.get())+"', owner_name = '"+str(owner2.get())+"', owner_price = '"+str(cost2.get())+"' where rc = '" +str(show.get())+ "'" )
    conn1.commit()
    
    win14.quit()
    win14.destroy()
    import sell_car
    
def check():

    try: 
        cursor.execute("select * from inventory where rc = '" +str(show.get())+ "'") 
        ls = cursor.fetchall()

        rf.destroy()
        tinsert.lower()

        if(len(ls)==0):
            rd = tk.Button(win14,font=('Times New Roman',15) ,text='RC not found...Press to continue',command = check1)
            rd.grid(column=7, row=3,columnspan=10)
        else:
            cursor.execute("select rc, make, model, yr, run, colour, fuel, selling_price from inventory where rc = '" +str(show.get())+ "'")
            ls = pd.DataFrame(cursor.fetchall())

            rc1 = ls.iloc[0][0]
            make1 = ls.iloc[0][1]
            model1 = ls.iloc[0][2]
            yr1 = str(ls.iloc[0][3])
            run1 = str(ls.iloc[0][4])
            color1 = ls.iloc[0][5]
            fuel1 = ls.iloc[0][6]
            sell1 = str(ls.iloc[0][7])
            
            win14.setvar(name=rc1, value=ls.iloc[0][0])
            win14.setvar(name=make1, value=ls.iloc[0][1])
            win14.setvar(name=model1, value=ls.iloc[0][2])
            win14.setvar(name=yr1, value=str(ls.iloc[0][3]))
            win14.setvar(name=run1, value=str(ls.iloc[0][4]))
            win14.setvar(name=color1, value=ls.iloc[0][5])
            win14.setvar(name=fuel1, value=ls.iloc[0][6])
            win14.setvar(name=sell1, value=str(ls.iloc[0][7]))
    
            cursor1.execute("select contact_no, rc, owner_name, owner_price from ownr where rc = '" +str(show.get())+ "'")
            ls1 = pd.DataFrame(cursor1.fetchall())
    
            contact1 = ls1.iloc[0][0]
            owner1 = ls1.iloc[0][2]
            cost1 = str(ls1.iloc[0][3])
    
            win14.setvar(name=contact1, value=ls1.iloc[0][0])
            win14.setvar(name=owner1, value=ls1.iloc[0][2])
            win14.setvar(name=cost1, value=str(ls1.iloc[0][3]))
    
            rcin = tk.Label(win14, text="Registration Number : ",  anchor="w", justify=LEFT)
            rcin.grid(column=9, row=2,columnspan=3)
            rcin.configure(font=('Times New Roman',15),width=20)

            rc1f = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=rc1)
            rc1f.grid(column=12, row=2,columnspan=3)
            rc1f.config(state='readonly')

            makein = tk.Label(win14, text="Brand (Make) : ", anchor="w", justify=LEFT) 		
            makein.grid(column=9, row=3,columnspan=3)
            makein.configure(font=('Times New Roman',15),width=20)

            makef = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=make1)
            makef.grid(column=10, row=3,columnspan=3)
            makef.config(state='disabled')
    
            amakef = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=make2)
            amakef.grid(column=13, row=3,columnspan=3)

            modelin = tk.Label(win14, text="Vehicle Type (Model) : ", anchor="w", justify=LEFT) 		
            modelin.grid(column=7, row=4,columnspan=3)
            modelin.configure(font=('Times New Roman',15),width=20)
     
            modelf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=model1) 
            modelf.grid(column=10, row=4,columnspan=3)
            modelf.config(state='disabled')
    
            amodelf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=model2) 
            amodelf.grid(column=13, row=4,columnspan=3)

            yrin= tk.Label(win14, text="Manufacturing Year : ", anchor="w", justify=LEFT) 		
            yrin.grid(column=7, row=5,columnspan=3)
            yrin.configure(font=('Times New Roman',15),width=20)

            yrf= tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=yr1) 
            yrf.grid(column=10, row=5,columnspan=3)
            yrf.config(state='disabled')
    
            ayrf= tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=yr2) 
            ayrf.grid(column=13, row=5,columnspan=3)
    
            runin= tk.Label(win14, text="Kilometer Reading : ", anchor="w", justify=LEFT) 		
            runin.grid(column=7, row=6,columnspan=3)
            runin.configure(font=('Times New Roman',15),width=20)

            runf= tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=run1) 
            runf.grid(column=10, row=6,columnspan=3)
            runf.config(state='disabled')
    
            arunf= tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=run2) 
            arunf.grid(column=13, row=6,columnspan=3)
    
            colorin = tk.Label(win14, text="Vehicle Colour : ", anchor="w", justify=LEFT) 		
            colorin.grid(column=7, row=7,columnspan=3)
            colorin.configure(font=('Times New Roman',15),width=20)

            colorf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=color1) 
            colorf.grid(column=10, row=7,columnspan=3)
            colorf.config(state='disabled')
    
            acolorf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=color2) 
            acolorf.grid(column=13, row=7,columnspan=3)
    
            fuelin = tk.Label(win14, text="Fuel Type : ", anchor="w", justify=LEFT) 		
            fuelin.grid(column=7, row=8,columnspan=3)
            fuelin.configure(font=('Times New Roman',15),width=20)

            fuelf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=fuel1) 
            fuelf.grid(column=10, row=8,columnspan=3)
            fuelf.config(state='disabled')
    
            afuelf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=fuel2) 
            afuelf.grid(column=13, row=8,columnspan=3)

            sellin = tk.Label(win14, text="Selling Price : ", anchor="w", justify=LEFT) 		
            sellin.grid(column=7, row=9,columnspan=3)
            sellin.configure(font=('Times New Roman',15),width=20)

            sellf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=sell1) 
            sellf.grid(column=10, row=9,columnspan=3)
            sellf.config(state='disabled')
    
            asellf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=sell2) 
            asellf.grid(column=13, row=9,columnspan=3)

            costin = tk.Label(win14, text="Owner's Price : ", anchor="w", justify=LEFT) 		
            costin.grid(column=7, row=10,columnspan=3)
            costin.configure(font=('Times New Roman',15),width=20)

            costf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=cost1) 
            costf.grid(column=10, row=10,columnspan=3)
            costf.config(state='disabled')
    
            acostf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=cost2) 
            acostf.grid(column=13, row=10,columnspan=3)
    
            ownerin = tk.Label(win14, text="Owner's Name : ", anchor="w", justify=LEFT) 		
            ownerin.grid(column=7, row=11,columnspan=3)
            ownerin.configure(font=('Times New Roman',15),width=20)

            ownerf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=owner1) 
            ownerf.grid(column=10, row=11,columnspan=3)
            ownerf.config(state='disabled')
    
            aownerf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=owner2) 
            aownerf.grid(column=13, row=11,columnspan=3)
        
            contactin = tk.Label(win14, text="Owner's Mobile : ", anchor="w", justify=LEFT) 		
            contactin.grid(column=7, row=12,columnspan=3)
            contactin.configure(font=('Times New Roman',15),width=20)

            contactf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=contact1) 
            contactf.grid(column=10, row=12,columnspan=3)
            contactf.config(state='disabled')
    
            acontactf = tk.Entry(win14,font=('Times New Roman',15), width=20, textvariable=contact2) 
            acontactf.grid(column=13, row=12,columnspan=3)

            backf=tk.Button(win14,font=('Times New Roman',15), text="Update",command=updatecar)
            backf.grid(column=12, row=13,columnspan=1)
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
        

rf = Frame(win14)
rf.grid(column=0,row=2,columnspan=20)
lshow = tk.Label(rf, text="Enter RC No.: ",font=('times new roman',15)).grid(column=1,row=1,padx=10)

show = tk.StringVar() 
tshow = tk.Entry(rf,font=('times new roman',15), textvariable=show) 
tshow.grid(column=2, row=1)

tinsert=tk.Button(win14,font=('Times New Roman',15), text="Change Details" ,command=check) 
tinsert.grid(column=7, row=3,columnspan=10)


