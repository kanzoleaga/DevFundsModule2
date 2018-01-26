import os
from  src.com.jalasoft.search_files.search.asset import Asset

class Directory(Asset):
    def __init__(self):
        Asset.__init__(self, "", "", "")
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_children_number(self):
        return len(self.children)

    def get_all_files(self, base_path):
        pass

    def show_all_directories(self, base_path):
        for root, directories, files in os.walk(base_path):
            for dirs in directories:
                dir_all = os.path.join(root, dirs)
                print(dir_all)
