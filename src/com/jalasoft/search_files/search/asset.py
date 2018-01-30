class Asset(object):
    def __init__(self, path, name, size):
        self.path = path
        self.name = name
        self.size = size
        self.is_directory = False

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def set_path(self, path):
        self.path = path

    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size

    def get_is_directory(self):
        return self.is_directory
