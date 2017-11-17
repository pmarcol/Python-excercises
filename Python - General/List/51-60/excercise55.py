"""
Write a Python program to remove key values pairs from a list of dictionaries.

Note: I wasn't sure what am I supposed to do, so I peeked into the solution. The objective is to delete
key+value from all dictionaries in the list for certain key.
"""

"""
SOLUTION:
"""

# very nice! Turns out double fors may be a little bit hard to read, but clever.
def origSolution(aList, aKey):
    return [{k: v for k, v in d.items() if k != aKey} for d in aList]

# that's how I would do this if I was said to.
def mySolution(aList, aKey):
    # damn! first I tried to make a copy of the input list by outList = list(aList) or ... = aList.copy(),
    # BUT! turns out that the dictionaries inside were referencing the same object, so dic.pop(...) affected also the input list.
    # Strange.
    import copy
    outList = copy.deepcopy(aList)
    for dic in outList:
        dic.pop(aKey, None)
    return outList

myList = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
myKey = 'key1'

#print(origSolution(myList, myKey))  # [{'key2': 'value2'}, {'key2': 'value4'}]
#print(myList)
#print(mySolution(myList, myKey))    # [{'key2': 'value2'}, {'key2': 'value4'}]
#print(myList)

mySolution(myList, myKey) 