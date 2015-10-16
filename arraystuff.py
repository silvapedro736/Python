# Array Stuff

a = []

for i in range(10):
    a.append(0)

a = a
b = a

b[0] = "t"

print b

a[0] = 0
print a

