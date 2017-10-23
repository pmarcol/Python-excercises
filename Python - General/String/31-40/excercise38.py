"""
Write a Python program to count occurrences of a substring in a string.
"""

"""
SOLUTION:
"""

def countSubs(main, sub):
    return main.count(sub)

myMain = "test, test1, test2, test3, test1test"
mySub1 = "test1"
mySub2 = "test"

print(countSubs(myMain, mySub1)) #2
print(countSubs(myMain, mySub2)) #6
