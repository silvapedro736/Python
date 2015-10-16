#RPG GAME
import random

print "WELCOME TO RPG GAME!"

print ""

print "Enter your username: ",

username = raw_input()

playerhp = 100

playerattack = 5

playerlevel = 0

x = 0

while playerhp > 0:
    playerlevel = playerlevel + 1
    x = x + 1
    monsterattack = 1
                          

    monsterhealth = round(random.uniform(1,(playerlevel * 20)), 2)

    print "Monster " + str(x)
    print "Player Level" + str(playerlevel)

    while True:

        print "Press Enter to Attack"
                      

        at = raw_input()


        playerhp = playerhp - monsterattack
        go = go - playerattack

        print playerhp
        print go

print "YOU DIED!"
    

    

    
                      
