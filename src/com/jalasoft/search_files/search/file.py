"""
File class inheritance from Asset
"""
from src.com.jalasoft.search_files.search.asset import Asset

class File(Asset):
    def __init__(self, path, name, extension):
        super().__init__(path, name)
        self.extension = extension

    def get_extension(self):
        return self.extension


