"""
Write a Python function to create the HTML string with tags around the word(s).
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

"""
SOLUTION:
"""

def addTags(tag, myStr):
    return "<%s>%s</%s>" % (tag, myStr, tag)

print(addTags("bold", "Important Stuff"))