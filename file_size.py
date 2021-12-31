# -*- coding: utf-8 -*-

import glob
import os

''' INSERT PATH HERE'''
dir_name = "D:"

# recursive search with given directory name
list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/**/*', recursive=True))

# enumerate to add filesize, filepath
files_with_size = [(os.stat(files).st_size, files.replace("/", "\\", 1)) for files in list_of_files]

# sort largest file at top
files_with_size.sort(reverse=True)

# write output
''' INSERT OUTPUT FILENAME HERE'''
with open('file_size.txt', 'w') as fp:
    fp.write('Bytes    |    Filepath\n-----------------------------------------\n')
    fp.write('\n'.join('%s    |    %s' % x for x in files_with_size))
