"""
Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

"""
SOLUTION:
"""

myList = [45, 55, 60, 37, 100, 105, 220]

out = list(filter(lambda x: (x%15 == 0), myList)) 

print(out)

#additionally: filter with two conditions, say, divisible by both 15 and 2:
#out = list(filter(lambda x: (x%15 == 0 or x%2 == 0), myList)) 