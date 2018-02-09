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
            self.result = self.search_files_and_directories()

    def search_files_and_directories(self):
        """
        :return:
        """

        logger.info("search_files_and_directories : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for a_dir in directories:
                directory = Directory(os.path.join(root, a_dir), a_dir)
                print(directory.get_path)
                self.result.append(directory.get_path())

            for file in files:
                file = File(os.path.join(root, file), file)
                #print(file.get_path())
                self.result.append(file.get_path())
                #print(self.result)
        logger.info("search_files_and_directories : Exit")
        return self.result

    def search_all_files(self):
        logger.info("search_all_files : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                self.result.append(file.get_path())
        logger.info("search_all_files : Exit")
        return self.result

    def search_all_directories(self):
        logger.info("search_all_directories : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                self.result.append(directory.get_path())
        logger.info("search_all_directories : Exit")
        return self.result

    def search_by_filter(self):
        pass

    def search_files_by_extension(self):
        """

        :param extension:
        :return:
        """

        logger.info("search_files_by_extension : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_name().lower().endswith(("." + self.criteria.get_criteria_value('extension')).lower()):
                    self.result.append(file.get_path())
        logger.info("search_files_by_extension : Exit")
        return self.result

    def search_files_and_directories_by_name(self):
        """

        :param name:
        :return:
        """
        logger.info("search_files_and_directories_by_name : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                if self.criteria.get_criteria_value('name').lower() in directory.get_name().lower():
                    self.result.append(directory.get_path())

            for file in files:
                file = File(os.path.join(root, file), file)
                if self.criteria.get_criteria_value('name').lower() in file.get_name().lower():
                    self.result.append(file.get_path())
        logger.info("search_files_and_directories_by_name : Exit")
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


    def search_files_and_directories_less_than_size_bytes(self):
        logger.info("search_files_and_directories_less_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                directory_size = Search.search_directory_size_from_path(self, directory.get_path())
                if directory_size < self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(directory_size / 1024)
                    self.result.append(directory.get_path() + " -> " + str(size_kb) + " KB (" + str(directory_size) + " bytes )")
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() < self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(file.get_size() / 1024)
                    self.result.append(file.get_path() + " -> " + str(size_kb) + " KB (" + str(file.get_size()) + " bytes )")
        logger.info("search_files_and_directories_less_than_size_bytes : Exit")
        return self.result

    def search_files_and_directories_greater_than_size_bytes(self):
        logger.info("search_files_and_directories_greater_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                directory_size = Search.search_directory_size_from_path(self, directory.get_path())
                if directory_size > self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(directory_size / 1024)
                    self.result.append(directory.get_path() + " -> " + str(size_kb) + " KB (" + str(directory_size) + " bytes )")


            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() > self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(file.get_size() / 1024)
                    self.result.append(file.get_path() + " -> " + str(size_kb) + " KB (" + str(file.get_size()) + " bytes )")
        logger.info("search_files_and_directories_greater_than_size_bytes : Exit")
        return self.result

    def search_files_less_than_size_bytes(self):
        logger.info("search_files_less_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() < self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(file.get_size() / 1024)
                    self.result.append(file.get_path() + " -> " + str(size_kb) + " KB (" + str(file.get_size()) + " bytes )")
        logger.info("search_files_less_than_size_bytes : Exit")
        return self.result

    def search_files_greater_than_size_bytes(self):
        logger.info("search_files_greater_than_size_bytes : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                if file.get_size() > self.criteria.get_criteria_value('size'):
                    size_kb = "{0:.2f}".format(file.get_size() / 1024)
                    self.result.append(file.get_path() + " -> " + str(size_kb) + " KB (" + str(file.get_size()) + " bytes )")
        logger.info("search_files_greater_than_size_bytes : Exit")
        return self.result

    def search_directories_by_name(self, name):
        logger.info("search_directories_by_name : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                if name.lower() in directory.get_name().lower():
                    self.result.append(directory.get_path())
        logger.info("search_directories_by_name : Exit")
        return self.result

    def search_directory_size(self):
        logger.info("directory_size : Enter")
        size = 0
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for file in files:
                file = File(os.path.join(root, file), file)
                size += file.get_size()
        logger.info("directory_size : Exit")
        return size

    def search_directory_size_from_path(self, file_path):
        logger.info("directory_size : Enter")
        size = 0
        for root, directories, files in os.walk(file_path):
            for file in files:
                file = File(os.path.join(root, file), file)
                size += file.get_size()
        logger.info("directory_size : Exit")
        return size

    def count_files_by_directory(self):
        logger.info("count_files_by_directory : Enter")
        counter = 0
        for filenames in os.walk(self.criteria.get_criteria_value('path')):
            for f in filenames[2]:
                counter += 1
        logger.info("count_files_by_directory : Exit")
        return counter

