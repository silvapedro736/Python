import random

a = []
n = 0.0
p = 100000000

for i in range(p):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    #a.append([x, y])

    #if (a[i][0]*a[i][0]) + (a[i][1]*a[i][1]) <= 1:
    if x*x + y*y <=1:
        #print a[i],
        #print "is in the circle."
        n = n + 1
    #else:
        #print a[i],
        #print "is not in the circle."

print "Pi is ",
print 4.0*(n/p)
    
    
