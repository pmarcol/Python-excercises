"""
Write a Python program to change the position of every n-th value with the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]

NOTE: The instruction is somewhat misleading, but example explains the concept well.
"""

"""
SOLUTION:
"""

def myShuffle(aList):
    out = []
    # prepare list of reference indices
    indices = [x for x in range(len(aList)) if x%2 == 1]
    for ind in indices:
        out += [aList[ind], aList[ind - 1]]
    if len(aList)%2 == 1:
        out += [aList[-1]]
    return out

myList1 = [1, 2, True, False, 3.14159, 1.61803]
myList2 = [1, 2, True, False, 3.14159, 1.61803, 'test']

print(myShuffle(myList1)) # [2, 1, False, True, 1.61803, 3.14159]
print(myShuffle(myList2)) # [2, 1, False, True, 1.61803, 3.14159, 'test']
    