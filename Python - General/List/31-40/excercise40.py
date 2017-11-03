"""
Write a Python program to split a list based on first character of word.

NOTE: Not sure what am I supposed to do.

EDIT: I peeked at solution and modified it so there is a function that returns a dictionary
with first letters as keys and lists of words starting with this letter as values
"""

"""
SOLUTION:
"""
def myGroup(aList):
    from itertools import groupby
    from operator import itemgetter
    outDic = {}
    for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
        temp = []
        for word in words:
            temp.append(word)
        outDic[letter] = temp
    return outDic


word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

myDictionary = myGroup(word_list)
print(myDictionary['a']) # ['ask']
print(myDictionary['g']) # ['get', 'give', 'go']
print(myDictionary['z']) # KeyError: 'z'