#!/usr/bin/python

import sys
import editor

path = sys.argv[1]
arguments = sys.argv[2:]
text = ' '.join(arguments)

editor.replace_text(0,-1,text)

#print 'path - ', path
#print 'text - ', text