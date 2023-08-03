#Game
#Tristan 
#Text based story game with a marine corps theme
import random 
import art
from random import choice, randint
import string

class salty_lcpl(object):
    name = 'salt'
    health = 100
    motivation =  3
    defense = 15
    salty = 10
class moto_cpl(object):
    name = 'moto'
    health = 150
    motivation = 10
    defense = 10
    salty = 3
class boot_pvt(object):
    name = 'boot'
    health = 125
    motivation = 5
    defense = 5
    salty = 5
    
class gunny(object):
    name = 'Gunny'
    health = 20 
    strength = 10
    loot = random.randint(0,2)
class butterbars(object):
    name = 'Butterbars'
    health = 10
    strength = 5
    loot = random.randint(0,2)
class Istsgt(object):
    name = '1stSgt'
    health = 30
    strength = 15
    loot = random.randint(0,2)
class SgtMaj(object):
    name = 'SgtMaj'
    health = 100
    strength = 20

def gameOver(marine, score):
#This function is called when the health of your marine runs out. It then tells you your score and prints your score to a txt file using the gameScore function.
#Then it displays GAME OVER and asks if you would like to play again. 
    if marine.health < 1:
        print('You are all out of health')
        print('Better luck next time')
        print('Your score is...', score)
        
        gameScore(score)
        
        file = open('score.txt', 'r')
        
        for line in file:
            xline = line.split(',')
            print(xline[0], xline[1])
            
        for _ in range (1):
            word = ''.join(choice(string.ascii_lowercase) for _ in range(randint(1,8)))
            art.tprint('GAME OVER', font = 'dancing font')
        answer = input('Would you like to play again?')
        if answer.lower().strip() == 'yes':
            if marine.name == 'salt':
                marine.health = 100
                marine.motivation = 3
                marine.salty = 10

            elif marine.name == 'moto':
                marine.health = 150
                marine.motivation = 10
                marine.salty=3

            elif marine.name == 'boot':
                marine.health = 125
                marine.motivation = 5
                marine.salty = 5
            start()
        elif answer.lower().strip() == 'no':
            exit()            
def winner(marine, score): 
#This function is called when you defeat the SgtMaj. It is similar to the gameOver function, but instead of GAME OVER, it will print You Win!"""
    gameScore(score)
    file = open('score.txt', 'r') 
    for line in file:
        xline = line.split(',')
        print(xline[0], xline[1])    
    for _ in range (1):
        word = ''.join(choice(string.ascii_lowercase) for _ in range(randint(1,8)))
        art.tprint('You Win!', font = 'dancing font')
    answer = input('Would you like to play again?')
    if answer.lower().strip() == 'yes':
        if marine.name == 'salt':
            marine.health = 100
            marine.motivation = 3
            marine.salty = 10

        elif marine.name == 'moto':
            marine.health = 150
            marine.motivation = 10
            marine.salty=3

        elif marine.name == 'boot':
            marine.health = 125
            marine.motivation = 5
            marine.salty = 5
        start()
    elif answer.lower().strip() == 'no':
        exit()    
    
def gameScore(score):
#This function is called when the game ends. It gives the user the option to type their name to be associated with their score.
#It opens a file named score.txt, inputs the name and score, adds a blank line, and then closes the file.
    file = open('score.txt','a')
    name = input('Type your name....')
    file.write(str(name))
    file.write(',')
    file.write(str(score))
    file.write('.')
    file.write('\n')
    file.close()

def aspiration():
#This function is called after you pass your ASVAB. It allows you to select your class that you will be using throughout the game.
#It also displays the stats of the class you select.
        
    print('Welcome to the fleet, what kind of marine do you aspire to be?')
    selection = input('1. Boot Pvt \n2. Moto Cpl \n3. Salty LCpl \n')
    if selection == "1":
        marine = boot_pvt
        print('You have selected Boot Pvt...These are your traits...')
        print('Health - ', marine.health)
        print('Motivation - ', marine.motivation)
        print('Defense - ', marine.defense)
        print('Salty - ', marine.salty)
        return marine

    elif selection == '2':
        marine = moto_cpl
        print('You have selected Moto Cpl...These are your traits...')
        print('Health - ', marine.health)
        print('Motivation - ', marine.motivation)
        print('Defense - ', marine.defense)
        print('Salty - ', marine.salty)
        return marine

    elif selection == '3':
        marine = salty_lcpl
        print('You have selected Salty LCpl...These are your traits...')
        print('Health - ', marine.health)
        print('Motivation - ', marine.motivation)
        print('Defense - ', marine.defense)
        print('Salty - ', marine.salty)
        return marine

    else:
        print('Please press 1, 2, or 3')
        aspiration()

