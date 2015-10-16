print "Enter Number:"
x = raw_input()
n = float(x)
if not n == 2:
    if n % 2 == 1:
        y = n / 3.0
        while y > 0:
            y = y - 1
            print y
        if not y == 0:
            print n,
            print " is not a prime number."
        if y == 0:
            print n,
            print " is a prime number."
    if n % 2 == 0:
        print n,
        print " is not a prime number."
if n == 1:
    print n,
    print " is not a prime number."

    
    

