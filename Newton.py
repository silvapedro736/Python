#Newton's Method
import time

while True:
    time.sleep(1)
    print "--------------"
    print "---Newton's---"
    print "----Method----"
    print "--------------"

    time.sleep(.7)

    print "Equation: a(x*x) + bx + c = f(x)"
    print "Input value for a:",
    a = raw_input()
    print "Input value for b:",
    b = raw_input()
    print "Input value for c:",
    c = raw_input()

    af = float(a)
    bf = float(b)
    cf = float(c)

    print "Equation: " + a + "(x*x) + " + b + "x + " + c

    x = 1

    y = 1000

    tr = True

    t = []

    g = (bf - (4 * af * cf))

    if g < 0:
        print "No x intercept"

    if g > 0:

        g = (bf - (4 * af * cf))**(.5)

        if not g < 0:

            while tr:
        
                y = (af * (x * x)) + (bf * x) + cf
    
                if y == 0:
                    break

                if not y == 0.00:
    
                    if y < 0.00:
                        x = x + 0.01

                    if y > 0.00:
                        x = x - 0.01



        

            t.append(x)

        

        

            if len(t) == 3:
                if t[0] == t[2]:
                    break
                    tr = False
                
                if  not t[0] == t[2]:
                    t = []



        
        




        print "y is 0 when x is: " + str(x)

print "It is Neel's fault!"


    
