"""
Write a Python program to empty a variable without destroying it. Go to the editor

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}

NOTE: Literally: WTF is this sample about
"""

"""
SOLUTION:
"""

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)

print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())

#NOTE: If I understand this right, the above commands just get the type of the variables and create new ones with,
# like, constructors with no arguments, so they (constructors) return default
# - 'empty' (whatever it means for the certain type) - value