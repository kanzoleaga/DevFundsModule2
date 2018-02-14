"""
Directory class inheritance from Asset
"""
import os
from  src.com.jalasoft.search_files.search.asset import Asset

class Directory(Asset):
    def __init__(self, path, name):
        super().__init__(path, name)
        self.child_dirs = []
        self.size = 0

    # Size was not set as pert of the constructor because of efficiency, It will be called only
    # if the search criteria includes size
    def set_size(self):
        start_path = self.path
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        self.size = total_size







