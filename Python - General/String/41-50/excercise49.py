"""
Write a Python program to count and display the vowels of a given text.
"""

"""
SOLUTION:
"""

def countVowels(aStr):
    myTrans = str.maketrans('','','aeiouy')
    lowStr = aStr.lower()
    return len(aStr) - len(lowStr.translate(myTrans))

myStr = "mytEsTStrIngForCOuNtIngvOwels"

print(countVowels(myStr))   # 9