import os

class Asset(object):
    def __init__(self, path, name, size):
        self.path = path
        self.name = name
        self.size = size

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size
