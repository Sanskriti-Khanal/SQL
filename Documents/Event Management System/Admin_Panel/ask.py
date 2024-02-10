
from tkinter import *
from PIL import ImageTk

#Functinality

def admin():
    ask.destroy()
    from Auth_Login import logina

def agent():
    ask.destroy()
    from Auth_Login import login



# GUI
ask = Tk()
ask.geometry('990x660+50+50')
ask.resizable(0, 0)
ask.title('Login Page')

bgImage = ImageTk.PhotoImage(file='Images/ask.png')
bgLabel = Label(ask, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(ask, text='WELCOME!', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='#DFA7E4', fg='#A5256B')
heading.place(x=700, y=120)

heading1 = Label(ask, text='Streamline Your Events with Evento Your Ultimate', font=('Microsoft Yahei UI Light', 16), bg='#DFA7E4', fg='#A5256B')
heading1.place(x=620, y=170)

heading2 = Label(ask, text=' Event Management Solution', font=('Microsoft Yahei UI Light', 16), bg='#DFA7E4', fg='#A5256B')
heading2.place(x=680, y=200)



AdminButton = Button(ask, text='Admin', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=admin)
AdminButton.place(x=620, y=350)

AgentButton = Button(ask, text='Agent', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#A5256B',
                     activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=agent)
AgentButton.place(x=800, y=350)

ask.mainloop()
