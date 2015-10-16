#Graphics Pi

import random
from graphics import *

a = []
n = 0.0
p = 10

Circle(1, 1)

def graph(a, b):
    Rectangle(a, b)

for i in range(p):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    x = int(x)
    y = int(y)

    x = Point(x, x)
    y = Point(y, y)

    a.append([x, y])

    #if (a[i][0]*a[i][0]) + (a[i][1]*a[i][1]) <= 1:
    #if x*x + y*y <=1:
        #print a[i],
        #print "is in the circle."
        #n = n + 1
    #else:
        #print a[i],
        #print "is not in the circle."
    graph(a[i][0], a[i][1])
