from tkinter import*
from PIL import ImageTk


#functionality
def exit_button():
    admin.destroy()

def agent_data():
    admin.destroy()
    import agent

def venue_data():
    admin.destroy()
    import venue


def decor_data():
    admin.destroy()
    import decor


def catering_data():
    admin.destroy()
    import catering


#GUI
admin = Tk()
admin.geometry('990x660+50+50')
admin.resizable(0,0)
admin.title('Admin Dashboard')


bgImage=ImageTk.PhotoImage(file='Images/dahboard.png')
bgLabel=Label(admin,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(admin,text='Welcome To Agent Panel!',font=('Microsoft Yahei UI Light',30,'bold'),bg='white',fg='#A5256B')
heading.place(x=280,y=20)

heading1=Label(admin,text='Dasboard',font=('Microsoft Yahei UI Light',22),bg='white',fg='#A5256B')
heading1.place(x=280,y=90)




AgentButton = Button(admin, text='Agent', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=agent_data)
AgentButton.place(x=300, y=175)


VenueButton = Button(admin, text='Venue', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=venue_data)
VenueButton.place(x=300, y=275)

DecoractionButton = Button(admin, text='Decoration', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=decor_data)
DecoractionButton.place(x=600, y=175)

CateringButton = Button(admin, text='Catering', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1,command=catering_data)
CateringButton.place(x=600, y=275)

exitbutton=Button(admin,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=exit_button)
exitbutton.place(x=50,y=600)

























admin.mainloop()