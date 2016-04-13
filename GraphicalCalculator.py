#Graphical Calculator
from graphics import *
from Tkinter import *

wMain = Tk()

font = "times", 20
lInput = Label(wMain, text = "Equation: ", relief = RAISED, bd = 0, font = font)
lInput.place(x = 110, y = 30)

lInput2 = Label(wMain, text = "y = ", relief = RAISED, bd = 0, font = font)
lInput2.place(x = 60, y = 60)

eEquation = Entry(wMain, bd = 3)
eEquation.place(x = 100, y = 60)

bEnter = Button(wMain, text = "Enter", command = graphCallBack)
bEnter.place(x = 120, y = 100)

equation = eEquation.get()

wMain.minsize(width = 300, height = 150)
wMain.maxsize(width = 300, height = 150)
wMain.title("Main")
wMain.mainloop()


def graphCallBack():

    

    l = list(eEquation.get())
    y = []

    print l
    print eEquation.get()


wMainCallBack()
