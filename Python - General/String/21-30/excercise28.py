"""
Write a Python program to add a prefix text to all of the lines in a string.
"""

"""
SOLUTION:
"""

def addPrefix(aString, prefix):
    import textwrap
    return textwrap.indent(aString, prefix)

sample_text ='''
Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
as C++ or Java.
    '''

print(addPrefix(sample_text,"-->"))