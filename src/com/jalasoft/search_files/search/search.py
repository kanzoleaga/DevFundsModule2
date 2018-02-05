"""
class Search perform the search on a given path
working according custom filters
"""
from  src.com.jalasoft.search_files.search.directory import Directory
from  src.com.jalasoft.search_files.search.file import  File
import os
from src.com.jalasoft.search_files.utils.logging_config import LOGGER as LOGGER

class Search():
    def __init__(self, base_path):
        """

        :param base_path: this parameter is main to search by any criteria
        """
        self.base_path = base_path

    def search_files_and_directories(self):
        """

        :return:
        """

        LOGGER.info("search_files_and_directories : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                result.append(directory.get_path())

            for file in files:
                file = File(os.path.join(root, file), file)
                result.append(file.get_path())
        LOGGER.info("search_files_and_directories : Exit")
        return result

    def search_all_files(self):
        LOGGER.info("search_all_files : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                result.append(file.get_path())
        LOGGER.info("search_all_files : Exit")
        return result

    def search_all_directories(self):
        LOGGER.info("search_all_directories : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                result.append(directory.get_path())
        LOGGER.info("search_all_directories : Exit")
        return result

    def search_by_filter(self):
        pass

    def search_files_by_extension(self, extension):
        """

        :param extension:
        :return:
        """

        LOGGER.info("search_files_by_extension : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_name().lower().endswith(("." + extension).lower()):
                    result.append(file.get_path())
        LOGGER.info("search_files_by_extension : Exit")
        return result

    def search_files_by_name(self, name):
        """

        :param name:
        :return:
        """
        LOGGER.info("search_files_by_name : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if name.lower() in file.get_name().lower():
                    result.append(file.get_path())
        LOGGER.info("search_files_by_name : Exit")
        return result

    def search_files_less_than_size_bytes(self, size):
        LOGGER.info("search_files_less_than_size_bytes : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() < size:
                    result.append(file.get_path() + " -> " + str(file.get_size()))
        LOGGER.info("search_files_less_than_size_bytes : Exit")
        return result

    def search_files_greater_than_size_bytes(self, size):
        LOGGER.info("search_files_greater_than_size_bytes : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() > size:
                    result.append(file.get_path() + " -> " + str(file.get_size()))
        LOGGER.info("search_files_greater_than_size_bytes : Exit")
        return result

    def search_directories_by_name(self, name):
        LOGGER.info("search_directories_by_name : Enter")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                if name.lower() in directory.get_name().lower():
                    result.append(directory.get_path())
        LOGGER.info("search_directories_by_name : Exit")
        return result

    def search_directory_size(self):
        LOGGER.info("directory_size : Enter")
        size = 0
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                size += file.get_size()
        LOGGER.info("directory_size : Exit")
        return size

    def count_files_by_directory(self):
        LOGGER.info("count_files_by_directory : Enter")
        counter = 0
        for filenames in os.walk(self.base_path):
            for f in filenames[2]:
                counter += 1
        LOGGER.info("count_files_by_directory : Exit")
        return counter

if __name__ == "__main__":
    search = Search("C:\\test")

    print(search.search_files_and_directories())
    print(search.search_all_files())
    print(search.search_all_directories())
    print(search.search_files_by_extension("txt"))
    print(search.search_files_by_name("kate"))
    print(search.search_files_less_than_size_bytes(20000))
    print(search.search_files_greater_than_size_bytes(20000))
    print(search.search_directories_by_name("test2"))
    print("Directory size in bytes is: " + str(search.directory_size()))
    print("Directory has: " + str(search.count_files_by_directory()) + "  files")