def encounterSelect(gunny, butterbars, Istsgt):
#This is creating a list that will randomly spit out one of the three encounters
    encounterList = [gunny, butterbars, Istsgt]
    chance = random.randint(0,2)
    encounter = encounterList[chance]
    return encounter

def loot():
#This is creating loot and a list that will randomly spit out one of the three loot.
    loot = ['challenge coin', '6105', 'LOA']
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, marine):
#This is allowing the loot that you pick up to be applied to your marine's stats.
    if lootDrop == 'challenge coin':
        print('You take the challenge coin, increasing your motivation by 5')
        marine.motivation = marine.motivation + 5
        print('Your motivation is now...', marine.motivation)
        return marine
    
    elif lootDrop == '6105':
        print('You take the 6105, increasing your saltiness by 5')
        marine.salty = marine.salty + 5
        print('Your saltiness is now...', marine.salty)
        return marine
    
    elif lootDrop == 'LOA':
        print('You take the LOA, increasing your health by 20')
        marine.health = marine.health + 20
        print('Your health is now...', marine.health)
        return marine
    
def encounterState(score, marine):
#This is what starts an encounter. It uses the other functions to pull a random enemy from the encounter list.
#If you get past the enemy it resets their health for the next time you encounter them. It also adds to your score.
    enemy = encounterSelect(gunny, butterbars, Istsgt)
    print('A wild', enemy.name, 'has appeared.')
    print('What will you do?')
    while enemy.health > 1:
        choice = input('1. Give motivated response\n2. Give salty response\n3. Run!')

        if choice == '1': 
            print('You give a motivated response to the', enemy.name)
            stunchance = random.randint(0,10)
            if stunchance > 3:
                enemy.health = enemy.health - marine.motivation
                print('You stunned the', enemy.name, 'their health is now', enemy.health)

                if enemy.health > 1:
                    marine.health = marine.health - (enemy.strength / marine.defense)
                    print("The", enemy.name, 'is not pleased and blasts you! Your health is now...', marine.health)
                    gameOver(marine, score)

                else:
                    if enemy.name == 'Gunny':
                        enemy.health = 20
                        score = score + 20

                    elif enemy.name == 'Butterbars':
                        enemy.health = 10
                        score = score + 10

                    elif enemy.name == '1stSgt':
                        enemy.health = 30
                        score = score + 30

                    print('You have gotten pass the', enemy.name)
                    print('Looks like they gave you something.')
                    lootDrop = loot()
                    print ('You got a', lootDrop)
                    lootEffect(lootDrop, marine)
                    return score, marine
            else:
                print("Looks like they didn't hear you. Try using some volume!")
                print('The', enemy.name, 'is now irritated and blasts you!')
                marine.health = marine.health - enemy.strength
                print('Your health is now...', marine.health)
                gameOver(marine, score)

        elif choice == '2':
            print('You give a salty response to the', enemy.name)
            stunchance = random.randint(0,10)
            if stunchance > 3:
                enemy.health = enemy.health - marine.salty
                print('You stunned the', enemy.name, 'their health is now', enemy.health)

                if enemy.health > 1:
                    marine.health = marine.health - (enemy.strength / marine.defense)
                    print("The", enemy.name, 'is not pleased and blasts you! Your health is now...', marine.health)
                    gameOver(marine, score)

                else:
                    if enemy.name == 'Gunny':
                        enemy.health = 20
                        score = score + 20

                    elif enemy.name == 'Butterbars':
                        enemy.health = 10
                        score = score + 10

                    elif enemy.name == '1stSgt':
                        enemy.health = 30
                        score = score + 30

                    print('You have gotten pass the', enemy.name)
                    print('Looks like they gave you something.')
                    lootDrop = loot()
                    print ('You got a', lootDrop)
                    lootEffect(lootDrop, marine)
                    return score, marine

            else:
                print("Looks like they didn't hear you. Try using some volume!")
                print('The', enemy.name, 'is now irritated and blasts you!')
                marine.health = marine.health - enemy.strength
                print('Your health is now...', marine.health)
                gameOver(marine, score)
                
        elif choice == '3':
            print('You try to run away without being noticed...')
            escapechance = random.randint(1,5)
            if escapechance > 1:
                print('You get away safely!')
                return score, marine
                
            else:
                marine.health = marine.health - enemy.strength
                print('The', enemy.name, 'spotted you and blasts you for trying to avoid them! Your health is now...', marine.health)
                gameOver(marine, score)
        else:
            print('Please press 1, 2, or 3')
            encounterState(score, marine)
            
