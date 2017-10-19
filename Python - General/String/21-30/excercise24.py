"""
Write a Python program to check whether a string starts with specified characters.
"""

"""
SOLUTION:
"""

#mine
def StartsWith1(mainStr, subStr):
    return mainStr[:len(subStr)] == subStr

#from the source page, it turns out there is dedicated function for that
def StartsWith2(mainStr, subStr):
    return mainStr.startswith(subStr)

print(StartsWith1("Python", "Py"))   #True
print(StartsWith1("Test", "Py"))     #False

print(StartsWith2("Python", "Py"))   #True
print(StartsWith2("Test", "Py"))     #False