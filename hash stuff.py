#Hash Stuff

import hashlib

def hasher():
    num = -1
    p = 0
    l = []
    test = True
    while test:
        num = num + 1
        p = str(hashlib.sha256("message name" + str(num)))
        l = list(p)
        print num
        if l[0] == "0" and l[1] == "0":
            test = False


    print p
    print n

hasher()
        
