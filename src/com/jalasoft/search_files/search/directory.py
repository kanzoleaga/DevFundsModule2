"""
Directory class inheritance from Asset
"""
from  src.com.jalasoft.search_files.search.asset import Asset

class Directory(Asset):
    def __init__(self, path, name):
        super().__init__(path, name)

        self.child_dirs = 0

    def set_dir_name(self, dir_name):
        return self.dir_name

    def set_dir_path(self, path):
        return self.path


