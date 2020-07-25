#! /usr/bin/env python3

### Print Lists in 4 different ways - from https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

# Python program to print list using for loop 
a = [6, 9, 3, 12, 15] 

# printing the list using loop 
print("\nFirst Lesson")
print(*a)
# for x in a: 
for x in range(len(a)): 
    # print(len(a))
    # print(x)
    print(a[x])    
print("The above is incorrect; should be in one line(?)")
    
# Python program to print list WITHOUT using loop 
# printing the list using * operator separated  
# by space  
print("\nSecond Lesson")
print(*a) 
  
# printing the list using * and sep operator 
print("\nThird Lesson")
print("printing lists separated by commas") 
print(*a, sep = ", ")  
  
# print in new line 
print("\nForth Lesson")
print("printing lists in new line") 
print(*a, sep = "\n") 

# Convert a list to a string for display
print("\nFifth Lesson - using \"join\"")
# Python program to print list by converting a list to a string for display 
a =["Geeks", "for", "Geeks"] 
# print the list using join function() 
print(' '.join(a)) 
  
# print the list by converting a list of integers to string
print("\nSixth Lesson - convert to a string for printing")  
a = [1, 2, 3, 4, 5] 
print(str(a)[1:-1])


#  Using map : Use map() to convert each item in the list to a string if list is not a string, and then join them:
# Python program to print list print the list by converting a list of integers to string using map 
print("\nSeventh Lesson - using \"map\" to convert integers to a string for printing") 
# a = [1, 2, 3, 4, 5] 
print(' '.join(map(str, a)))  
print("print each index on a new line")
print('\n'.join(map(str, a))) 