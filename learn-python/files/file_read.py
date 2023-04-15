'''
Reading file

For Windows,
    use backslash '\' and drive letter (C:\) as needed.
For Unix,
    use slash '/'

'''

import os.path  # get path from os

## With method
''' read file with method '''

# Read

with open(os.path.dirname(__file__) + '/../data/file_read.txt') as sample_file_read:
    sample_content = sample_file_read.read()
    print(sample_content)

##  simple non-general method
# with open('read_read.txt') as file_read:
#     content = file_read.read()
#     print(content)

# Readlines

with open(os.path.dirname(__file__) + '/../data/file_readlines.txt') as file_lines:
    lines_content = file_lines.readlines()
    for lines in lines_content:
        print(lines.strip())

## Store file data

# string

with open(os.path.dirname(__file__) + '/../data/file_data_str.txt') as file_lines:
    lines_content = file_lines.readlines()

data_str = ""
for data_lines in lines_content:
    data_str += data_lines.lstrip()

print(data_str)