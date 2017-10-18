"""
Write a Python function to get a string made of 4 copies of the last two characters of a specified string
(length must be at least 2).
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

"""
SOLUTION:
"""

def fourTimesEnd(myStr):
    if len(myStr) < 2:
        print("The given string must have length of at least 2")
        return
    return 4*myStr[-2:]

print(fourTimesEnd("a"))    #error
print(fourTimesEnd("test")) #stststst