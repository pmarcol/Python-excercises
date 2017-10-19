"""
Write a Python program to create a Caesar encryption.

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher,
the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext
is replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.
"""

"""
SOLUTION:
"""

def ceasarEncryption(aString, shift):
    #I know, I should put some restrictions here (e.g. letters only - but I guess that is not the main objective here)
    return ''.join([chr(encryptedIndex(ord(c),shift)) for c in aString])

def encryptedIndex(original, shift):
    startIndex = 0
    #check whether encrypted character is capital or not
    if 64<original<91:
        startIndex = 65
    else:
        startIndex = 97
    return ((original - startIndex + shift) % 26) + startIndex

print(ceasarEncryption("MySecretMessage", 3)) #PbVhfuhwPhvvdjh
