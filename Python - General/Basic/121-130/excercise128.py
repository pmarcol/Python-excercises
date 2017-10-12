"""
Write a Python program to check if lowercase letters exist in a string.
"""

"""
SOLUTION:
"""

def lowerExist1(myStr):
    for char in myStr:
        if char.islower(): return True
    return False

def lowerExist2(myStr):
    return any(char.islower() for char in myStr)

str1 = 'TEST'
str2 = 'TEsT'
str3 = 'test'

print(lowerExist1(str1)) #False
print(lowerExist1(str2)) #True
print(lowerExist1(str3)) #True

print('')

print(lowerExist2(str1)) #False
print(lowerExist2(str2)) #True
print(lowerExist2(str3)) #True