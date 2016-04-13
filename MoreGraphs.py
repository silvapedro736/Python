#Graphs\

from graphics import *
import random

a = 0
rec = []
num1 = 10
array = []
MaxFreq = 0
for i in range(num1):
    array.append(0)

for i in range(1000):
    a = 0
    for i in range(num1):
        a = a + (random.uniform(0, 1))
    for i in range(num1):
        if i <= a <= (i + 1):
            array[i] = array[i] + 1
for i in range(len(array)):
    if array[i] > MaxFreq:
        MaxFreq = array[i]
        
graph = GraphWin("BarGraph", 400, 400)
graph.setCoords(-.2, 0, num1, MaxFreq + 10)

for i in range(num1):
    p1 = Point((i), 0)
    p2 = Point(i+1, array[i])
    rec.append([p1, p2])


color = []
for i in range(num1):
    color.append([random.uniform(20, 200), random.uniform(20, 200), random.uniform(20, 200)])

for i in range(num1):
    bar = Rectangle(rec[i][0], rec[i][1])
    col = color_rgb(color[i][0], color[i][1], color[i][2])
    #tex = Text(i + .5, array[i])
    #tex.draw(graph)
    bar.setFill(col)
    bar.draw(graph)

graph.getMouse()
graph.close()

#print color
#print array
#print rec
    
