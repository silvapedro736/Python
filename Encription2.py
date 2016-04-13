#Encription 2

import random

key = []
key2 = []
numb = []
enc = []
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]


    

print "Enter Text to Encrypt: "
    
string = raw_input()

l = list(string)


for i in range(len(l)):
    for r in range(len(abc)):
        if l[i] == abc[r]:
            numb.append(r)

for i in range(len(numb)):

    y = int(round(random.uniform(1, 99), 0))
    key.append(y)
    x = int(round(random.uniform(1, 99), 0))
    key2.append(x)

    keysave = key



for i in range(len(numb)):

    y = (key[i] + numb[i]) * key2[i]
    
    enc.append(y)

print enc

print "Decript?"

m = raw_input()

print enc

print key2

for i in range(len(numb)):

    print enc[i] / key2[i]

print key

for i in range(len(numb)):

    print (enc[i] / key2[i]) - key[i]

for i in range(len(numb)):
    print abc[((enc[i] / key2[i]) - key[i])],
            


