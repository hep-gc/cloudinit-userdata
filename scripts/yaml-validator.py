#!/usr/bin/python
import os
import yaml
import sys
# Reads all files in current directory matching "*yaml*" and does some sanity checks

files = os.listdir(os.getcwd())
if len(files) == 1:
    print "Run from the parent directory i.e. $python scripts/yaml-validtor.py" 
    sys.exit(0)
print "Attempting to validate ~ %s files." % len(files)
buf = []
ebuf = []
for file in files:
    if 'yaml' in file:
        try:
            with open(os.getcwd() + '/' + file) as f:
                yaml.load(f)
                buf.append(".")
        except Exception as e:
            buf.append("x")
            ebuf.append(e)
            #print e
print ''.join(buf)
print '\n'.join(ebuf)
print "Done." 
