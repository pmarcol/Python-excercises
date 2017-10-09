"""
Write a Python program to access and print a URL's content to the console.
"""

"""
SOLUTION:
"""

#from the source page:
"""
from http.client import HTTPConnection
conn9 = HTTPConnection("example.com")
conn9.request("GET", "/")
result = conn9.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
"""

#from stackoverflow:
import requests
response = requests.get("http://www.example.com")
print(response.content)
