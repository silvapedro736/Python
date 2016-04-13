#Conways Game of Life

import random
from graphics import *
from Tkinter import *
import tkMessageBox

#------------------------------------------------------------------------------------------
# Generates Grid

wGetInfo = Tk()

lOptions = Label(wGetInfo, text = "Window Size:")
lOptions.place(x = 9, y = 6)

var = IntVar()

R1 = Radiobutton(wGetInfo, text="100 x 100", variable = var, value = 7)
R1.place(x = 100, y =6)

R2 = Radiobutton(wGetInfo, text="400 x 400", variable = var, value = 3)
R2.place(x = 100, y = 40)

R3 = Radiobutton(wGetInfo, text="1000 x 1000", variable = var, value = 5)
R3.place(x = 100, y = 74)

#------------------------------------------------------------------------------------------
# Game Generator

def gameCallBack():

    wGetInfo.destroy()

    sizes = 100
    a = []
    b = []
    c = []
    p = []

    for i in range(sizes):
        a.append(0)
        for r in range(sizes):
            b.append(a)
            
    for i in range(sizes):
        r = random.uniform (0,1)
        for r in range(sizes):
            if r >= 0.5:
                b[i][r] = b[i][r]+1

    #for i in range(sizes):
        #print b[i]

    graph = GraphWin("Conway's Game of Life", 500, 500)
    graph.setCoords(-.2, 0, sizes, sizes)

    for i in range(len(a)):

        g = i
        d = 0

        while g > sizes:
            g = g - sizes
            d = d + 1
        
        p1 = Point((i), (d))
        p2 = Point((i + 1), (d + 1))

        p.append([p1, p2])
    print b

        
        

bSelect = Button(wGetInfo, text = "Confirm", command = gameCallBack)
bSelect.place(x = 70, y = 105)

wGetInfo.minsize(width = 210, height = 150)
wGetInfo.maxsize(width = 210, height = 150)
wGetInfo.title("Conway's Game of Life")
wGetInfo.mainloop()

graph = GraphWin("BarGraph", 1000, 1000)
graph.setCoords(-.2, 0, num1, MaxFreq + 10)
