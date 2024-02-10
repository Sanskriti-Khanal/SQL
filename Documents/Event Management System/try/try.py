from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def create():
    id = user_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if id == "" or name == "" or phone == "":
        MessageBox.showinfo("ALERT", "Insert values!!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkinter_db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO users (id, name, phone) VALUES (%s, %s, %s)", (id, name, phone))
        con.commit()

        MessageBox.showinfo("Status", "Successfully inserted!")
        con.close()

def update():
    id = user_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        MessageBox.showinfo("ALERT", "Enter value to update!!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkinter_db")
        cursor = con.cursor()
        cursor.execute("UPDATE users SET name = %s, phone = %s WHERE id = %s", (name, phone, id))
        con.commit()

        MessageBox.showinfo("Status", "Successfully updated!")
        con.close()

def delete():
    if user_entry.get() == "":
        MessageBox.showinfo("ALERT", "Enter ID to delete!!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkinter_db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_entry.get(),))
        con.commit()

        user_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

        MessageBox.showinfo("Status", "Successfully deleted!")
        con.close()

def select():
    if user_entry.get() == "":
        MessageBox.showinfo("ALERT", "Enter ID to select!!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="tkinter_db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_entry.get(),))
        rows = cursor.fetchall()

        for row in rows:
            name_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            name_entry.insert(0, row[1])
            phone_entry.insert(0, row[2])

        con.close()

root = Tk()
root.geometry("350x200")
root.title("CRUD")
root.eval('tk::PlaceWindow . Center')

user_id = Label(root, text="ID:")
user_id.place(x=50, y=30)
user_entry = Entry(root, width=32)
user_entry.place(x=150, y=30)

name = Label(root, text="Full name:")
name.place(x=50, y=80)
name_entry = Entry(root, width=32)
name_entry.place(x=150, y=80)

phone = Label(root, text="Phone")
phone.place(x=50, y=130)
phone_entry = Entry(root, width=32)
phone_entry.place(x=150, y=130)

Create_Button = Button(root, text="Create", command=create, bg='yellow')
Create_Button.place(x=150, y=160)

Update_Button = Button(root, text="Update", command=update, bg='purple')
Update_Button.place(x=200, y=160)

Delete_Button = Button(root, text="Delete", command=delete, bg='red')
Delete_Button.place(x=253, y=160)

Select_Button = Button(root, text="Select", command=select, bg='grey')
Select_Button.place(x=303, y=160)

root.mainloop()