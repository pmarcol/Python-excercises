"""
Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python

NOTE: It seems that the solution on the source page does not reflect the instructions (which are not very clear TBH).
The objective here is to use str.rsplit(del, 1)[0], but I would argue about the maxsplit parameter value = 1.`
"""

"""
SOLUTION:
"""

def getSubBeforeSep(myStr, sep):
    return myStr.rsplit(sep,1)[0]

myStr = "https://www.w3resource.com/python-exercises/string"
print(getSubBeforeSep(myStr,"/")) #https://www.w3resource.com/python-exercises
print(getSubBeforeSep(myStr,"-")) #https://www.w3resource.com/python