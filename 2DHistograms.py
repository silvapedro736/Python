#2D Histograms

import random
from graphics import *


#------------------------------------------------------------------------------------------
# Returns an array of lenth X filled up with Zeros

# X = Lenth of the array

def zeros(x):
    a = []
    for i in range(x):
        a. append(0)
        
    return a
#------------------------------------------------------------------------------------------
# Returns the sum of all values in an array

# X = Array that will be "summed"

def sumArray(x):
    s = 0
    for i in range(len(x)):
        s = s + x[i]
    
    return s
#------------------------------------------------------------------------------------------
# Returns a random array of lenth x

# X = Lenth of the random array
# mini = minimum value for random numbers
# maxi = maximum value for random numbers

def randArray(x, mini, maxi):
    a = []
    for i in range(x):
        a.append(random.uniform(mini, maxi))
   
    return a
#------------------------------------------------------------------------------------------
# Returns the average of all values in an array

# X = Array that will "avg"

def avg(x):
    avg = sumArray(x) / len(x)

    return avg
#------------------------------------------------------------------------------------------
# Returns the maximum value of an array

# X = Array that will have the maximum value found

def maximum(x):
    m = -(9*(10**3))
    for i in range(len(x)):
        if x[i] > m:
            m = x[i]
            
    return m
#------------------------------------------------------------------------------------------
# Returns the array that will be used to generate a histogram

# bins = number of bins
# X = Array that will be used to fill up the histogram.

def histogram(bins, x):
    h = zeros(bins)
    for i in range(len(x)):
        if i <= x[i] <= i + 1:
            h[i] = h[i] + 1

    return h
#------------------------------------------------------------------------------------------
# Generates the histogram

# X = Array that will be used to graph

def bargraph(x):
    win = GraphWin("Bar Graph", 400, 400)
    win.setCoords(-.2, 0, len(x), maximum(x)+ 10)
    for i in range(len(x)):
        rec = Rectangle(Point(i, 0), Point(i+1, x[i]))
        rec.draw(win)
    win.getMouse()
    win.close()
#------------------------------------------------------------------------------------------
    
