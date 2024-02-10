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



def updatecatering():

    
    update_window=Toplevel()
    update_window.grab_set()
    update_window.resizable(0,0)


    companylabel=Label(update_window,text='Agency Name',font=('times new roman',20,'bold'))
    companylabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    companyEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    companyEntry.grid(row=1,column=1,padx=10,pady=15)
    
    namelabel=Label(update_window,text='Manager Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=2,column=1,padx=10,pady=15)
    
     
    addresslabel=Label(update_window,text='Address',font=('times new roman',20,'bold'))
    addresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    addressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)

    contactlabel=Label(update_window,text='Contact',font=('times new roman',20,'bold'))
    contactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    contactEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    contactEntry.grid(row=3,column=1,padx=10,pady=15)
    

    submitbutton=ttk.Button(update_window,text='Update')
    submitbutton.grid(row=7,columnspan=2) 



    selected_item = cateringTable.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select an item to update")
        return
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Event Management System")
        cursor = con.cursor()
        cursor.execute("UPDATE catering SET  catering_manager = %s catering_address = %s catering_contact =%s Where catering_name = %s", ())
        con.commit()

        messagebox.showinfo("Status", "Successfully updated!")
        con.close()

   

def showcatering():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    query = 'SELECT * FROM catering'
    cursor.execute(query)
    fetched_data = cursor.fetchall()

        # Clear existing rows from the agentTable
    cateringTable.delete(*cateringTable.get_children())

        # Insert fetched data into agentTable
    for data in fetched_data:
            cateringTable.insert('', END, values=data)
    

    



def deletecatering():
    selected_item = cateringTable.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select an item to delete")
        return
    
    content = cateringTable.item(selected_item)
    content_id = content['values'][0]
    
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
        cursor = con.cursor()
        query = 'DELETE FROM catering WHERE id=%s'
        cursor.execute(query, (content_id,))
        con.commit()
        messagebox.showinfo('Deleted', f'Record with ID {content_id} has been deleted successfully')
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error deleting record: {e}")
    finally:
        cursor.close()
        con.close()

def addcatering():
    def add_data():
        if nameEntry.get()=='' or nameEntry.get()=='' or contactEntry.get()=='' or addressEntry.get()=='':
            messagebox.showerror('Error','All Fields Must Be Filled',parent=add_window)
            return
        

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO catering(catering_agency, catering_manager, catering_address, catering_contact) VALUES (%s, %s, %s, %s)", (companyEntry.get(), nameEntry.get(), addressEntry.get(), contactEntry.get()))
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
root.title('Add Catering')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Catering Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=750, y=60)

leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=155,width=360,height=525)

addnewbutton=Button(leftFrame,text='Add New',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=addcatering)
addnewbutton.grid(row=1,column=0,pady=20,padx=100)

updatbutton=Button(leftFrame,text='Update',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=updatecatering)
updatbutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete ',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=deletecatering)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show ',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=showcatering)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

cateringTable=ttk.Treeview(rightFrame,columns=('Id','Agency Name','Manager','Address','Contact'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=cateringTable.xview)
ScrollbarY.config(command=cateringTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
cateringTable.pack(fill=BOTH,expand=1)

cateringTable.heading('Id',text='Id')
cateringTable.heading('Agency Name',text='Agency Name')
cateringTable.heading('Manager',text='Manager')
cateringTable.heading('Address',text='Address')
cateringTable.heading('Contact',text='Contact')



cateringTable.config(show='headings')

root.mainloop()