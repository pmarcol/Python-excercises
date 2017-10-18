"""
Write a Python function to insert a string in the middle of a string.
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

NOTE: Ok, so if you look at the solution on the source page, you will see, that it is just as hardcoded as only can be:
tag[:2] + theString + tag[2:]
I will try to come up with something more clever.
"""

"""
SOLUTION:
"""

def insertStringIntoString(strToBeSplit, strToBeInserted):
    mid = len(strToBeSplit)//2 #if the result will not be int, it will be rouded down - sa little modification can make it be rounded up instead.
    return strToBeSplit[:mid] + strToBeInserted + strToBeSplit[mid:]

print(insertStringIntoString("<<>>", "something"))  #<<something>>
print(insertStringIntoString("{{#}}", "test"))      #{{test#}}
print(insertStringIntoString("", "something"))      #something