from  src.com.jalasoft.search_files.search.directory import Directory
from  src.com.jalasoft.search_files.search.file import  File
import os


class Search(object):
    def __init__(self, base_path):
        self.base_path = base_path
        self.directory = Directory()
        self.file = File("", "", "", "")


    def search_all_directories(self):
        list_asset = []
        for root, directories, files in os.walk(self.base_path):
            for dirs in directories:
                dir_all = os.path.join(root, dirs)
                list_asset.append(dir_all)
            for file in files:
                file = os.path.join(root, file)
                list_asset.append(file)
        return list_asset


    def search_all_files(self):
        pass

    def search_by_filter(self):
        pass

    def search_file_by_extesion(self):
        pass

    def search_file_by_content(self):
        pass

    def search_less_than_size(self):
        pass

    def search_greater_than_size(self):
        pass

    def search_only_sub_directories(self):
        pass

    def search_deeped_files(self):
        pass

    def count_files(self):
        pass

if __name__ == "__main__":
    search = Search("C:\\test")
    print(search.search_all_directories())