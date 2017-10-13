"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'

NOTE: There is a little mess in the instructions. Don't know where the 'bad' part came from.
My approach: Find first occurence of 'not' and first occurence of 'poor'. If the first comes before the latter,
replace 'not .. poor' substring LIMITED BY THE VERY MENTIONED OCCURENCES (original solution would replace every occurence 
of such substring if it was possible)
"""

"""
SOLUTION:
"""

def myFunc(aString):
    indOfNot = aString.find('not')
    indOfPoor = aString.find('poor')
    out = aString[:indOfNot] + 'good' + aString[indOfPoor+4:]
    return out

myStr = 'The lyrics is not that poor!'
print(myFunc(myStr))