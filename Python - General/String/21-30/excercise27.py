"""
Write a Python program to remove existing indentation from all of the lines in a given text.

NOTE: textwrap.dedent is given as solution here.
However, I do not know why it does not work if only some of the lines are indented
"""

"""
SOLUTION:
"""

import textwrap

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
'''

text_without_Indentation = textwrap.dedent(sample_text)

print(sample_text)
print(text_without_Indentation )