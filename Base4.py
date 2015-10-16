while True:
    a = []
    print ""
    print "Enter base: ",
    b = raw_input()
    print "Enter Number to convert: ",
    num = raw_input()
    b = int(b)
    num = int(num)
    def base(y, k):
        i = 0
        con = True
        while con:
            x = y%(k**(i+1))
            y = y - x
            x = x/(k**i)
            a.append(x)
            i = i + 1
            if y == 0:
                con = False


    base(num, b)
    print str(num) + " becomes ",
    for item in a[::-1]:
        print item,
