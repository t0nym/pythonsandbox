#! /usr/bin/env python3

###     Exercise in code structuring - best for git diff analagies
countries=[
            'China', 
            'Russia', 
            'USA',
            'Jamaica'
            ]

print("First iteration")
print(*countries)

print("Second iteration")
print(*countries, end='.')
print("\n")

print("Third iteration")
print(*countries, end='.\n')

print("\nForth iteration - introduction to the \"set\" method... basically it removes duplicates")
countries=['China',
           'USA',
           'Jamaica',
           'Jamaica',
           'UK',
           'China'
           ]
print(*countries)
print('Turns {0} into:'.format(countries))
print(sorted(set(countries),key=countries.index))

#Set Comprehension
print("\nFifth iteration - Set Comprehension")
print({ x+1 for x in range(5)})

#Dict Comprehension
print("\nSixth iteration - Dictionary Comprehension")
print({ x:x+1 for x in range(5)})

print("\nSeventh iteration - switching variables")
a,b=[1,2]
print('a,b=[1,2]')
a,b=b,a
print('a,b=b,a')
print("\"a\" is now {0} and \"b\" is now {1}!!!".format(a,b))