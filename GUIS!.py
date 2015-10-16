from Tkinter import *
import tkMessageBox
import Tkinter

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Welcome " + E1.get())


root = Tk()
frame = Frame(root)
frame.pack()


L1 = Label(frame, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(frame, bd =5)

E1.pack(side = LEFT)

L2 = Label(frame, text="Password")
L2.pack( side = LEFT)
E2 = Entry(frame, bd =5)

E2.pack(side  = BOTTOM)

B = Button(frame, text ="Hello", command = helloCallBack)
B.place(x = 2, y = -10)

B.pack()

root.mainloop()



