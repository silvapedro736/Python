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

playergold = 0

def cls(): print "\n" * 40

while playerhp > 0:
    playerlevel = playerlevel + 1
    x = x + 1
    monsterattack = round(random.uniform(1, (playerlevel * 4)), 2)

    if playerlevel > 49:
        monsterattack = round(random.uniform(1, (playerlevel * 8)), 2)
                          

    monsterhealth = round(random.uniform(1,(playerlevel * 35)), 2)


    if playerlevel > 49:
        monsterhealth = round(random.uniform(1,(playerlevel * 70)), 2)

        
    initmhealth = monsterhealth

    print "Monster " + str(x)
    print "Player Level" + str(playerlevel)

    fight = True

    while fight:

        


        playerhp = playerhp - monsterattack
        monsterhealth = monsterhealth - playerattack

        print "Your Health: " + str(playerhp)
        print "Monster Health" + str(monsterhealth)

        playergold = playergold + (initmhealth / 3)

        store = True        

        if playerhp < 0:
            break

        if monsterhealth < 0:
            print "Monster Died"
            fight = False

        print "Press enter to continue"

        at = raw_input()
        

        cls()


    while store:

        if playerhp < 0:
            fight = False
            store = False
            break
            
        

        print "Your Money $" + str(playergold)

        print "Buy Health Pots $50         [1]"
        print "Buy Better Sword(+10) $100  [2]"
        print "Buy THE PENETRATOR(+50)$400 [3]"
        print "Buy SUPER HEALTH POTS $300  [4]"
        print "Exit                        [5]"

        choice = raw_input()

        if choice == "1":
            if playergold < 50:
                print "You do not have enought money!"
            if playergold > 50:
                playerhp = playerhp + 30 + (5 * playerlevel)
                playergold = playergold - 50
                
        if choice == "2":
            if playergold < 100:
                print "You do not have enought money!"
            if playergold > 100:
                playerattack = playerattack + 10
                playergold = playergold - 100
                
        if choice == "3":
            if playergold < 400:
                print "You do not have enought money!"
            if playergold > 400:
                playerattack = playerattack + 50
                playergold = playergold - 400

        if choice == "4":
            if playergold < 300:
                print "You do not have enought money!"
            if playergold > 300:
                playerhp = playerhp + 30 + (10 * playerlevel)
                playergold = playergold - 300        
                
        if choice == "5":
            store = False

print "YOU DIED!"
print username
print "Your level: " + str(playerlevel)
    

    

    
                      
