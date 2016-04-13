#Graphical Calculator
from Tkinter import *
import tkMessageBox


wMain = Tk()

font = "times", 20
lInput = Label(wMain, text = "Equation: ", relief = RAISED, bd = 0, font = font)
lInput.place(x = 110, y = 30)

lInput2 = Label(wMain, text = "y = ", relief = RAISED, bd = 0, font = font)
lInput2.place(x = 60, y = 60)

eEquation = Entry(wMain, bd = 3)
eEquation.place(x = 100, y = 60)



def signupCallBack():
    l = list(eEquation.get())
    y = []

    for i in range(10):
        p = l
        for r in range(len(p)):
            if p[r] == "x":
                p[r] = 3
                p[r] = i
        print p
        



                    
bEnter = Button(wMain, text = "Enter", command = signupCallBack)
bEnter.place(x = 120, y = 100)


wMain.minsize(width = 300, height = 150)
wMain.maxsize(width = 300, height = 150)
wMain.title("Main")
wMain.mainloop()

