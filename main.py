#Code
import random
import colorama
from colorama import Fore, Back
import time
#Nothings
turns = 100
keys = 0
friends = 0
x_coords = 0
y_coords = 0
#Story Start
print(Fore.WHITE + "This game is not real")
print("If you feel Frighten click of you have been warn.")
name = input(Fore.RED + 'Sign Here')
print(Fore.BLUE + name, " this will be your last day. Your life will come to an end.")
time.sleep(2)
print("Your body will rot as life will leave your body.")
time.sleep(2)
print("But this is just the beginning of the day so come along.")
print("You and your friends, Jayden and De'Lady meet up in a park.")
time.sleep(2)
print("You went and spoke to your friends, you talk for hours and hours until it became dark outside.")
print("You and your friend talk about the new corn maze in the town that only appears in the dark.")
choice = input("They ask you if you want to go to the maze since it's dark outside?(Y/N)")
if choice == "Y" or "y":
    print(Fore.WHITE + "Ending 1/5 \b  The scarey cat ending.")
    time.sleep(3)
    exit()
print("You deiced to go to the maze but on your way you were almost hit by the train with your friends")
print("You entered the maze as the door slowly shut.")
print("Your friends start to panic as you all here a voice saying collect all of the keys.")
print("You are able to walk in the maze by going North, West, South, and East.")
print("Controls: 1 is North, 2 is South, 3 is West, 4 is East. Find all the keys and there are challenges you must face so be were. And you must complete the maze in under 100 moves if you don't you will be trap forever.")
while keys != 3:
    walk = int(input("Where to go?"))
    turns = -1
    if walk == 1:
        y_coords = +1
    elif walk == 2:
        y_coords = -1
    elif walk == 3:
        x_coords = -1
    elif walk == 4:
        x_coords = +1
    if x_coords == 10 and y_coords == 5:
        print("You found a key area but in order to pass you must beat the rock in Rock, Paper, Scissors if you lose you will lose a life, lose one your friend dies, lose all you die.")
        choice1 = int(input("Controls: 1 is rock, 2 is paper, 3 is scissors. "))
        lives = 3
        while choice1 != random.randrange(1,3):
            lives = -1
            print("Wrong")
            choice1 = int(input("You have ", lives, " left hurry one already died. "))
            if lives <= 0:
                friends = +1
                print(Fore.WHITE + "Ending 2/5 died by trying to collect a key.")
                time.sleep(2)
                exit()
        print("Good job you obtain a key.")
        keys = +1
    elif x_coords == 0 and y_coords == -6:
        print("You found a key area")
        print("You found it but you must guess a password with the riddle 'I have cities, but no houses; I have mountains, but no trees; I have water, but no fish; I have roads, but no cars. What am I?'")
        print("You have 3 chances if you fail you will die. and lose one your friend dies")
        lives = 3
        guess = input("'I have cities, but no houses; I have mountains, but no trees; I have water, but no fish; I have roads, but no cars. What am I?' ")
        while guess != "a map" or "A map" or "A Map":
            lives = -1
            friends = +1
            print("Wrong")
            guess = input("'I have cities, but no houses; I have mountains, but no trees; I have water, but no fish; I have roads, but no cars. What am I?' ")
            if lives <= 0:
                print(Fore.WHITE + "Ending 2/5 died by trying to collect a key.")
                time.sleep(2)
                exit()
        print("You found the key but there is another riddle but harder. AAnd your lives are the same")
        guess = input("'I exist always, but have no form. I am perceived by all, but have no voice. I have no beginning and no end, yet I shape the course of everything. What am I?' ")
        while guess != "Time":
            lives = -1
            friends = +1
            print("Wrong")
            guess = input("'I exist always, but have no form. I am perceived by all, but have no voice. I have no beginning and no end, yet I shape the course of everything. What am I?' ")
            if lives <= 0:
                print(Fore.WHITE + "Ending 2/5 died by trying to collect a key.")
                time.sleep(2)
                exit()
        print("You got another key.")
        keys = +1
    elif x_coords == 30 and y_coords == -20:
        print("You founded a key but to escape you must a unscramble  word.")
        guess = input("oladneriidhtonatrenneketnnuhmigdrd ")
        lives = 3
        while guess != "The United Kingdom And Northern Ireland" or "the united kingdom and northern ireland":
            lives = -1
            friends = +1
            print("Wrong")
            guess = input("oladneriidhtonatrenneketnnuhmigdrd ")
            if lives <= 0:
                print(Fore.WHITE + "Ending 2/5 died by trying to collect a key.")
                time.sleep(2)
                exit()
        print("You got a key")
        keys = +1
    if turns >= 0:
        print(Fore.WHITE + "Ending 3/5 died by getting trap and the area transforming into Hell.")
        time.sleep(2)
        exit()
if friends > 0:
    print(Fore.WHITE + "Ending 4/5 Friends Lost \b You were able to escape but your friends all died as you escape the maze in sorrow you walk into a staircase walking all the way up to the sky  with a white color. The End")
    time.sleep(2)
    exit()
else:
    print(Fore.WHITE + "Ending 5/5 The True End \b You were able to escape with your friends as you walk up and insert your keys you felt a breeze and the staircase appeared. As you walked up the white gates open as you see a perfect place to rest as you faded away.")
    time.sleep(2)
    exit()    
            
