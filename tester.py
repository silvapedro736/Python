#Tester

import random


def gameCallBack(entry):

    #wMain.destroy()

    p = []
    alives = []
    size = 15

    def startUpCallBack():

        live = 1.0/int(entry) * (size**2)

        for i in range(int(live)):
            x = int(random.uniform(0, size))
            y = int(random.uniform(0, size))

            alives.append([x, y])

        return alives

    def firstLoadCallBack():

        startUpCallBack()

        for i in range(size):
            a = []
            for r in range(size):
                a.append(0)
            p.append(a)

            
        for i in range(size):
            for r in range(size):
                for q in range(len(alives)):
                    if alives[q][0] == r:
                        if alives[q][1] == i:
                            p[i][r] = 1
        print p

    firstLoadCallBack()

gameCallBack(10)
