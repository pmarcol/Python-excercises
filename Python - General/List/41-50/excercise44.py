"""
Write a Python program to generate groups of five consecutive numbers in a list.

Note: My solution is more generic - it takes a number and generates list of lists of groups of five consecutive numbers.
In the last group there will be numbers up to the given one.
"""

"""
SOLUTION:
"""

def myFunc(num):
    outList = []
    for i in range(num//5):
        outList.append(list(range(5*i + 1, 5*i + 6)))
    if num % 5 != 0:
        outList.append(list(range(5*(num//5) + 1, num + 1)))
    return outList

print(myFunc(12))   # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12]]
print(myFunc(10))   # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(myFunc(9))    # [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
print(myFunc(0))    # []