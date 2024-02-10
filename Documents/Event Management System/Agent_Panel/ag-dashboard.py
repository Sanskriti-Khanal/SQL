from tkinter import*
from PIL import ImageTk



#functionality
def exit_button():
    agent.destroy()
   


#GUI
agent = Tk()
agent.geometry('990x660+50+50')
agent.resizable(0,0)
agent.title('Login Page')


bgImage=ImageTk.PhotoImage(file='Images/dahboard.png')
bgLabel=Label(agent,image=bgImage)
bgLabel.place(x=0,y=0)


heading=Label(agent,text='Welcome To Agent Panel!',font=('Microsoft Yahei UI Light',30,'bold'),bg='white',fg='#A5256B')
heading.place(x=280,y=20)

heading1=Label(agent,text='Dasboard',font=('Microsoft Yahei UI Light',22),bg='white',fg='#A5256B')
heading1.place(x=280,y=90)




LoginButton = Button(agent, text='Past Booking', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1)
LoginButton.place(x=310, y=175)


LoginButton = Button(agent, text='Create New Booking', font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0, width=13, height=1)
LoginButton.place(x=600, y=175)


exitbutton=Button(agent,text='Exit',font=('Open Sans', 16, 'bold'), fg='#A5256B', bg='#DFA7E4', activebackground='#DFA7E4', highlightbackground='#DFA7E4', cursor='hand2', bd=0,width=13,command=exit_button)
exitbutton.place(x=50,y=600)

























agent.mainloop()