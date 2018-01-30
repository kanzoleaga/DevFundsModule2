"""
Asset class
"""
import os
class Asset(object):
    def __init__(self, path, name):
        """

        :param path: path entered for the user to any search
        :param name:this contains file or directory name
        """

        self.path = path
        self.name = name
        self.size = os.path.getsize(path)
        self.is_directory = False

    def get_path(self):
        return self.path

    def get_size(self):
        return self.size

    def get_is_directory(self):
        return True

    def get_name(self):
        return self.name

    def set_is_directory(self, asset):
        self.is_directory = asset