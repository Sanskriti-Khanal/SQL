from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import time
import ttkthemes
from tkinter import ttk, BOTH
import mysql.connector 
import re


#functionality
def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'Date:{date}\nTime:{currenttime}')
    datetimelabel.after(1000,clock)

def adddecor():
    def add_data():
        if nameEntry.get()=='' or nameEntry.get()=='' or contactEntry.get()=='' or addressEntry.get()=='':
            messagebox.showerror('Error','All Fields Must Be Filled',parent=add_window)
            return
        

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO decor(agency_name, agency_manager, decor_address, decor_contact) VALUES (%s, %s, %s, %s)", (nameEntry.get(), nameEntry.get(), addressEntry.get(), contactEntry.get()))

            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")


            




    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    # idlabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    # idlabel.grid(row=0,column=0,padx=30,pady=15,sticky= W)                                             
    # idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # idEntry.grid(row=0,column=1,padx=10,pady=15)

    companylabel=Label(add_window,text='Agency Name',font=('times new roman',20,'bold'))
    companylabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    companyEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    companyEntry.grid(row=1,column=1,padx=10,pady=15)
    
    namelabel=Label(add_window,text='Manager Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=2,column=1,padx=10,pady=15)
    
     
    addresslabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)

    contactlabel=Label(add_window,text='Contact',font=('times new roman',20,'bold'))
    contactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    contactEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    contactEntry.grid(row=3,column=1,padx=10,pady=15)
    

    submitbutton=ttk.Button(add_window,text='Add',command=add_data)
    submitbutton.grid(row=7,columnspan=2) 
    




   



#GUI
root=ttkthemes.ThemedTk('Radiance')
root.get_themes()

root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Decoraction')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Decoraction Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=750, y=60)



leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=155,width=360,height=525)

addnewbutton=Button(leftFrame,text='Add New',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=adddecor)
addnewbutton.grid(row=1,column=0,pady=20,padx=100)

updatbutton=Button(leftFrame,text='Update',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
updatbutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete ',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

agentTable=ttk.Treeview(rightFrame,columns=('Id','Agency Name','Manager','Address','Contact'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=agentTable.xview)
ScrollbarY.config(command=agentTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
agentTable.pack(fill=BOTH,expand=1)

agentTable.heading('Id',text='Id')
agentTable.heading('Agency Name',text='Agency Name')
agentTable.heading('Manager',text='Manager')
agentTable.heading('Address',text='Address')
agentTable.heading('Contact',text='Contact')



agentTable.config(show='headings')

root.mainloop()