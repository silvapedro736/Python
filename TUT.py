#THE TEST!





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





print (av1 - av2) / av1

print (av1 - av3) / av1

print (av3 - av2) / av3

y = (av1 - av2)/av1

x = (10 / 3) + (10 / 3) * y

print x

y2 = (av3 - av2) / av3

x2 = (10 / 3) + (10 / 3) * y2

print x2

print 10 - x - x2
                






#x = av[0]
#x2 = av[1]
#x3 = av[2]
#averf = 
#aver = (av1 + av2 + av3) / (x + x2+ x3)

#while aver > averf:
#
#    av1 = av1 * x
#    av2 = av2 * x2
##
#    aver = (av1 + av2 + av3) / (x + x2+ x3)
#
#    if aver > averf:
#        averf = aver

    

    
    

    

#print averf
#print x
#print x2
#print x3
