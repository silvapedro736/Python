#GRAPHS

from graphics import *
import random

a = []

L = 10

M = 10

for i in range(L):
    a.append(random.uniform(0, M))


win=GraphWin()
win.setCoords(-0.2,0,L,M+0.2)

def main(x, y):
    rec = Rectangle(x, y)
    rec.draw(win)

for i in range(5):
    p1 = Point(i, 0)
    p2 = Point(i+1, a[i])
    main(p1, p2)
    print p1
    print p2
