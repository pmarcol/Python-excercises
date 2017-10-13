"""
Write a Python program to list home directory without absolute path.
"""

"""
SOLUTION:
"""

#from source page
import os
print(os.path.expanduser('~'))
#from stackoverflow - for Python 3.4+
from pathlib import Path
print(str(Path.home()))