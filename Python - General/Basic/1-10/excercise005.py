"""
Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
"""

"""
SOLUTION:
"""

firstname = input('Give me your first name:')
lastname = input('Give me your last name:')
original = firstname + " " + lastname
reversed = lastname + " " + firstname
print(reversed)