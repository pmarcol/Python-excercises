"""
Write a Python program to sort a list of nested dictionaries.

NOTE: Copied the solution and introduced slight modifications to show the concept
"""

"""
SOLUTION:
"""

my_list = [{'key': {'subkey1': 1, 'subkey2' : 11}}, {'key': {'subkey1': 10, 'subkey2' : 6}}, {'key': {'subkey1': 5, 'subkey2' : 2}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey1'], reverse=True)
print("Sorted List: ")
print(my_list)
# [{'key': {'subkey1': 10, 'subkey2': 6}}, {'key': {'subkey1': 5, 'subkey2': 2}}, {'key': {'subkey1': 1, 'subkey2': 11}}]
my_list.sort(key=lambda e: e['key']['subkey2'], reverse=True)
print("Sorted List: ")
print(my_list)
# [{'key': {'subkey1': 1, 'subkey2': 11}}, {'key': {'subkey1': 10, 'subkey2': 6}}, {'key': {'subkey1': 5, 'subkey2': 2}}]