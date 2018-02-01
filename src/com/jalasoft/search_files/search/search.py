"""
class Search perform the search on a given path
working according custom filters
"""
from  src.com.jalasoft.search_files.search.directory import Directory
from  src.com.jalasoft.search_files.search.file import  File
import os
import fnmatch
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

        LOGGER.info("=========start setting new value for search criteria=========")
        result = []
        for root, directories, files in os.walk(self.base_path):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                result.append(os.path.join(self.base_path,directory.get_name()))
                LOGGER.debug(self,'directories search', directory)

            for file in files:
                file = File(os.path.join(root, file), file)
                result.append(os.path.join(root,file.get_name()))
                LOGGER.info('Doing something')
        return result

    def search_all_files(self):
        pass
    def search_by_filter(self):
        pass

    def search_file_by_extension(self, extension):
        """

        :param extension:
        :return:
        """

        result = []
        for root, directories, files in os.walk(self.base_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_name().endswith(file.get_extension()):
                    result.append(os.path.join(root, file.get_name()))

        return result

    def searh_by_name(self, name):
        """

        :param name:
        :return:
        """
        name = name + ".*"
        result = []
        for root, dirnames, filenames in os.walk(self.base_path):
            for file in fnmatch.filter(filenames, name):
                file = File(os.path.join(root, file), file)
                result.append(os.path.join(root, file.get_name()))
        return result




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

    def count_files(self, counter=0):
        for filenames in os.walk(self.base_path):
            for f in filenames[2]:
                counter += 1
        return "we found " + str(counter) + "  files in " + self.base_path

if __name__ == "__main__":
    search = Search("C:\\test")

    print(search.search_files_and_directories())
    print(search.search_file_by_extension(".txt"))
    print(search.searh_by_name("kate"))
    print(search.count_files())