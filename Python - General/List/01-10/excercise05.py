"""
Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

"""
SOLUTION:
"""

def myFunc(aList):
    out = 0
    for el in aList:
        if len(el) and el[0] == el[-1]:
            out += 1
    return out

myList = ['abc', 'xyz', 'aba', '1221']

print (myFunc(myList)) #2