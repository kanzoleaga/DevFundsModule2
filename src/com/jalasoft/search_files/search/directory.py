import os
from  src.com.jalasoft.search_files.search.asset import Asset

class Directory(Asset):
    def __init__(self):
        Asset.__init__(self, "", "", "")
        self.is_directory = False

    def set_directory_name(self, directory_name):
        self.directory_name = directory_name

    def get_directory_name(self):
       return  self.directory_name

    def get_is_directory(self):
       return  self.get_is_directory

    def set_is_directory(self, is_directory ):
        self.is_directory = is_directory
