"""
Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350

NOTE: I hope to make more generic function, not only for ints
"""

"""
SOLUTION:
"""

def myConcat(aList):
    return ''.join([str(x) for x in aList])

myList1 = [11, 33, 50]
myList2 = [21, True, 3.14159, 'test']

print(myConcat(myList1)) # 113350
print(myConcat(myList2)) # 21True3.14159test