#Fix for arrays!

a = []
b = []

for i in range(10):
    a.append(0)

for i in range(len(a)):
    b.append(a[i])

b[0] = "t"
b[4] = 5



print a
print b
