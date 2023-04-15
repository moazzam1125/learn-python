'''
JSON (JavaScript Object Notation)
---------------------------------
The json format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.
json a datastore.
'''

import json
import os.path  # get path from os

# Dump file
''' write json file '''

with open(os.path.dirname(__file__) + '/../data/dump.json', 'w') as json_file:
    json_content = [1, 2, 3, 4, 5]
    json.dump(json_content, json_file)

# Load file
''' load json file '''

with open(os.path.dirname(__file__) + '/../data/dump.json') as json_file:
    json_content = json.load(json_file)
    print(json_content)