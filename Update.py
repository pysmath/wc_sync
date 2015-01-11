#!/usr/bin/python

import sys

path = sys.argv[1] #The path sent through with the x-callback-url.
arguments = sys.argv[2:] # A list of words from the file being copied.
text = ' '.join(arguments) # Join the list into a single string.

f = open(path, 'w') # To clear the file.
f.write(text) # Write the new code to the file.
f.close()