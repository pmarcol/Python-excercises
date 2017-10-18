"""
Write a Python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3 then return the original string.
Sample function and result : 
first_three('ipy') -> ipy
first_three('python') -> pyt
"""

"""
SOLUTION:
"""

def giveThreeFirst(myStr):
    return myStr[:3]

print(giveThreeFirst("te"))             #te
print(giveThreeFirst("myTestString"))   #myT