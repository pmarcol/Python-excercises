"""
Write a Python function that takes a list of words and returns the length of the longest one.
"""

"""
SOLUTION:
"""

def myFunc(myList):
    max = 0
    for aStr in myList:
        if not(isinstance(aStr, str)):
            print("All elements should be strings")
            return
        if len(aStr) > max:
            max = len(aStr)
    return max

print(myFunc(['test', 'long_word','test1'])) #9
print(myFunc(['test', 1]))                   #Error