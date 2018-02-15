"""
class Search perform the search on a given path
working according custom filters
"""
from  src.com.jalasoft.search_files.search.directory import *
from  src.com.jalasoft.search_files.search.file import *
import os
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

    def set_advanced_search_criteria(self, path, name=None, extension=None, asset_type=None, size=None, size_less_than=None, owner=None, create_date):
        self.criteria = SearchCriteria(path, name, extension, asset_type, size, size_less_than, owner, create_date)

    def search_by_criteria(self):
        if self.criteria.get_criteria_value('name') == None \
                and self.criteria.get_criteria_value('asset_type') == None\
                and self.criteria.get_criteria_value('extension') == None:
            self.search_files_and_directories()

    def satisfies_criteria(self, asset):
        name_criteria = self.criteria.get_criteria_value('name')
        extension_criteria = self.criteria.get_criteria_value('extension')
        size_criteria = self.criteria.get_criteria_value('size')
        size_less_than_criteria = self.criteria.get_criteria_value('size_less_than')
        #owner_criteria = self.criteria.get_criteria.value('owner')
        asset_type_criteria = self.criteria.get_criteria_value('asset_type')

        if asset_type_criteria == 'dir' and isinstance(asset, File):
            return False
        if asset_type_criteria == 'file' and isinstance(asset, Directory):
            return False
        if isinstance(asset, Directory) and (asset_type_criteria is None or asset_type_criteria == 'dir'):
            if name_criteria is not None and name_criteria.lower() not in asset.name.lower():
                return False
            # owner_criteria = self.criteria.get_criteria.value('owner')
            # if owner_criteria is not None and asset.owner != owner_criteria:
            #     return False
            size_less_than_criteria = self.criteria.get_criteria_value('size_less_than')
            if size_criteria is not None and size_less_than_criteria == True and asset.size > size_criteria:
                return False
            if size_criteria is not None and size_less_than_criteria == False and asset.size < size_criteria:
                return False

        if isinstance(asset, File) and (asset_type_criteria is None or asset_type_criteria == 'file'):
            if name_criteria is not None and name_criteria.lower() not in asset.name.lower():
                return False
            if extension_criteria is not None and asset.extension.lower() != extension_criteria.lower():
                return False
            # if owner_criteria is not None and asset.owner != owner_criteria:
            #     return False
            if size_criteria is not None and size_less_than_criteria == True and asset.size > size_criteria:
                return False
            if size_criteria is not None and size_less_than_criteria == False and asset.size < size_criteria:
                return False
        return True



    def search_any_criteria(self):
        """
                :return:
                """
        logger.info("search_files_and_directories : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            asset_type_criteria = self.criteria.get_criteria_value('asset_type')
            owner_criteria = self.criteria.get_criteria_value('owner')
            #craete_date_criteria = self.criteria.get_criteria_value('create_date')
            if asset_type_criteria == None or asset_type_criteria == 'dir':
                for dir in directories:
                    directory = Directory(os.path.join(root, dir), dir)
                    if self.satisfies_criteria(directory):
                        self.result.append(directory.get_path())

            if asset_type_criteria == None or asset_type_criteria == 'file':
                for file in files:
                    file = File(os.path.join(root, file), file)
                    # Setting file owner only if this criteria is enabled for the search
                    if owner_criteria is not None:
                        file.set_owner()
                    # Setting file create_date only if this criteria is enabled for the search
                    # if create_date_criteria is not None:
                    #     file.set_create_date()
                    if self.satisfies_criteria(file):
                        self.result.append(file.get_path())
        logger.info("search_files_and_directories : Exit")

    def search_files_and_directories(self):
        """
        :return:
        """
        logger.info("search_files_and_directories : Enter")
        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):
            for dir in directories:
                directory = Directory(os.path.join(root, dir), dir)
                self.result.append(directory.get_path())

            for file in files:
                file = File(os.path.join(root, file), file)
                self.result.append(file.get_path())
        logger.info("search_files_and_directories : Exit")


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
        Searches all file and directories from a path, assiming that the seach criteria has only path defined

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