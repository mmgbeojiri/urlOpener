import os
import sys
import webbrowser


url = str({sys.argv[1]})
print("Opening URL... ", url)
# Using urlopen() function with url in it  
webbrowser.open(url, new=2)
