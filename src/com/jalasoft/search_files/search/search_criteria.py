from src.com.jalasoft.search_files.utils.logging_config import logger
from src.com.jalasoft.search_files.utils.validator import *

class SearchCriteria(object):

    def __init__(self, path, name=None, extension=None, asset_type=None, size=None, size_less_than=None,
                 owner=None, create_date=None, modify_date=None, last_access_date=None):
        """
        :param path: str This is the path where the searching is going to start. None is not supported
        :param name: str    This is the name of the file to be searched.
        :param extension: str  The extension of the file to be searched
        :param asset_type: str   The values accepted for this are file or dir
        :param size: int     The size in KB to be searched for
        :param size_less_than: bool  If False, files and directories greater than the size will be searched
        :param owner: str    The owner of the file
        :param create_date: datetime The creation date of the file
        :param modify_date: datetime The modification time of the file
        :param last_access_date: datetime. The last access date of the file
        """
        if not is_valid_path(path):
            raise AttributeError('Invalid attribute path')
        self.criteria = {
                        'path': path,
                        'name': name,
                        'extension': extension,
                        'asset_type': asset_type,
                        'size': size,
                        'size_less_than': size_less_than,
                        'owner': owner,
                        'create_date': create_date,
                        'modify_date': modify_date,
                        'last_access_date': last_access_date
        }

    def get_criteria_value(self, key):
        """
        This returns the value of an specific search criteria. For example it will return '.txt'
        in case the extension criteria has this value
        :param key: str the key name of the criteria
        :return:  the value of the criteria it may be an string or an integer
        """
        logger.info("get_criteria_value : Enter")
        if key in self.criteria.keys():
            return self.criteria[key]
        else:
            raise ValueError('Invalid key. Key value' + key + 'is not a valid criteria')

