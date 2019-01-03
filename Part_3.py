'''
Created on Jan 3, 2019
@author: kwilliams-koester21
'''

import random
wrong = 0
correct = 0
rounds = int(input("How many rounds of the game should be simulated: "))
while rounds < 10 or rounds > 10000:
    print("Must enter a number between 10 and 10,000")
    rounds = int(input("Please try again: "))
change = input("Should the player 'switch' or 'stay':")
while change.lower() != 'stay' and change.lower() != 'switch':
    change = input("Please try again:")
for i in range (0,rounds,1):
    if change.lower() == 'switch':
        car = random.randint(1,4)
        guess = random.randint(1,4)
        if car == 1 and guess == 1:
            guess = int(3)
            wrong += 1 
        elif car == 2 and guess == 2:
            guess = int(1)
            wrong +=1
        elif car == 3 and guess == 3:
            guess = int(2)
            wrong +=1
        elif car == 1 and guess == 2:
            guess = int(1)
            correct += 1
        elif car == 1 and guess == 3:
            guess = int(1)
            correct +=1
        elif car == 2 and guess == 1:
            guess = int(2)
            correct += 1 
        elif car == 2 and guess == 3:
            guess = int(2)
            correct += 1
        elif car == 3 and guess == 1:
            guess = int(3)
            correct += 1 
        elif car == 3 and guess == 2:
            guess = int(3)
            correct += 1
    if change.lower() =='stay':
        car = random.randint(1,4)
        guess = random.randint(1,4)
        if car == 1 and guess == 1:
            correct += 1 
        elif car == 2 and guess == 2:
            correct +=1
        elif car == 3 and guess == 3:
            correct += 1 
        else:
            wrong += 1 
print("The player won",correct,"/",rounds,"games (",format((correct/rounds)*100,'3.2f'),"%)!")