
while True:
    h = "Welcome to Number to Binary"
    equ = "="
    print h
    print "Enter number to convert:"
    s = raw_input()

    v = int(s) 

    bina = bin(v)[2:]  

    print v,

    print equ,
    print bina
    

