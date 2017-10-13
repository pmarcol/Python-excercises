"""
Write a Python program to split a variable length string into variables.

NOTE: Ech, once again - I do not fully understand the task. I have a clue, but totally not sure about it.
"""

"""
SOLUTION:
"""

#Solution from source
"""
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)

var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)
"""

# NOTE: Okay, after analyzing the solution:
# the assumption here is that we have some input list,
# but we cannot be sure what's inside - it can be empty, have only one value etc.
# So we append 'None' as many times, as many variables we want to get (in case the list is empty).
# Below I wrote a function that does similar thing, but inserts the variables into new list
# (note, that ([1])[:3] would still give [1], and we would like to get 1, None, None)
# I get them in form of list, because I want the number of variables to be passed as parameter

def getVariablesFromList(aList, num):
    outList = (aList + [None]*num)[:num]
    return outList

print(getVariablesFromList([1],3))          #[1, None, None]
print(getVariablesFromList([],2))           #[None, None]
print(getVariablesFromList([1,2,3,4,5],2))  #[1, 2]