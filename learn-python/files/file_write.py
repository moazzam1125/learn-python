''' Writting file '''

import os.path  # get path from os

## With method

# Write file (Overwrite file)

with open(os.path.dirname(__file__) + '/../data/file_write.txt', 'w') as write_file:
    write_file.write("Write file from Files.")
    write_file.write("\nOverwrite file from Files.")

# Append to a file (writing to a file)

with open(os.path.dirname(__file__) + '/../data/file_append.txt', 'a') as write_file:
    write_file.write("Append to a file from Files.\n")