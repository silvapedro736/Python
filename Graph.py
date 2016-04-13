from graphics import *
from Tkinter import *
import tkMessageBox

Rate = Tk()
lUsername = Label(Rate, text="Username:")
lUsername.place(x = 9, y = 6)
eUsername = Entry(Rate, bd =5)
eUsername.place(x = 80, y = 1)
lPassword = Label(Rate, text="Password:")
lPassword.place(x = 9, y = 35)
ePassword = Entry(Rate, bd =5)
ePassword.place(x = 80, y = 35)



Rate.minsize(width = 250, height = 127)
Rate.maxsize(width = 250, height = 127)
Rate.title("Rate")
Rate.mainloop()
