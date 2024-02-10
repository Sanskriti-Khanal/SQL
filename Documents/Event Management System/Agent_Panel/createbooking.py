from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk

#GUI
root = Tk()
root.geometry("1150x680+50+20")  # Corrected geometry dimensions
root.resizable(0, 0)
root.title('Create Booking')

bgImage = ImageTk.PhotoImage(file='Images/Screenshot 2024-02-10 at 12.15.45.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(root, text='Create Booking', font=('arial', 28), bg='#DFA7E4', fg='#A5256B')
heading.place(x=600, y=70)

root.mainloop()
