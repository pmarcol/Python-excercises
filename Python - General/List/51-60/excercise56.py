"""
Write a Python program to convert a string to a list.
"""

"""
SOLUTION:
"""

def strToList(aString):
    return list(aString)

myString = "testString123;\nA"

print(strToList(myString)) # ['t', 'e', 's', 't', 'S', 't', 'r', 'i', 'n', 'g', '1', '2', '3', ';', '\n', 'A']

# Ok, turns out I misunderstood the instructions again. Here's what it was about.

import ast
color ="['Red', 'Green', 'White']"
print(ast.literal_eval(color))