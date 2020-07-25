#! /usr/bin/env python3

###     Print a column of numbers
print("Print nubbers in a range of 4")
for numbers in range (4):
    print(numbers)

print()
print("Print strings from within a list")   
distro = ["ubuntu", "mint", "elementary"]
for xyz in distro:
    print (xyz)
    
print()
print("Print leters from a word")
for xyz in "ubuntu":
    print(xyz)
    
print()
print("Print from a list and break on \"mint\"")
for xyz in distro:
    print (xyz)
    if xyz == "mint":
        break
print()
print("Print from a list and skip \"mint\"")
for xyz in distro:
    if xyz == "mint":
        continue
    print (xyz)
    
print()
print("Print from a nested loop of 2 x lists")
linux = ["secure", "superior"]
for x in distro:
    for y in linux:
        print (x,y)
        
print()
print("Print nubbers in a range and then demonstrate \"else\"")
for numbers in range (4):
    print(numbers)
else:
    print("Good Job")
    
print()
print("Using \"pass\" to demonstrate empty statement whilst avoiding an error")
for numbers in range (4):
    pass
print("Finished loop... ")