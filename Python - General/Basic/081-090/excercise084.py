"""
Write a Python program to count the number occurrence of a specific character in a string.
"""

"""
SOLUTION:
"""

def countCharInString(myChar, myString):
    return myString.count(myChar)

theString = input("Give me a string: ")
while True:
    theChar = input("Give me a character: ")
    if(len(theChar) != 1):
        print("You should give exactly one character.")
        continue
    else:
        break

print(countCharInString(theChar, theString))