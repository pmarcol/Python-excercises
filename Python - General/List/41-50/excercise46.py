"""
Write a Python program to select the odd items of a list.

NOTE: Instructions unclear. I thought that actually odd numbers must remain;
turns out, that the objective was to print elements on odd positions in the original list.
"""

"""
SOLUTION:
"""

def myFunc(aList):
    return [x for x in aList if x% 2 == 1]

def origSolution(aList):
    return aList[::2]

myList = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]

print(myFunc(myList))       # [1, 3, 5, 7, 9]
print(origSolution(myList)) # [1, 2, 4, 6, 8]
