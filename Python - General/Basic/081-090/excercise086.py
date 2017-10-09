"""
Write a Python program to get the ASCII value of a character.
"""

"""
SOLUTION:
"""

def getAscii(myChar):
    return ord(myChar)

while True:
    theChar = input("Give me a character: ")
    if(len(theChar) != 1):
        print("You should give exactly one character.")
        continue
    else:
        break

print(getAscii(theChar))