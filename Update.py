#!/usr/bin/python

import sys
import editor

path = sys.argv[1].split(' ')[0] #The path sent through with the x-callback-url.
text = sys.argv[1].split(' ',1)[1] # A list of words from the file being copied.
#text = ' '.join(arguments) # Join the list into a single string.

this_path = '/var/mobile/Containers/Data/Application/DE7C6A0B-20CA-4DF3-8B54-7E3572E1FF19/Documents/WC_Sync/Update.py'

editor.open_file(this_path) # Replacing content of currently open file causes crashes

f = open(path, 'w') # To clear the file.
f.write(text) # Write the new code to the file.
f.close()

editor.open_file(path) # Return to original file.