#!/usr/bin/env python3

###     Create a program that does the following: 
###
### 1) Create a variable that holds a "magic number" between 0 and 10
### 2) Tell the user to pick a number between 0 and 10. 
### 3) If the user picks the "magic number", then tell them they've won!
### 4) Else, tell them to run the program again. 
###

# Import the random number library
import random

# set the initial values
the_number = random.randint(0, 10)
# tries = 1
triesLimit = 3

# Create the "magic number" function
def magic_number_intro():
    print("The magic number function... \n")
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 0 and 10.")

def guess_loop():
    # Ask the question
    guess = int(input("Take a guess (preferably within {} attempts..): ".format(triesLimit)))
    tries = 1

    # guess while you still can
    while tries < triesLimit and not guess == the_number :
        #Test Entry: 
        print("{} is guess, {} is the number and {} is amount of tries thus far...\n".format(guess, the_number, tries))
        if guess > the_number :
            # print("Guess lower...")
            guess = int(input("Guess lower: "))
        elif guess < the_number :
            # print("Guess higher...")
            guess = int(input("Guess higher: "))
        else:
            print("ERRONEOUS INPUT!!! \n\tEXITING...\n")
            break
        # guess = int(input(": "))
        tries += 1
    # return guess, the_number, tries, triesLimit
    # guess, the_number, tries, triesLimit = guess_loop()
    #Test Entry: 
    # print("From within \"wash_up\", {} is guess, {} is the number and {} is amount of tries thus far...\n".format(guess, the_number, tries))

    if triesLimit <= tries : 
        print("\nYou've reached your limit of {} guesses - try again, if you want".format(triesLimit))
        print("The number randomly generated was {}\n".format(the_number))
        # break
    elif guess == the_number :
        print("\nYou guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!")
        # break

# Call the salient functions
magic_number_intro()
guess_loop()
# wash_up_function()
# wash_up_function(guess_loop(guess, the_number, tries, triesLimit))

# Finish up!
input("Press the <ENTER> key to exit.")
