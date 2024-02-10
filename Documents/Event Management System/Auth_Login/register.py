from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector 
import re

def connect_database():
    username = usernameEntry.get()
    email = EmailEntry.get()
    password = passwordEntry.get()
    confirm_password = ConfirmpasswordEntry.get()

    if email == '' or username == '' or password == '' or confirm_password == '':
        messagebox.showerror('Error', 'All fields must be filled')
    elif password != confirm_password:
        messagebox.showerror('Error', 'Password Mismatched!')
    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
            cursor = con.cursor()
            cursor.execute("INSERT INTO Register (Username, Password, Email) VALUES (%s,%s,%s)", (username, password, email))
            con.commit()
            con.close()
            messagebox.showinfo("Status", "Successfully registered")
        except Exception as e:
            messagebox.showerror("Error", f"Error in connecting to database: {str(e)}")

# functionality
def login_page():
    Register.destroy()
    import login

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def Email_enter(event):
    if EmailEntry.get() == 'Email':
        EmailEntry.delete(0, END)

def ConfirmPass_enter(event):
    if ConfirmpasswordEntry.get() == 'Confirm Password':
        ConfirmpasswordEntry.delete(0, END)

# GUI
Register = Tk()
Register.geometry('990x660+50+50')
Register.resizable(0, 0)
Register.title('Register Page')

bgImage = ImageTk.PhotoImage(file='Images/Register.png')
bgLabel = Label(Register, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(Register, text='Create an Account', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading.place(x=400, y=80)

heading1 = Label(Register, text='Already have an account?', font=('Microsoft Yahei UI Light', 18), bg='#DFA7E4',
                 fg='#A5256B')
heading1.place(x=390, y=120)

LoginButton = Button(Register, text='Log In', font=('Open Sans', 9, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0,command=login_page)
LoginButton.place(x=600, y=125)

Username = Label(Register, text='Username:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Username.place(x=330, y=210)

usernameEntry = Entry(Register, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='white')  # Set white border color
usernameEntry.place(x=400, y=210)


Email = Label(Register, text='Email:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Email.place(x=355, y=260)
EmailEntry = Entry(Register , width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                      highlightbackground='white')  # Set white border color
EmailEntry.place(x=400, y=260)


Password = Label(Register, text='Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Password.place(x=330, y=310)

passwordEntry = Entry(Register, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                       highlightbackground='white')  # Set white border color
passwordEntry.place(x=400, y=310)


ConfirmPass = Label(Register, text='Confirm Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
ConfirmPass.place(x=285, y=360)

ConfirmpasswordEntry = Entry(Register, width=38, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#DFA7E4',
                       highlightbackground='white')  # Set white border color
ConfirmpasswordEntry.place(x=400, y=360)
ConfirmpasswordEntry.config(show='*')



CreateButton = Button(Register, text='Creat Account', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B', activebackground='#DFA7E4',highlightbackground='#DFA7E4',cursor='hand2',bd=0,width=13,height=1,command=connect_database)
CreateButton.place(x=450, y=450)

Register.mainloop()
