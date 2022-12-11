import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import Error

win6 = tk.Tk()
win6.title("Details Window")

pic= PhotoImage(master=win6,file="BuySellCar.png")
pic_label = Label(win6,image=pic).grid(column=7,row=0,columnspan=10, rowspan=20)

def insert():
    try: 
        conn = mysql.connector.connect(host='localhost', port='3306', database='harshal',user='root',password='root',charset='utf8', auth_plugin='mysql_native_password')

        rc2 = rc1.get()
        make2 = make1.get()
        model2 = model1.get()
        yr2 = yr1.get()
        run2 = run1.get()
        color2 = color1.get()
        fuel2 = fuel1.get()
        sell2 = sell1.get()
        cost2 = cost1.get()
        owner2 = owner1.get()
        contact2 = contact1.get()
        
        cursor1 = conn.cursor()
        cursor1.execute("insert into inventory ( rc, make, model, yr, run, colour, fuel, selling_price, stat) values('"+str(rc2)+"', '"+str(make2)+"','"+str(model2)+"','"+str(yr2)+"','"+str(run2)+"', '"+str(color2)+"', '"+str(fuel2)+"', '"+str(sell2)+"', '"+str(0)+"')")
            
        cursor = conn.cursor()
        cursor.execute("insert into ownr (contact_no, rc, owner_name, owner_price) values ('"+str(contact2)+"', '"+str(rc2)+"', '"+str(owner2)+"', '"+str(cost2)+"')")

        conn.commit()
        
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")

        win6.quit()
        win6.destroy()
        import sell_car
        
def back():
    win6.quit()
    win6.destroy()
    import sell_car
       
rcin = tk.Label(win6, text="Registration Number : ",  anchor="w", justify=LEFT)
rcin.grid(column=9, row=2,columnspan=3)
rcin.configure(font=('Times New Roman',15),width=20)
rc1 = tk.StringVar()
rc1f = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=rc1)
rc1f.grid(column=12, row=2,columnspan=3)

makein = tk.Label(win6, text="Brand (Make) : ", anchor="w", justify=LEFT) 		
makein.grid(column=9, row=3,columnspan=3)
makein.configure(font=('Times New Roman',15),width=20)
make1 = tk.StringVar()
makef = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=make1)
makef.grid(column=12, row=3,columnspan=3)

modelin = tk.Label(win6, text="Vehicle Type (Model) : ", anchor="w", justify=LEFT) 		
modelin.grid(column=9, row=4,columnspan=3)
modelin.configure(font=('Times New Roman',15),width=20)
model1 = tk.StringVar() 
modelf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=model1) 
modelf.grid(column=12, row=4,columnspan=3)

yrin= tk.Label(win6, text="Manufacturing Year : ", anchor="w", justify=LEFT) 		
yrin.grid(column=9, row=5,columnspan=3)
yrin.configure(font=('Times New Roman',15),width=20)
yr1 = tk.IntVar() 
yrf= tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=yr1) 
yrf.grid(column=12, row=5,columnspan=3)

runin= tk.Label(win6, text="Kilometer Reading : ", anchor="w", justify=LEFT) 		
runin.grid(column=9, row=6,columnspan=3)
runin.configure(font=('Times New Roman',15),width=20)
run1 = tk.IntVar() 
runf= tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=run1) 
runf.grid(column=12, row=6,columnspan=3) 

colorin = tk.Label(win6, text="Vehicle Colour : ", anchor="w", justify=LEFT) 		
colorin.grid(column=9, row=7,columnspan=3)
colorin.configure(font=('Times New Roman',15),width=20)
color1 = tk.StringVar() 
colorf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=color1) 
colorf.grid(column=12, row=7,columnspan=3)
 
fuelin = tk.Label(win6, text="Fuel Type : ", anchor="w", justify=LEFT) 		
fuelin.grid(column=9, row=8,columnspan=3)
fuelin.configure(font=('Times New Roman',15),width=20)
fuel1 = tk.StringVar() 
fuelf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=fuel1) 
fuelf.grid(column=12, row=8,columnspan=3)

sellin = tk.Label(win6, text="Selling Price : ", anchor="w", justify=LEFT) 		
sellin.grid(column=9, row=9,columnspan=3)
sellin.configure(font=('Times New Roman',15),width=20)
sell1 = tk.IntVar() 
sellf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=sell1) 
sellf.grid(column=12, row=9,columnspan=3)

costin = tk.Label(win6, text="Owner's Price : ", anchor="w", justify=LEFT) 		
costin.grid(column=9, row=10,columnspan=3)
costin.configure(font=('Times New Roman',15),width=20)
cost1 = tk.IntVar() 
costf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=cost1) 
costf.grid(column=12, row=10,columnspan=3)

ownerin = tk.Label(win6, text="Owner's Name : ", anchor="w", justify=LEFT) 		
ownerin.grid(column=9, row=11,columnspan=3)
ownerin.configure(font=('Times New Roman',15),width=20)
owner1 = tk.StringVar() 
ownerf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=owner1) 
ownerf.grid(column=12, row=11,columnspan=3)

contactin = tk.Label(win6, text="Owner's Mobile : ", anchor="w", justify=LEFT) 		
contactin.grid(column=9, row=12,columnspan=3)
contactin.configure(font=('Times New Roman',15),width=20)
contact1 = tk.StringVar() 
contactf = tk.Entry(win6,font=('Times New Roman',15), width=20, textvariable=contact1) 
contactf.grid(column=12, row=12,columnspan=3)

insert=tk.Button(win6,font=('Times New Roman',15), text="Insert Details" ,command=insert) 
insert.grid(column=11, row=13,columnspan=1)

back=tk.Button(win6,font=('Times New Roman',15), text="Back to Previous Menu",command=back)
back.grid(column=12, row=13,columnspan=1)


