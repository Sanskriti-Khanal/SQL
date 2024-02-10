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

def update_agent():

    update_window=Toplevel()
    update_window.grab_set()
    update_window.resizable(0,0)
    
    # idlabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    # idlabel.grid(row=0,column=0,padx=30,pady=15,sticky= W)                                             
    # idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    # idEntry.grid(row=0,column=1,padx=10,pady=15)

    namelabel=Label(update_window,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    companylabel=Label(update_window,text='Company Name',font=('times new roman',20,'bold'))
    companylabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    companyEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    companyEntry.grid(row=2,column=1,padx=10,pady=15)
    
    contactlabel=Label(update_window,text='Contact',font=('times new roman',20,'bold'))
    contactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    contactEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    contactEntry.grid(row=3,column=1,padx=10,pady=15)
    
    emaillabel=Label(update_window,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=4,column=0,padx=30,pady=15,sticky= W)
    emailEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=4,column=1,padx=10,pady=15)
    
    addresslabel=Label(update_window,text='Address',font=('times new roman',20,'bold'))
    addresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    addressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)
    
    c_registeredlabel=Label(update_window,text='Company Registered',font=('times new roman',20,'bold'))
    c_registeredlabel.grid(row=6,column=0,padx=30,pady=15,sticky= W)
    c_registeredEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    c_registeredEntry.grid(row=6,column=1,padx=10,pady=15)

    updatebutton=ttk.Button(update_window,text='Update Agent')
    updatebutton.grid(row=7,columnspan=2)

    selected_item = agentTable.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select an item to update")
        return
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Event Management System")
        cursor = con.cursor()
        cursor.execute("UPDATE agent SET  company_name = %s contact = %s email = %s address = %s company_registered=%s Where name= %s", ())
        con.commit()

        messagebox.showinfo("Status", "Successfully updated!")
        con.close()

   

def show_agent():
    con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
    cursor = con.cursor()
    query = 'SELECT * FROM agent'
    cursor.execute(query)
    fetched_data = cursor.fetchall()

        # Clear existing rows from the agentTable
    agentTable.delete(*agentTable.get_children())

        # Insert fetched data into agentTable
    for data in fetched_data:
            agentTable.insert('', END, values=data)
    

    



def delete_agent():
    selected_item = agentTable.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select an item to delete")
        return
    
    content = agentTable.item(selected_item)
    content_id = content['values'][0]
    
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
        cursor = con.cursor()
        query = 'DELETE FROM agent WHERE id=%s'
        cursor.execute(query, (content_id,))
        con.commit()
        messagebox.showinfo('Deleted', f'Record with ID {content_id} has been deleted successfully')
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error deleting record: {e}")
    finally:
        cursor.close()
        con.close()



# def delete_button():
#     if nameEntry.get() == "":
#         messagebox.showinfo("ALERT", "Enter Name to delete!!")
#     else:
#         con = mysql.connect(host="localhost", user="root", password="", database="Event Management System")
#         cursor = con.cursor()
#         cursor.execute("DELETE FROM users WHERE id = %s", (nameEntry.get(),))
#         con.commit()

#         user_entry.delete(0, 'end')
#         name_entry.delete(0, 'end')
#         phone_entry.delete(0, 'end')

#         messagebox.showinfo("Status", "Successfully deleted!")
#         con.close()


def addagent():
    def add_data():
        if nameEntry.get()=='' or companyEntry.get()=='' or contactEntry.get()=='' or emailEntry.get()==''or addressEntry.get()=='' or c_registeredEntry.get()=='':
            messagebox.showerror('Error','All Fields Must Be Filled',parent=add_window)
            return
        

        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO agent (name, company_name,contact,email,address,company_registered) VALUES (%s,%s,%s,%s,%s,%s)", ( nameEntry.get(), companyEntry.get(), contactEntry.get(), emailEntry.get(), addressEntry.get(), c_registeredEntry.get()))
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

    namelabel=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    namelabel.grid(row=1,column=0,padx=30,pady=15,sticky= W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)
    
    companylabel=Label(add_window,text='Company Name',font=('times new roman',20,'bold'))
    companylabel.grid(row=2,column=0,padx=30,pady=15,sticky= W)
    companyEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    companyEntry.grid(row=2,column=1,padx=10,pady=15)
    
    contactlabel=Label(add_window,text='Contact',font=('times new roman',20,'bold'))
    contactlabel.grid(row=3,column=0,padx=30,pady=15,sticky= W)
    contactEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    contactEntry.grid(row=3,column=1,padx=10,pady=15)
    
    emaillabel=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emaillabel.grid(row=4,column=0,padx=30,pady=15,sticky= W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=4,column=1,padx=10,pady=15)
    
    addresslabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addresslabel.grid(row=5,column=0,padx=30,pady=15,sticky= W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=5,column=1,padx=10,pady=15)
    
    c_registeredlabel=Label(add_window,text='Company Registered',font=('times new roman',20,'bold'))
    c_registeredlabel.grid(row=6,column=0,padx=30,pady=15,sticky= W)
    c_registeredEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    c_registeredEntry.grid(row=6,column=1,padx=10,pady=15)

    submitbutton=ttk.Button(add_window,text='Add Agent',command= add_data)
    submitbutton.grid(row=7,columnspan=2) 
    




   



#GUI
root=ttkthemes.ThemedTk('Radiance')
root.get_themes()

root.geometry('1174x680+50+20')
root.resizable(0,0)
root.title('Add Agent')

bgImage = ImageTk.PhotoImage(file='Images/add.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimelabel=Label(root,font=('times new Roman',18,'bold'),bg='#DFA7E4', fg='#A5256B')
datetimelabel.place(x=10,y=5)
clock()

heading2 = Label(root, text='Agent Details', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=750, y=60)


leftFrame=Frame(root,bg='#DFA7E4')
leftFrame.place(x=5,y=155,width=360,height=525)

addagentbutton=Button(leftFrame,text='Add Agent',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=addagent)
addagentbutton.grid(row=1,column=0,pady=20,padx=100)

updateagentbutton=Button(leftFrame,text='Update Agent',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=update_agent)
updateagentbutton.grid(row=2,column=0,pady=20,padx=100)

deletebutton=Button(leftFrame,text='Delete Agent',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=delete_agent)
deletebutton.grid(row=3,column=0,pady=20,padx=100)

showbutton=Button(leftFrame,text='Show Agent',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=show_agent)
showbutton.grid(row=4,column=0,pady=20,padx=100)

exitbutton=Button(leftFrame,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13)
exitbutton.grid(row=5,column=0,pady=20,padx=100)

rightFrame=Frame(root,bg='white')
rightFrame.place(x=365,y=130,width=820,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame)

agentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Company Name','Contact','Email','Address','Company Registered'),
                        xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=agentTable.xview)
ScrollbarY.config(command=agentTable.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
agentTable.pack(fill=BOTH,expand=1)

agentTable.heading('Id',text='Id')
agentTable.heading('Name',text='Name')
agentTable.heading('Company Name',text='Company Name')
agentTable.heading('Contact',text='Contact')
agentTable.heading('Email',text='Email')
agentTable.heading('Address',text='Address')
agentTable.heading('Company Registered',text='Company Registered')


agentTable.config(show='headings')

root.mainloop()