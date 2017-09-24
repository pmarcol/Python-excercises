"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java 
Output : java
"""

"""
SOLUTION:
"""

while True:
    elements = input('Give me a filename:').rstrip().split('.')
    if(len(elements)<2):
        print("Did you forget about extension? Try again.")
        continue
    else:
        break
    
fileExtension = elements[-1].lstrip()
print('Given file has the following extension: %s' % (fileExtension))
        
