# Module Import, Type Conversion, User Input, While Loop w/Comparison Operators

import random

guess=0

guesses=0

answer=random.randint(1,100)

while guess !=answer:

    guesses+=1

    guess=int(input("Please guess a number between 1 an 100: "))

    if answer < guess:
        print("Your guess is too high, please try again.")

    elif answer > guess:
        print("Your guess is too small, please try again.")
    
    else:
        print(f"Great!! You have guessed the number in {guesses} guesses!")

