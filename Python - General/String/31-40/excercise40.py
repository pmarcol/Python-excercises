"""
Write a Python program to reverse words in a string.
"""

"""
SOLUTION:
"""

def reverseWords(aStr):
    words = aStr.split()
    return ' '.join(words[::-1])

myStr1 = "The quick brown fox jumps over the lazy dog."
myStr2 = "Python Exercises."

print(reverseWords(myStr1))
print(reverseWords(myStr2))