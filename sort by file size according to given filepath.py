# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:31:12 2022

@author: jefni
"""

import glob
import os

dir_name = input("Enter full path to sort by file size: ")
dir_name_len = len(dir_name) + 1

# Get a list of files (file paths) in the given directory 
list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/**/*', recursive=True))


list_of_files = sorted(list_of_files, key =  lambda x: os.stat(x).st_size, reverse=True)
print()
print('             MB | Full path & filename')
print('        ------------------------------')
for elem in list_of_files:
    file_size  = os.stat(elem).st_size 
    elem = str(elem)
    print('{:15f} | {:s}'.format(file_size, elem[dir_name_len:]))
