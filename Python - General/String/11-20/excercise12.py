"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

"""
SOLUTION:
"""

def countOccurences(myStr):
    words = myStr.split()
    wordsSet = set(words)
    myDic = {}
    for word in wordsSet:
        myDic[word] = words.count(word)
    return myDic

myStr1 = "sto lat sto lat niech zyje zyje nam"
myStr2 = "test test1 test test2 test test3"

print(countOccurences(myStr1))
print(countOccurences(myStr2))