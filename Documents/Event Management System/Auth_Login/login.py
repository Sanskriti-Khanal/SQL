
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Event Management System"
)

# def login_agent():
#     username = usernameEntry.get()
#     password = passwordEntry.get()

#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="Event Management System"
#     )
#     cursor = connection.cursor()

#     cursor.execute('SELECT * FROM Register WHERE Username=%s AND Password=%s', (usernameEntry.get(), passwordEntry.get()))
#     user = cursor.fetchone()

# # functionality
def login_agent():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','All fields must be filled')
        return

    try:
        # Connect to the database
        con = mysql.connector.connect(host='localhost', user='root', password='', database='Event Management System')
        cursor = con.cursor()

        # Execute the select query to check if the provided username and password exist in the database
        cursor.execute("SELECT * FROM Register WHERE username = %s AND password = %s", (usernameEntry.get(), passwordEntry.get()))
        row = cursor.fetchone()

        if row:
            messagebox.showinfo('Success', 'Welcome')
            login.destroy()
            from Agent_Panel import agent
        else:
            messagebox.showerror('Error', 'Please provide correct details')

        # Close the database connection
        con.close()

    except mysql.connector.Error as e:
        messagebox.showerror('Error', f'Error connecting to database:{e} ')



def register_page():
    login.destroy()
    import register

def forget_pass():
    login.destroy()
    import forgetpass



# GUI
login = Tk()
login.geometry('990x660+50+50')
login.resizable(0, 0)
login.title('Login Page')

bgImage = ImageTk.PhotoImage(file='Images/login.png')
bgLabel = Label(login, image=bgImage)
bgLabel.place(x=0, y=0)


heading0 = Label(login, text='WELCOME!', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading0.place(x=700, y=120)

heading = Label(login, text='Sign in to your account, Agent Panel', font=('Microsoft Yahei UI Light', 20, ), bg='#DFA7E4', fg='#A5256B')
heading.place(x=630, y=160)



Username = Label(login, text='Username:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Username.place(x=600, y=250)

usernameEntry = Entry(login, width=40, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
usernameEntry.place(x=670, y=250)


frame1 = Frame(login, width=288, height=2, bg='#A5256B')
frame1.place(x=670, y=270)

Password = Label(login, text='Password:', font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#DFA7E4', fg='#A5256B')
Password.place(x=600, y=300)

passwordEntry = Entry(login, width=40, font=('Microsoft Yahei UI Light', 11), bg='white', bd=0, fg='#A5256B',
                      highlightbackground='white')
passwordEntry.place(x=670, y=300)
passwordEntry.config(show='*')


frame2 = Frame(login, width=288, height=2, bg='#A5256B')
frame2.place(x=670, y=320)

forgetButton = Button(login, text='Forgot Password?', bd=0, bg='#DFA7EA', activebackground='#DFA7E4', cursor='hand2',
                      highlightbackground='#DFA7E4', font=('Microsoft Yahei UI Light', 9), fg='#A5256B',command=forget_pass)
forgetButton.place(x=825, y=350)

LoginButton = Button(login, text='Login', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=login_agent)
LoginButton.place(x=715, y=450)

RegisterLabel = Label(login, text="Don't have an account?", font=('Open Sans', 9,), fg='#A5256B', bg='#DFA7EA')
RegisterLabel.place(x=650, y=550)

CreateButton = Button(login, text='Create', font=('Open Sans', 9, 'bold'), fg='#A5256B', bg='#A5256B',
                   activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,command=register_page)
CreateButton.place(x=760, y=550)

login.mainloop()
