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

aver = ((av1 + av2 + av3) / 3) * 100

w1 = 1

w2 = 1

w3 = 1

averf = 0


while True:
    aver = ((av1 + av2 + av3) / 3) * 100

    if aver > averf:
        aver = averf

    if aver == averf:
        w1 = w1 + 1
        if aver < averf:
            w1 = w1 - 2

    print aver
    print averf
        
    
