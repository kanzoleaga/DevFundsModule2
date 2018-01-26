from src.com.jalasoft.search_files.search.asset import Asset

class File(Asset):
    def __init__(self, extension, path, name, size):
        Asset.__init__(self, path, name, size)
        self.extension = extension

    def get_extension(self):
        return self.extension
