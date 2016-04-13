#2D Histogram

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



a = zeros(10)

for i in range(10):
    avg(randArray(x, 0, 10))
    for i in range(len(x)):
        if i <= x[i] <= i + 1:
            h[i] = h[i] + 1
