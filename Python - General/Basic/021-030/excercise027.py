"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""

"""
SOLUTION:
"""

def myConcat(myList):
    output = ''
    for word in myList:
        output += word
    return output

inputString = input('Give me list of strings:')
elements = inputString.split(',')

print(myConcat(elements))