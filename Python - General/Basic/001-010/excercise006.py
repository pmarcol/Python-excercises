"""Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
"""

"""
SOLUTION:
"""

import sys
from pathlib import Path

abspath = Path(__file__)
toolspath = abspath.parents[3]
sys.path.append(str(toolspath / 'tools'))

from GetFromUser import GetListOfIntegers

while True:
    myList = GetListOfIntegers()
    if (len(myList)<=1):
        print("You should give at least two numbers. Try again.")
        continue
    else:
        break
    
numbersTuple = tuple(myList)

print('List: %s' % (myList))
print('Tuple: %s' % (numbersTuple,))

