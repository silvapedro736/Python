import time

start = time.time()

array = []

Prime = True

num=2

while len(array)<10000:

    Prime=True

    for x in range(2, num/2):
        if num%x==0:
            Prime = False

        if not Prime:
            break

    if Prime:
        array.append(num)

    num = num + 1

        


print array

end = time.time()

print (end - start)

