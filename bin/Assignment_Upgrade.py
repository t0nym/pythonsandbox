#!/usr/bin/env python3

###     Pls Note!
###     Upgrade version is to split the "guess_loop" function and utilise the "wash_up_function" 
###   I attempted to work on yesterday. 
###     Also cleaned up in places deemed fitting. 
###

###########################
###
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
theNumber = random.randint(0, 10)
# tries = 1
triesLimit = 3

# Create the "magic number" function
def magic_number_intro():
    print("The magic number function... \n")
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 0 and 10.")

#   this should be obvious - "guess_loop"... duh!
def guess_loop():
    # Ask the question
    guess = int(input("Take a guess (preferably within {} attempts..): ".format(triesLimit)))
    tries = 1

    # guess while you still can
    while tries < triesLimit and not guess == theNumber :
        #Test Entry: 
        print("{} is guess, {} is the number and {} is amount of tries thus far...\n".format(guess, theNumber, tries))
        if guess > theNumber :
            # print("Guess lower...")
            guess = int(input("Guess lower: "))
        elif guess < theNumber :
            # print("Guess higher...")
            guess = int(input("Guess higher: "))
        else:
            print("ERRONEOUS INPUT!!! \n\tEXITING...\n")
            break

        tries += 1
    return guess, theNumber, tries, triesLimit

    # guess, theNumber, tries, triesLimit = guess_loop()
    #Test Entry: 
    # print("From within \"wash_up\", {} is guess, {} is the number and {} is amount of tries thus far...\n".format(guess, theNumber, tries))

def wash_up_function(guess, theNumber, tries, triesLimit):
    if guess == theNumber :
        print("\nYou guessed it!  The number was", theNumber)
        print("And it only took you", tries, "tries!")
    elif triesLimit == tries : 
        print("\nYou've reached your limit of {} guesses - try again, if you want".format(triesLimit))
        print("The number randomly generated was {}".format(theNumber))

# Call the salient functions
magic_number_intro()
# guess_loop()
wash_up_function(*guess_loop())
# wash_up_function(guess_loop(guess, theNumber, tries, triesLimit)) ### This is WRONG and will give you errors!!!

# ... and a good programmer always finishes up nicely?
input("Press the <ENTER> key to exit.")

