import random
from graphics import *
from Tkinter import *
import tkMessageBox


wMain = Tk()

font = "times", 25, "bold"
lTitle = Label(wMain, text = "Conway's Game of Life", font = font)
lTitle.place(x = 120, y = 30)

font2 = "times", 20
lOption = Label(wMain, text = "Number of Starting Cells", font = font2)
lOption.place(x = 145, y = 80)

font3 = "times", 15
lOption2 = Label(wMain, text = "1/", font = font3)
lOption2.place(x = 155, y = 110)

eEntry = Entry(wMain, bd = 2)
eEntry.place(x = 175, y = 110)

def gameCallBack():

    p = []
    pf = []
    size = 30
    green = color_rgb(82, 245, 103)
    red = color_rgb(247, 34, 49)
    deads = []
    dead = 1.0/int(eEntry.get()) * (size**2)

    for i in range(int(dead)):
        x = int(random.uniform(0, size))
        y = int(random.uniform(0, size))
                 
        deads.append([x, y])
    #print deads
    #print len(deads)
    
    wMain.destroy()

    game = GraphWin("The Game Of Life", 400, 400)
    game.setCoords(-.2, 0, size, size + .2)

    def rand():
        for i in range(size):
            for r in range(size):
                p.append([Point(r, i), Point(r+1, i+1), 0])
        for i in range(size):
            for r in range(size):
                for q in range(len(deads)):
                    if deads[q][0] == r:
                        if deads[q][1] == i:
                            p[(size*i)+r][2] = 1
    
    
        return pf
        print pf

    p = rand()

    while True:
    
        for i in range(len(p)):
            point = Rectangle(p[i][0], p[i][1])
            if p[i][2] == 0:
                point.setFill(red)
            if p[i][2] == 1:
                point.setFill(green)

            point.draw(game)


        

        

    



        
bBegin = Button(wMain, text = "Begin", command = gameCallBack)
bBegin.place(x = 210, y = 150)


wMain.minsize(width = 500, height = 210)
wMain.maxsize(width = 500, height = 210)
wMain.title("Conway's Game of Life")
wMain.mainloop()
