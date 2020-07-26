#!/usr/bin/env python3

"""
30 Simple Tricks to Level Up Your Python Coding; 
taken from "https://medium.com/better-programming/30-simple-tricks-to-level-up-your-python-coding-5b625c15b79a"

"""

print("30 Simple Tricks to upgrade one's Python Coding\n")

print("\n###\t1. Slicing a sequence")
t0nym = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
print(*t0nym, "... is the list we're using to demonstrate...")
print(len(t0nym), "- number of elements in the list")
print(t0nym[1:3], "is the 2nd through 3rd element list.")
print(t0nym[1:9:2], "= returning every other even number (using a range with a step)")
print(t0nym[:5], "- print the first 5 elements.")
print(t0nym[9:], "- print from the ninth element 'til the end.")
print(t0nym[:], "- print the entire list.")

print("\n\n###\t2. Reversing a sequence - see CODE for examples")
print(t0nym[::-1], "...as stated")
b = 'start'
print("b = 'start', so reversing it will be thus: \"", b[::-1], "\"")

print("\n\n###\t3. Reverse Indexing examples")
print(t0nym[-1], "- element traversal and search using reverse indexing instead of using a[len(a)-1]")
print(t0nym[-5:-1], "- in combination with slicing, using \"a[-5:-1]\"")



print("\n\n###\t4. Multiple Variable Assignments")   
tee, mac = 8, 5
print("\t...tee, mac = 8, 5, INSTEAD of assigning with tee = 8; mac = 5")
print(f'\t...therefore tee is {tee}; mac is {mac}')
nubbers = [1, 2, 3, 4, 5]
print("Swap the first and last elements in a list containing [1, 2, 3, 4, 5] ")
print("... using nubbers[0], nubbers[-1] = nubbers[-1], nubbers[0]")
nubbers[0], nubbers[-1] = nubbers[-1], nubbers[0]
print("we get: ", *nubbers)


print("\n\n###\t5. Check if a Sequence Is Empty")
print("Using \"empty_list = [(), '', [], {}, set()]\"")
print("...we print")
empty_list = [(), '', [], {}, set()]
for item in empty_list:
    if not item:
        print(f'\t...defining and hence printing {type(item)}')


print("\n\n###\t6. List Comprehensions")        
print("Basically, demonstrating \"[<some_expression> for element in iterable if <some_condition>]\"")
nubberList = [1, 2, 3, 4, 5]
print("\t...using [x*9 for x in nubberList]")
# print(*nubberList)
print("\t...therefore, acting on each list member will result in ", [x*9 for x in nubberList])

print("And a tad more complex, using [x*3 for x in nubberList if x%2 == 1] : ", [x*3 for x in nubberList if x%2 == 1])
print("\t...basically, multiplying each element ONLY if it's resultant modulus is \"1\"")

print("\n\n###\t7. Set Comprehensions")        
print("The difference is that we’ll use the curly brackets instead of square brackets. \nAlso, the duplicate elements will get removed by the definition of the set data type.")
print("\t...ergo, using the list \"zed = [1, -2, 2, -3, 3, 4, 4, 5, 5, 5]\" ")
zed = [1, -2, 2, -3, 3, 4, 4, 5, 5, 5]
###   {x*x for x in zed} and print (x)
print("\tusing {x*x for x in zed}, will result in:", {x*x for x in zed}, "\nNote the negative number enumeration...")


# print("")""
# print("")
# print("")
# print("")
# print("")\n
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")