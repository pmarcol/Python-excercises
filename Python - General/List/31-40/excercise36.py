"""
Write a Python program to get variable unique identification number or string.
"""

"""
SOLUTION:
"""

myVars = [True, 100, 3.14, 'test']
testVar1 = 'test'
testVar2 = 'test'

print(format(id(myVars), 'x'))
print(format(id(testVar1), 'x'))
print(format(id(testVar2), 'x')) # the last two ones will have the same ids