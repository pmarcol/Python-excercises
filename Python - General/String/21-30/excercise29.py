"""
Write a Python program to set the indentation of the first line.

NOTE: Solution copied, but I guess the excercise was about using initial_indent parameter.
"""

"""
SOLUTION:
"""

import textwrap

sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()

print(textwrap.fill(text1,
                    initial_indent='--->',
                    subsequent_indent='\t',
                    width=50,
                    ))