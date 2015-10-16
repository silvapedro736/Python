#Encription

import random

key = []
key2 = []
numb = []
enc = []

while len(key) < 10:
    y = int(round(random.uniform(1, 99), 0))
    key.append(y)
    x = int(round(random.uniform(1, 99), 0))
    key2.append(x)

    keysave = key

for x in range(10):
    

    print "Enter number " + str(x + 1) + " to encrypt: "
    
    num = raw_input()

    num = int(num)
    
    numb.append(num)

for i in range(10):

    y = (key[i] + numb[i]) * key2[i]
    
    enc.append(y)

print enc

print "Decript?"

m = raw_input()

print enc

print key2

for i in range(10):

    print enc[i] / key2[i]

print key

for i in range(10):

    print (enc[i] / key2[i]) - key[i]


