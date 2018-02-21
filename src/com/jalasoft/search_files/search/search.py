"""
class Search perform the search on a given path
working according custom filters
"""
from  src.com.jalasoft.search_files.search.directory import *
from  src.com.jalasoft.search_files.search.file import *
import os
from src.com.jalasoft.search_files.search.search_criteria import *
from src.com.jalasoft.search_files.utils.logging_config import logger
from beautifultable import BeautifulTable

class Search():
    def __init__(self):
        """
        :param base_path: this parameter is main to search by any criteria
        """
        self.result = []
        self.criteria = {}


    def set_basic_search_criteria(self, path, name=None, extension=None, asset_type=None):
        self.criteria = SearchCriteria(path, name, extension, asset_type)

    def set_advanced_search_criteria(self, path, name=None, extension=None, asset_type=None, size=None, size_less_than=None, owner=None, create_date=None, create_date_less_than=None, modify_date=None, modify_date_less_than=None, last_access_date=None, content=None):
        self.criteria = SearchCriteria(path, name, extension, asset_type, size, size_less_than, owner, create_date, create_date_less_than, modify_date, modify_date_less_than, last_access_date, content)

    def satisfies_criteria(self, asset):
        name_criteria = self.criteria.get_criteria_value('name')
        extension_criteria = self.criteria.get_criteria_value('extension')
        size_criteria = self.criteria.get_criteria_value('size')
        size_less_than_criteria = self.criteria.get_criteria_value('size_less_than')
        owner_criteria = self.criteria.get_criteria_value('owner')
        asset_type_criteria = self.criteria.get_criteria_value('asset_type')
        create_date_criteria = self.criteria.get_criteria_value('create_date')
        create_date_less_than_criteria = self.criteria.get_criteria_value('create_date_less_than')
        modify_date_criteria = self.criteria.get_criteria_value('modify_date')
        modify_date_less_than_criteria = self.criteria.get_criteria_value('modify_date_less_than')
        last_access_date_criteria = self.criteria.get_criteria_value('last_access_date')
        content = self.criteria.get_criteria_value('content')

        if asset_type_criteria == 'dir' and isinstance(asset, File):
            return False
        if asset_type_criteria == 'file' and isinstance(asset, Directory):
            return False
        if isinstance(asset, Directory) and (asset_type_criteria is None or asset_type_criteria == 'dir'):

            if content is not None:
                return False
            if name_criteria is not None and name_criteria.lower() not in asset.name.lower():
                return False
            if size_criteria is not None and size_less_than_criteria is True and asset.size > size_criteria:
                return False
            if size_criteria is not None and size_less_than_criteria is False and asset.size < size_criteria:
                return False
            if create_date_criteria is not None and create_date_less_than_criteria is True and asset.created > create_date_criteria:
                return False
            if create_date_criteria is not None and create_date_less_than_criteria is False and asset.created <= create_date_criteria:
                return False
            if modify_date_criteria is not None and modify_date_less_than_criteria is True and asset.modified > modify_date_criteria:
                return False
            if modify_date_criteria is not None and modify_date_less_than_criteria is False and asset.modified <= modify_date_criteria:
                return False
            if last_access_date_criteria is not None and asset.last_access != last_access_date_criteria:
                return False

        if isinstance(asset, File) and (asset_type_criteria is None or asset_type_criteria == 'file'):

            if name_criteria is not None and name_criteria.lower() not in asset.name.lower():
                return False
            if extension_criteria is not None and asset.extension.lower() != extension_criteria.lower():
                return False
            if owner_criteria is not None and asset.get_owner() != owner_criteria:
                 return False
            if size_criteria is not None and size_less_than_criteria is True and asset.size > size_criteria:
                return False
            if size_criteria is not None and size_less_than_criteria is False and asset.size <= size_criteria:
                return False

            if create_date_criteria is not None and create_date_less_than_criteria is True and asset.created > create_date_criteria:
                return False

            if create_date_criteria is not None and create_date_less_than_criteria is False and asset.created <= create_date_criteria:
                return False

            if modify_date_criteria is not None and modify_date_less_than_criteria is True and asset.modified > modify_date_criteria:
                return False

            if modify_date_criteria is not None and modify_date_less_than_criteria is False and asset.modified <= modify_date_criteria:
                return False

            if last_access_date_criteria is not None and asset.last_access != last_access_date_criteria:
                return False
            if content is not None:
                return asset.search_by_content(content)
        return True

    def search_any_criteria(self):
        """
                :return:
                """

        last_result = BeautifulTable(220)
        last_result.column_headers = ["Path", "Size",  "Owner", "Asset Type", "Create Date", "Modified Date",
                                      "Last Access Date"]
        last_result.width_exceed_policy = last_result.WEP_WRAP
        last_result.default_alignment.ALIGN_LEFT
        logger.info("search_files_and_directories : Enter")

        for root, directories, files in os.walk(self.criteria.get_criteria_value('path')):

            asset_type_criteria = self.criteria.get_criteria_value('asset_type')
            if asset_type_criteria is None or asset_type_criteria == 'file':
                for file_name in files:

                    file = File(os.path.join(root, file_name), file_name)
                    if self.criteria.get_criteria_value('path') == "c:\\":
                        file.owner = ""
                    else:
                        file.set_owner()

                    if self.satisfies_criteria(file):

                        size_kb = "{0:.2f}".format(file.get_size() / 1024)
                        size_print = str(size_kb) + " KB (" + str(file.get_size()) + " bytes )"
                        last_result.append_row([file.get_path(), size_print, file.get_owner(), "File",
                                                file.get_created_date(),
                                                file.get_modified_date(),
                                                file.get_last_access()])

            if asset_type_criteria is None or asset_type_criteria == 'dir':
                for name in directories:
                    directory = Directory(os.path.join(root, name), name)
                    if self.satisfies_criteria(directory):
                        size_kb = "{0:.2f}".format(directory.get_size() / 1024)
                        size_print = str(size_kb) + " KB (" + str(directory.get_size()) + " bytes )"
                        last_result.append_row([directory.get_path(), size_print, "", "Directory",
                                                directory.get_created_date(),
                                                directory.get_modified_date(),
                                                directory.get_last_access()])
        if len(last_result) >= 1:
            print(last_result)
        else:
            print('\n No results found for the specified criteria. \n')
        logger.info("search_files_and_directories : Exit")