"""
Write a Python program to clone or copy a list.
"""

"""
SOLUTION:
"""

original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
# Note: it is done this way, because simply making a reference new_list to original_list does not copy it.
print(original_list)    # [10, 22, 44, 23, 4]
print(new_list)         # [10, 22, 44, 23, 4]

new_list.append("test")
print()

print(original_list)    # [10, 22, 44, 23, 4]
print(new_list)         # [10, 22, 44, 23, 4, "test"]

#Now see what would happen if we just made a reference:
print()
print("Just making reference:")

original_list = [10, 22, 44, 23, 4]
new_list = original_list
print(original_list)    # [10, 22, 44, 23, 4]
print(new_list)         # [10, 22, 44, 23, 4]

new_list.append("test")
print()

print(original_list)    # [10, 22, 44, 23, 4, "test"]
print(new_list)         # [10, 22, 44, 23, 4, "test"]