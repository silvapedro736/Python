a = []
for i in range(10):
    b = []
    for r in range(10):
        b.append((r+i)%2)
    a.append(b)

for i in range(10):
    print a[i]