def SgtMaj_encounter(score, marine):
#This is the final encounter. If you pass this encounter you win the game. I am currently trying to resolve an issue with this function.
#If you restart the game the health is not reseting. 
    enemy = SgtMaj
    print('A wild', enemy.name, 'has appeared.')
    print('What will you do?')
    while enemy.health > 1:
        choice = input('1. Give motivated response\n2. Give salty response\n3. Run!')

        if choice == '1': 
            print('You give a motivated response to the', enemy.name)
            stunchance = random.randint(0,10)
            if stunchance > 3:
                enemy.health = enemy.health - marine.motivation
                print('You stunned the', enemy.name, 'their health is now', enemy.health)

                if enemy.health > 1:
                    marine.health = marine.health - (enemy.strength / marine.defense)
                    print("The", enemy.name, 'is not pleased and blasts you! Your health is now...', marine.health)
                    gameOver(marine, score)

                else:
                    if enemy.name == 'SgtMaj':
                        enemy.health = 100
                        score = score + 100
                    print('You have gotten pass the', enemy.name)
                    print('Looks like they gave you something.')
                    print ('You got a DD214! You Win!')
                    return score, marine
            else:
                print("Looks like they didn't hear you. Try using some volume!")
                print('The', enemy.name, 'is now irritated and blasts you!')
                marine.health = marine.health - enemy.strength
                print('Your health is now...', marine.health)
                gameOver(marine, score)

        elif choice == '2':
            print('You give a salty response to the', enemy.name)
            stunchance = random.randint(0,10)
            if stunchance > 3:
                enemy.health = enemy.health - marine.salty
                print('You stunned the', enemy.name, 'their health is now', enemy.health)

                if enemy.health > 1:
                    marine.health = marine.health - (enemy.strength / marine.defense)
                    print("The", enemy.name, 'is not pleased and blasts you! Your health is now...', marine.health)
                    gameOver(marine, score)

                else:
                    if enemy.name == 'SgtMaj':
                        enemy.health = 100
                        score = score + 100
                    print('You have gotten pass the', enemy.name)
                    print('Looks like they gave you something.')
                    print ('You got a DD214!')
                    return score, marine

            else:
                print("Looks like they didn't hear you. Try using some volume!")
                print('The', enemy.name, 'is now irritated and blasts you!')
                marine.health = marine.health - enemy.strength
                print('Your health is now...', marine.health)
                gameOver(marine, score)
                
        elif choice == '3':
            print('You try to run away without being noticed...')
            print("You can't escape!")

        else:
            print('Please press 1, 2, or 3')
            SgtMaj_encounter(score, marine)                
                
    
import time
score = 0
def start():
#This function starts the game. It begins with a input lines and calls on the other functions. 
    answer = input('Hello there! How would you like to join the United States Marine Corps?')
    if answer.lower().strip() == "yes":
        answer = input('Great! Do you have time to take a quick test called the ASVAB?')
        if answer.lower().strip() == 'yes':
            answer = input('Take this test and let me know if you pass or fail.')
        elif answer.lower().strip() == 'no':
            print('That is too bad. It would only take a few minutes to change your life.')
            for _ in range (1):
                word = ''.join(choice(string.ascii_lowercase) for _ in range(randint(1,8)))
                art.tprint('GAME OVER', font = 'dancing font')
                time.sleep(2)
                answer = input('Would you like to play again?')
                if answer.lower().strip() == 'yes':
                    start()
                elif answer.lower().strip() == 'no':
                    exit()
        else:
            print('Please type yes or no')
            start()
        if answer == 'I failed':
            answer = print('Yikes! I am going to recommend you head on over to the Army office a couple doors down. Have a nice day.')
            for _ in range (1):
                word = ''.join(choice(string.ascii_lowercase) for _ in range(randint(1,8)))
                art.tprint('GAME OVER', font = 'dancing font')
                time.sleep(2)
                answer = input('Would you like to play again?')
                if answer.lower().strip() == 'yes':
                    start()
                elif answer.lower().strip() == 'no':
                    exit()
        elif answer == 'I passed':
            answer == print('Great! You ship off to boot camp in two weeks!')
            time.sleep(3)
            score = 0
            marine = aspiration()
            time.sleep(3)
            score, marine = encounterState(score, marine)
            print('Score-',score)
            score, marine = encounterState(score, marine)
            print('Score-',score)
            score, marine = encounterState(score, marine)
            print('Score-', score)
            score, marine = SgtMaj_encounter(score, marine)
            winner(marine, score)
            
        else:
            print('Please type I passed or I failed.')
            start()

    elif answer.lower().strip() == "no":
        print("Yeah, you probably couldn't cut it anyways.")
        for _ in range (1):
                word = ''.join(choice(string.ascii_lowercase) for _ in range(randint(1,8)))
                art.tprint('GAME OVER', font = 'dancing font')
        time.sleep(2)
        answer = input('Would you like to play again?')
        if answer.lower().strip() == 'yes':
            start()
        elif answer.lower().strip() == 'no':
            exit()
    else:
        print('Please type yes or no')
        start()
start()