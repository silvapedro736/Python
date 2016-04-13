import random

a = 0

b = 10

c = 10


def rand(Min, Max, n):
    arr = []
    for i in range(n):
        arr.append(random.uniform(Min, Max))
    return arr
    

def mean():
    rand(a, b, c)
    m  = 0
    for i in range(len(arr)):
        m = m + arr[i]
    m = m / len(array)
    return m

#print rand(a, b, c)
print mean(arr)
#print arr



