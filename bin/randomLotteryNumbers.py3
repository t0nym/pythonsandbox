#!/usr/bin/env python3

###     Create a program that does the following: 
###
### 1) Creates 6 lottery numbers - none of which should be repeated. 
### 2) Print list content in a straight line.
### 3) Print list in a numeric order. 
###

# Import the random number library
import random
import os

###     Create list:
lotteryNos=[]

###         Some jazzy way of demonstrating some print formatting..
name="Tony"
surname="McKenzie"
monikername="t0nym"

print('\nMy name is', os.getlogin(), 'and I am ancient.')
print('Some interesting stuff in here...')

while len(lotteryNos) < 6:
    numeric = random.randint(1, 59)
    if numeric not in lotteryNos:
        lotteryNos.append(numeric)

### Test Entry... 
# print(lotteryNos)
lotteryNos.sort()
### Test Entry... 
# print(lotteryNos)
# print(lotteryNos)
###     'maps' numbers to a string for printing purposes... 
print("This is a randomly generated list of sorted numbers bound for the lottery..\n") 
print(' '.join(map(str, lotteryNos)), "\n")
