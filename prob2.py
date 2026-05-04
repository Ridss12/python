'''write a python program to print the content of a directory using 
the os module search online for the function which does that'''

import os

# specify directory path (or use '.' for current directory)
path = "/"

# get list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)