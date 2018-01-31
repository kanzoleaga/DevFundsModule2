"""
File class inheritance from Asset
"""
import os
from src.com.jalasoft.search_files.search.asset import Asset

class File(Asset):
    def __init__(self, path, name):
        super().__init__(path, name)
        self.extension = os.path.splitext(name)[1]


    def get_extension(self):
        return self.extension


