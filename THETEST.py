#THE TEST!

# 
#
#
#
#
#
#
#
#
#
#
#
#


student1 = [.6, .7, .8]
student2 = [.9, .9, .5]
student3 = [.9, .4, .8]
student4 = [.6, .7, .6]

question1 = [student1[0], student2[0], student3[0], student4[0]]
question2 = [student1[1], student2[1], student3[1], student4[1]]
question3 = [student1[2], student2[2], student3[2], student4[2]]

av1 = (question1[0] + question1[1] + question1[2]) / 3

av2 = (question2[0] + question2[1] + question2[2]) / 3

av3 = (question3[0] + question3[1] + question3[2]) / 3

a = [av1, av2, av3]



if av1 > av2:
    if av1 > av3:
            if av2 > av3:
                    av = [1, 2, 3]
            if av2 < av3:
                    av = [1, 3, 2]
    if av1 < av3:
            if av1 > av2:
                    av = [2, 3, 1]
            if av1 < av2:
                    av = [3, 2, 1]        
if av1 < av2:
    if av2 > av3:
        if av1 > av3:
                av = [2, 1, 3]
        if av1 < av3:
                av = [3, 1, 2]       
    if av2 < av3:
        if av1 > av2:
                av = [2, 3, 1]
        if av1 < av2:
                av = [3, 2, 1]
#print av
avv = []
for x in range(3):
    g = av[x]
    y = a[g - 1]
    avv.append(y)

x = avv[0] / avv[1]
x1 = avv[1] / avv[2]

xx = 1 + (1*x)
xx1 = xx + (xx*x1)

print "Best weight for question 3: " + str(1)
print "Best weight for question 2: " + str(xx)
print "Best weight for question 1: " + str(xx1)

A1 = av1 * xx
A2 = av2 * 1
A3 = av3 * xx1

print "Best Average: " + str(((A1 + A2 + A3)/(1 + xx + xx1)) * 100)
print "Average with normal weight: " + str(((av1 + av2 + av3)/(3)) * 100)




        

         




