#Made the repo to learn python while also doing some fun stuff







#Should start the code around here somewhere

import random
import math
import secrets
import json
import time
import pygame




#Need to make a database to store basic player info like how much money and their name


print ("Welcome to Rubi Palace, what game would you like to play today.")
with open('data.json' , 'r') as file:
    pass

# Slots basic logic, sucks ass need to upgrade

print ("Welcome to the slot machine sim, enter x to spin")

while True:

    tr = input()

    if tr != "x" :

        print("wrong input, enter x to start")

    else:

        while True:

            n1 = random.randrange(0, 9, 1)

            n2 = random.randrange(0, 9, 1)

            n3 = random.randrange(0, 9, 1)

            print( "\n Slotted numbers are", n1, n2, n3)

            if n1 == n2 == n3 == 7:

                print(f"Congratulations on hitting the jackpot")

            user = input("Press e to reroll or anything else to quit ==> ")

            if user != "e" :

                print("Thx for playing")

                break

        break