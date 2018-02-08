"""
class Search perform the search on a given path
working according custom filters
"""
from  src.com.jalasoft.search_files.search.directory import Directory
from  src.com.jalasoft.search_files.search.file import  File
import os
import fnmatch
from src.com.jalasoft.search_files.search.search_criteria import *
from src.com.jalasoft.search_files.utils.logging_config import logger

class Search():
    def __init__(self):
        """
        :param base_path: this parameter is main to search by any criteria
        """
        self.result = []
        self.criteria = {}

    def set_basic_search_criteria(self, path, name=None, extension=None, asset_type=None):
        self.criteria = SearchCriteria(path, name, extension, asset_type)

    def set_advanced_search_criteria(self, path, name=None, extension=None, size=None, asset_type=None):
        self.criteria = SearchCriteria(path, name, extension, size, asset_type)

    def search_by_criteria(self):
        if self.criteria.get_criteria_value('name') == None and self.criteria.get_criteria_value('asset_type') == None and self.criteria.get_criteria_value('extension') == None:
            Search.search_files_and_directories(self)

    def search_files_and_directories(self):
        """
        :return:
        """

        logger.info("search_files_and_directories : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                print (directory.get_path())
                self.result.append(directory.get_path())

            for file in files:
                file = File(os.path.join(root, file), file)
                self.result.append(file.get_path())
        logger.info("search_files_and_directories : Exit")
        return self.result

    def search_all_files(self):
        logger.info("search_all_files : Enter")
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                self.result.append(file.get_path())
        logger.info("search_all_files : Exit")
        return self.result

    def search_all_directories(self):
        logger.info("search_all_directories : Enter")
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                self.result.append(directory.get_path())
        logger.info("search_all_directories : Exit")
        return self.result

    def search_by_filter(self):
        pass

    def search_files_by_extension(self, extension):
        """

        :param extension:
        :return:
        """

        logger.info("search_files_by_extension : Enter")
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_name().lower().endswith(("." + extension).lower()):
                    self.result.append(file.get_path())
        logger.info("search_files_by_extension : Exit")
        return self.result

    def search_files_by_name(self):
        """

        :param name:
        :return:
        """
        logger.info("search_files_by_name : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                if self.criteria.get_criteria_value('name').lower() in file.get_name().lower():
                    self.result.append(file.get_path())
        logger.info("search_files_by_name : Exit")
        return self.result

    def search_files_less_than_size_bytes(self, size):
        logger.info("search_files_less_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() < size:
                    self.result.append(file.get_path() + " -> " + str(file.get_size()))
        logger.info("search_files_less_than_size_bytes : Exit")
        return self.result

    def search_files_greater_than_size_bytes(self, size):
        logger.info("search_files_greater_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() > size:
                    self.result.append(file.get_path() + " -> " + str(file.get_size()))
        logger.info("search_files_greater_than_size_bytes : Exit")
        return self.result

    def search_directories_by_name(self, name):
        logger.info("search_directories_by_name : Enter")
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                if name.lower() in directory.get_name().lower():
                    self.result.append(directory.get_path())
        logger.info("search_directories_by_name : Exit")
        return self.result

    def search_directory_size(self):
        logger.info("directory_size : Enter")
        size = 0
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                size += file.get_size()
        logger.info("directory_size : Exit")
        return size

    def count_files_by_directory(self):
        logger.info("count_files_by_directory : Enter")
        counter = 0
        for filenames in os.walk(self.base_path):
            for f in filenames[2]:
                counter += 1
        logger.info("count_files_by_directory : Exit")
        return counter

# if __name__ == "__main__":
#     search = Search("C:\\test")
#
#     print(search.search_files_and_directories())
#     print(search.search_all_files())
#     print(search.search_all_directories())
#     print(search.search_files_by_extension("txt"))
#     print(search.search_files_by_name("kate"))
#     print(search.search_files_less_than_size_bytes(20000))
#     print(search.search_files_greater_than_size_bytes(20000))
#     print(search.search_directories_by_name("test2"))
#     print("Directory size in bytes is: " + str(search.search_directory_size()))
#     print("Directory has: " + str(search.count_files_by_directory()) + "  files")
