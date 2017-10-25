"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black'] 
"""

"""
SOLUTION:
"""

def delete045(aList):
    del aList[4:6]
    del aList[0]
    return aList

myList = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(delete045(myList)) # [1, 2, 3, 6, 7, 8, 9]
print(delete045([0, 1, 2, 3])) # [1, 2, 3]