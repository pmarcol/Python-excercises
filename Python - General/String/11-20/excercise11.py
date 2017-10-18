"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

"""
SOLUTION:
"""

def OddIndexes(myStr):
    out = ''.join([myStr[i] for i in range(len(myStr)) if i%2 == 1]) # i%2 == 1 - it's the matter of interpretation. Could be i%2 == 0
    return out

print(OddIndexes("myTestStringNumber1")) #yettigubr