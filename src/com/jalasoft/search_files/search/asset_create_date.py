
import os
from datetime import datetime

path = os.getcwd()
total = 0
num_files = 0
date_format = '%d-%m-%y %H:%M:%S'
line = '-' * 60


for root, directories, files in os.walk(path, topdown=True):
    print('\nPath       :', root)
    for base_file in files:
        num_files += 1
        file = root + os.sep + base_file

        status = os.stat(file)
        size = status.st_size
        owner = status.st_file_attributes
        last_access = datetime.fromtimestamp(status.st_atime)
        modified = datetime.fromtimestamp(status.st_mtime)
        last_access = last_access.strftime(date_format)
        modified = modified.strftime(date_format)
        total += size
        print(line)
        print('File      :', base_file)
        print('Attribute      :', owner)
        print('Modified   :', modified)
        print('Lats access:', last_access)
        print('Size (Kb)  :', round(size / 1024, 1))

print(line)
print('Núm. Files:', num_files)
print('Total (kb)   :', round(total/1024, 1))
