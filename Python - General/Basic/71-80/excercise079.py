"""
Write a Python program to get the size of an object in bytes.
"""

"""
SOLUTION:
"""

from sys import getsizeof

myObject1 = ['test', 9, 8.777, True, False, 'test22']
myObject2 = 'test'
myObject3 = 'testtest'

print(getsizeof(myObject1), 'bytes')
print(getsizeof(myObject2), 'bytes')
print(getsizeof(myObject3), 'bytes')