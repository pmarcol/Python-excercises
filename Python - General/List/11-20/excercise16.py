"""
Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30 (both included).
"""

"""
SOLUTION:
"""

def myFunc():
    myList = [x**2 for x in list(range(1,31))]
    return myList[:5] + myList[-5:]

print(myFunc())