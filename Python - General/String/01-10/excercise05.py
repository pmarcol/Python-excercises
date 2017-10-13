"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
"""

"""
SOLUTION:
"""

def myFunc(str1, str2):
    #both must have length of at least 2:
    if min(len(str1), len(str2)) < 2:
        print("Both strings must have length of at least 2")
        return
    out = str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]
    return out

print(myFunc("abc", "xyz"))
print(myFunc("a", "xyz"))
print(myFunc("abc", "x"))
print(myFunc("ab", "xy"))
