i = 0
con = True
a = []

base = 2
num = 5013
num2 = num

while con:
    x = num%(base**(i+1))
    num = num - x
    x = x/(base**i)
    a.append(x)
    i = i + 1
    if num == 0:
        con = False


print str(num2) + " becomes ",
for item in a[::-1]:
    print item,
