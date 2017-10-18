"""
Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

"""
SOLUTION:
"""

def uniqueAndSorted(myStr):
    words = myStr.split(',')
    uniqueWords = list(set(words))
    return(sorted(uniqueWords))

myStr1 = "atest,btest,test,test1,test,test,test2,aatest"
print(uniqueAndSorted(myStr1)) #[aatest, atest, btest, test, test1, test2]