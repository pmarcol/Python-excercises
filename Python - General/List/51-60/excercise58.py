"""
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

"""
SOLUTION:
"""

def myFunc(list1, list2):
    # in original solution:
    # list1[-1:] = list2.
    # Nice, good to know.
    return (list1[:-1] + list2)


my1 = [1, 3, 5, 7, 9, 10]
my2 = [2, 4, 6, 8]

print(myFunc(my1, my2))