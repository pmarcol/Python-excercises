"""
Write a Python program to print out a set containing all the colors from color_list_1
which are not present in color_list_2. Go to the editor
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}

NOTE: My solution will be more generic: the two sets of strings will be input by user.
"""

"""
SOLUTION:
"""

def SetsSubstraction(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.difference(set2)

inputString1 = input('Give me first list of strings:')
list1 = inputString1.split(',')
inputString2 = input('Give me second list of strings:')
list2 = inputString2.split(',')

print("%s" % SetsSubstraction(list1, list2))