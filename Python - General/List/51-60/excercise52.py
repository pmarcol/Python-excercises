"""
Write a Python program to compute the similarity between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output: 
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']

Note: Seems like simple set difference. I will implement it this way.
Note2: Also nice solution with Counter() on the source page.
"""

"""
SOLUTION:
"""

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

print(list(set(list1).difference(set(list2)))) # ['white', 'orange', 'red'] not necessarily in this order
print(list(set(list2).difference(set(list1)))) # ['black', 'yellow'] not necessarily in this order