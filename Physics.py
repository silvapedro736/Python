while True:
    print "What height is the start(meters): " ,
    y0 = raw_input()

    print "What is the force being applied at the start: ",
    v0 = raw_input()

    a = -9.8
    dt = 0.01
    t = 0
    v = float(v0)
    y = float(y0)
    ymax = 0.0

    while y > -0.0000000001:
        t = t + dt
        v = v + a * dt
        y = y + v * dt

        if y > ymax:
            ymax = y

    print "Time taken: " + str(t) + "s"
    print "Final velocity:" + str(v) + " m/s"
    print "Max Height: " + str(ymax) + " m"


