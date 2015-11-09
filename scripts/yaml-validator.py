import os
import yaml

# Reads all files in current directory matching "*yaml*" and does some sanity checks

files = os.listdir(os.getcwd())

for file in files:
    if 'yaml' in file:
        try:
            with open(os.getcwd() + '/' + file) as f:
                yaml.load(f)
        except Exception as e:
            print e
 
