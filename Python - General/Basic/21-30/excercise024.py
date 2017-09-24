"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

"""
SOLUTION:
"""

def isVowel(aString):
    return (['a','e','i','o','u','y']).count(aString) > 0

while True:
    myString = input("Give me a letter:")
    if((len(myString) != 1) or not(myString.isalpha())):
        print("You should give exactly one letter. Try again.")
        continue
    else:
        break

print("Given letter is a vowel: %s" % (isVowel(myString)))
