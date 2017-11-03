"""
Write a Python program to generate all sublists of a list.
"""

"""
SOLUTION:
"""

def sublists(aList):
    out = []
    temp = []
    aLen = len(aList)
    for startInd in range(aLen):
        for ln in range(aLen - startInd + 1):
            temp = aList[startInd:(startInd + ln)]
            if temp not in out:
                out.append(temp)
    return out

myList = [1, 2, 3, 4, 5]

print(sublists(myList))